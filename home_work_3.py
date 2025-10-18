import sys

from pathlib import Path
from colorama import Fore, Style

SKIP_FOLDERS = ('venv', '.evn', 'hooks', 'objects', '.git')
TAB = ' ' * 2

def visualize_directory_structure(folder: str, sign = TAB) -> None:
    for index, item in enumerate(folder.iterdir()):
        if item.name in SKIP_FOLDERS:
            continue

        if item.is_dir():
            print(f"{Fore.YELLOW}{Style.BRIGHT}{sign}┣ 📂 {item.name}")
            visualize_directory_structure(item, f'{sign}┃{TAB}')
        elif item.is_file():
            print(f"{Fore.GREEN}{Style.NORMAL}{sign}┗ 📜 {item.name}")



if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            parent_folder = Path(sys.argv[1]).parent.resolve()
        else:
             parent_folder = Path(__file__).parent

        print(f"{Fore.MAGENTA}📦 {parent_folder.name}{Style.RESET_ALL}")
        visualize_directory_structure(parent_folder)

    except FileNotFoundError:
        print(f"Error: File or directory not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Access denied.")
        sys.exit(1)

#  py .\home_work_3.py
#  py .\home_work_3.py ".." 
#  py .\home_work_3.py "../.." 


# Створення та використання віртуального оточення.
# Правильність отримання та обробки шляху до директорії.
# Точність виведення структури директорії.
# Коректне застосування кольорового виведення за допомогою colorama.
# Якість коду, включаючи читабельність, структурування та коментарі.

# Приклад використання:
# 📦picture
#  ┣ 📂Logo
#  ┃ ┣ 📜IBM+Logo.png
#  ┃ ┣ 📜ibm.svg
#  ┃ ┗ 📜logo-tm.png
#  ┣ 📜bot-icon.png
#  ┗ 📜mongodb.jpg
