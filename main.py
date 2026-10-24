# Étape 1 : On importe les boîtes à outils de Python pour la compression
import os       # Pour mesurer la taille des fichiers
import bz2      # Pour l'algorithme bzip2
import lzma     # Pour l'algorithme lzma
import zipfile  # Pour simuler l'algorithme 7-zip (archives)

print("=== DEBUT DU PROGRAMME DE COMPRESSION ===")

# Étape 2 : On demande à l'utilisateur quel fichier il veut tester
nom_fichier = input("Entre le nom du fichier à compresser (ex: texte.txt) : ")

# On vérifie si le fichier existe vraiment
if not os.path.exists(nom_fichier):
    print("Erreur : Le fichier n'existe pas dans le dossier !")
else:
    # 1. RECUPERER LA TAILLE DE DEPART
    taille_initiale = os.path.getsize(nom_fichier)
    print(f"\nFichier choisi : {nom_fichier}")
    print(f"Taille originale : {taille_initiale} octets")

    # 2. TEST DE L'ALGORITHME BZIP2
    print("\n--- Test de l'algorithme BZIP2 ---")
    
    # Lecture du fichier d'origine
    fichier_original = open(nom_fichier, "rb")
    donnees = fichier_original.read()
    fichier_original.close()

    # Compression des données avec bz2
    donnees_compressees_bz2 = bz2.compress(donnees)

    # Écriture dans un nouveau fichier compressé (.bz2)
    nom_sortie_bz2 = nom_fichier + ".bz2"
    fichier_sortie = open(nom_sortie_bz2, "wb")
    fichier_sortie.write(donnees_compressees_bz2)
    fichier_sortie.close()

    # Calcul de la nouvelle taille et du pourcentage de réduction
    taille_bz2 = os.path.getsize(nom_sortie_bz2)
    gain_bz2 = (1 - (taille_bz2 / taille_initiale)) * 100
    print(f"Taille après BZIP2 : {taille_bz2} octets")
    print(f"Gain d'espace : {gain_bz2:.2f}%")


    # 3. TEST DE L'ALGORITHME LZMA
    print("\n--- Test de l'algorithme LZMA ---")

    # Compression avec lzma
    donnees_compressees_lzma = lzma.compress(donnees)

    # Écriture dans un nouveau fichier compressé (.xz)
    nom_sortie_lzma = nom_fichier + ".xz"
    fichier_sortie = open(nom_sortie_lzma, "wb")
    fichier_sortie.write(donnees_compressees_lzma)
    fichier_sortie.close()

    # Calcul de la nouvelle taille et du pourcentage
    taille_lzma = os.path.getsize(nom_sortie_lzma)
    gain_lzma = (1 - (taille_lzma / taille_initiale)) * 100
    print(f"Taille après LZMA : {taille_lzma} octets")
    print(f"Gain d'espace : {gain_lzma:.2f}%")


    # 4. TEST DE L'ALGORITHME 7-ZIP (via ZIP)
    print("\n--- Test de l'algorithme 7-ZIP / ZIP ---")

    nom_sortie_zip = nom_fichier + ".zip"
    
    # Création d'une archive zip pour compresser le fichier
    archive = zipfile.ZipFile(nom_sortie_zip, "w", zipfile.ZIP_DEFLATED)
    archive.write(nom_fichier)
    archive.close()

    # Calcul de la taille et du pourcentage
    taille_zip = os.path.getsize(nom_sortie_zip)
    gain_zip = (1 - (taille_zip / taille_initiale)) * 100
    print(f"Taille après 7-ZIP/ZIP : {taille_zip} octets")
    print(f"Gain d'espace : {gain_zip:.2f}%")

    print("\n=== FIN DES TESTS : Tout s'est bien passé ! ===")