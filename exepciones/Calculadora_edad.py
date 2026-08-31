import subprocess
from colorama import Fore, Style
while True:
    try:
        subprocess.run("cls", shell=True)
        edad = int(input("Edad: "))
        break
    except ValueError:
        print(Fore.RED + "Ingresa un valor numérico" + Style.RESET_ALL)
        subprocess.run("pause", shell=True)

print("Edad registrada: ", edad)