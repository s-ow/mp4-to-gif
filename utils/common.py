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
v = "1.0.0"
dev = "s-ow"

# COULEURS

r = Fore.RESET
m = Fore.MAGENTA

# FONCTIONS ===========================================================================

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    Write.Print("                               __  __ ____  _  _     _           ____ ___ _____ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                              |  \/  |  _ \| || |   | |_ ___    / ___|_ _|  ___|\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                              | |\/| | |_) | || |_  | __/ _ \  | |  _ | || |_   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[Dev]:{dev}                    | |  | |  __/|__   _| | || (_) | | |_| || ||  _|  \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[Version]:{v}               |_|  |_|_|      |_|    \__\___/   \____|___|_|    \n", Colors.purple_to_blue, interval=0.000)