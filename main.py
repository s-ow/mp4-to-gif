from utils.common import *
from utils.librairies import *

class formatFinal(object):
    GIF = ".gif"
    MP4 = ".mp4"

def conversion(chemin, targetFormat):
    sortie = os.path.splitext(chemin)[0] + targetFormat

    print(f"""
Conversion du fichier : 
          {chemin}
Vers :
          {sortie}
""")

    reader = imageio.get_reader(chemin)
    vid = imageio.get_reader(chemin, 'ffmpeg')
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(sortie, duration=fps)
    for i,im in enumerate(reader):
        sys.stdout.write(f"\rFrames traitées : {i}/{vid.count_frames()}")
        sys.stdout.flush()
        writer.append_data(im)
    print("\n\nFinalisation...")
    writer.close()
    print("Terminé.")



while True:
    clear()
    menu()

    path = input(f"\n[{m}>{r}] Chemin d'accès du fichier à convertir (pour quitter, tappez exit): ").replace("\"", "")

    if path == "exit":
        os.exit()
        break

    else:

        try:
            imageio.get_reader(path)

            conversion(path, formatFinal.GIF)

            time.sleep(2)

        except FileNotFoundError as e:
            print('Fichier introuvable.')
            time.sleep(2)

    