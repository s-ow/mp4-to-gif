from utils.librairies import *

os.system("title MP4 to GIF")

# VARIABLES ===========================================================================

accueil = """

  __  __ ____  _  _     _           ____ ___ _____ 
 |  \/  |  _ \| || |   | |_ ___    / ___|_ _|  ___|
 | |\/| | |_) | || |_  | __/ _ \  | |  _ | || |_   
 | |  | |  __/|__   _| | || (_) | | |_| || ||  _|  
 |_|  |_|_|      |_|    \__\___/   \____|___|_|    
                                                   

"""
v = "1.1.0"
dev = "s-ow"
git = "https://github.com/s-ow/mp4-to-gif"

# COULEURS

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
r = Fore.RESET

# FONCTIONS ===========================================================================

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    Write.Print("                               __  __ ____  _  _     _           ____ ___ _____ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                              |  \/  |  _ \| || |   | |_ ___    / ___|_ _|  ___|\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                              | |\/| | |_) | || |_  | __/ _ \  | |  _ | || |_   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                              | |  | |  __/|__   _| | || (_) | | |_| || ||  _|  \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                              |_|  |_|_|      |_|    \__\___/   \____|___|_|    \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[Dev]:{dev}                                                                     \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[Version]:{v}                                                                   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[Github]:{git}                                                                   \n", Colors.purple_to_blue, interval=0.000)
    print(f"""

{m}[{r}1{m}]{r} Sélectionner un fichier via un chemin d'accès
{m}[{r}2{m}]{r} Sélectionner un fichier via l'explorateur de fichiers
{m}[{r}3{m}]{r} {Fore.RED}QUITTER{r}
""")
