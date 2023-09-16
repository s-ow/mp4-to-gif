from utils.common import *
from utils.librairies import *

def conversion(chemin, targetFormat):
    sortie = os.path.splitext(chemin)[0] + targetFormat

    print(f"""
[{lr}-{r}] Conversion du fichier : 
          {chemin}
[{g}+{r}] Vers :
          {sortie}
""")

    reader = imageio.get_reader(chemin)
    fps = reader.get_meta_data()['fps']
    durée = reader.get_meta_data()['duration']
    frames = int(durée * fps)

    writer = imageio.get_writer(sortie, duration=fps)

    bar = progressbar.ProgressBar(max_value=frames, prefix=f"Frames traitées :")

    for i,im in enumerate(reader):
            writer.append_data(im)
            bar.update(i)

    print(f"\n\n[{g}~{r}] Finalisation...")
    if frames >= 1000:
        print(f'[{lr}!{r}] Selon la taille de votre fichier, cette étape peut prendre un temps plus ou moins long, n\'hésitez pas à aller faire un tour !')
    writer.close()
    print(f"{g}[{r}>{g}] {r}Terminé.")



while True:
    clear()
    menu()

    choix = input(f"\n[{m}>{r}] Choix : ") 

    if choix == "3":
        os.kill(os.getppid(), 0)
        break

    elif choix == "1":
        path = input(f"\n[{m}>{r}] Chemin d'accès du fichier : ").replace("\"", "")
        try:
            imageio.get_reader(path)

            conversion(path, ".gif")

            input(f"\n{m}[{r}>{m}]{r} Appuyez sur ENTREE : ")

        except FileNotFoundError as e:
            print('Fichier introuvable.')
            time.sleep(2)

    elif choix == "2":
        Tk().withdraw()
        path = askopenfilename(filetypes = [("all video format", ".mp4")])
        try:
            imageio.get_reader(path)

            conversion(path, ".gif")

            input(f"\n{m}[{r}>{m}]{r} Appuyez sur ENTREE : ")

        except FileNotFoundError as e:
            print('Fichier introuvable.')
            time.sleep(2)



    else:
        print('Choix invalide')
        time.sleep(2)
