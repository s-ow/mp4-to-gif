import os
import sys
import time
import imageio
import colorama
from colorama import Fore
from pystyle import Add, Anime, Center, Colorate, Colors, System, Write

try:
    import time
except:
    os.system("pip install time")
    import time

try:
    import imageio
except:
    os.system("pip install imageio")
    os.system("pip install imageio[ffmpeg]")
    import imageio

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import pystyle
except:
    os.system("pip install pystyle")
    import pystyle