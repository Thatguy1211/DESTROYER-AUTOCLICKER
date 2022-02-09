import colorama
import keyboard, mouse, pyautogui
import time
from time import sleep
from colorama import init, Fore, Back, Style

init(convert=True) # Converte de texto normal para colorido, necessário em todos os programas com colorama

# Para quem quiser fazer títulos como o de baixo: 
blocks = '''╔ ═ ╗ ╦

╠ ╣ ╩ ╗ ║

╚ ╝'''

command_key = "R"
print(f'''

{Fore.WHITE}╔════════════════════════════════════════════════{Fore.MAGENTA}════╗
{Fore.WHITE}║  {Fore.MAGENTA}═╦══╗ ╔═══ ╔═══ ══╦══ ╦══╗ ╔══╗ ╔   ╗ ╔═══ ═╦══╗  ║
{Fore.WHITE}║  {Fore.MAGENTA} ║  ║ ║    ║      ║   ║  ║ ║  ║ ╚═╦═╝ ║     ║  ║  ║
{Fore.MAGENTA}║   ║  ║ ╠═══ ╚══╗   ║   ╠══╣ ║  ║   ║   ╠═══  ╠══╣  ║
║   ║  ║ ║       ║   ║   ║  ║ ║  ║   ║   ║     ║  ║  ║
║  ═╩══╝ ╚═══ ═══╝   ║   ╚  ╝ ╚══╝   ║   ╚═══  ╚  ╝  ║
╚════════════════════════════════════════════════════╝
{Fore.WHITE}╔══════════════════════════════════════════════════{Fore.MAGENTA}═╗
║ {Fore.CYAN}DESCRIÇÃO: {Fore.MAGENTA}                                       ║
║                                                   ║
║{Fore.WHITE} Destroyer autoclicker é um programa               {Fore.MAGENTA}║
║{Fore.WHITE}python que enquanto você estiver apertando         {Fore.MAGENTA}║
║{Fore.WHITE}uma tecla de sua escolha, o autoclicker irá clicar {Fore.MAGENTA}║
║{Fore.WHITE}até você parar de segurar tal tecla                {Fore.MAGENTA}║
╚═══════════════════════════════════════════════════╝

\t{Fore.CYAN}╔══════════════════════════════╗
\t║ Criado por {Fore.MAGENTA}that_guy1211.exe{Fore.CYAN}  ║
\t╚══════════════════════════════╝
''')
print(f"\t  {Fore.MAGENTA}╔══════════════════════════╗")
print(f"\t  {Fore.MAGENTA}║ Tecla de controle: {Fore.CYAN}[",command_key,f"]{Fore.MAGENTA} ║")
print(f"\t  {Fore.MAGENTA}╚══════════════════════════╝\n")

def click():
    mouse.click('left')
    time.sleep(0.00000001) # delay de 0.00000001 segundos para não fritar o PC
    currentMouseX, currentMouseY = pyautogui.position()
    print(f'{Fore.RED} [|]Clicando em [ X: ', currentMouseX, 'Y: ', currentMouseY, ' ]')

def on_press():
    while keyboard.is_pressed(command_key):
        click()
        break

while True:
    on_press()
