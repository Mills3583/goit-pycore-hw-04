import sys
from pathlib import Path
import colorama


def visualize_directory_structure(path: Path, indent: str = ""):
  """
  Рекурсивно виводить структуру директорії з кольоровим маркуванням.
  """
  try:
    # Отримуємо відсортований список вмісту (спочатку папки, потім файли)
    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
      
    for i, item in enumerate(items):
      # Визначаємо, чи це останній елемент у списку для коректного малювання гілок
      is_last = (i == len(items) - 1)
      connector = "┗ " if is_last else "┣ "
        
      if item.is_dir():
        # Виводимо назву директорії синім кольором
        print(f"{indent}{connector}{colorama.Fore.BLUE}{item.name}/")

        # Рекурсивний виклик для піддиректорії з додатковим відступом
        new_indent = indent + ("  " if is_last else "┃ ")
        
        visualize_directory_structure(item, new_indent)
      
      else:
        # Виводимо назву файлу зеленим кольором
        print(f"{indent}{connector}{colorama.Fore.GREEN}{item.name}")
              
  except PermissionError:
    print(f"{indent}{colorama.Fore.RED}[Доступ заборонено]")


def main():
  # Перевірка наявності аргументу командного рядка
  if len(sys.argv) < 2:
    print(f"{colorama.Fore.YELLOW}Використання: python task3.py <шлях_до_директорії>")
    return

  # Формуємо шлях з аргументу
  target_path = Path(sys.argv[1])

  # Перевірка на існування та чи є це директорією
  if not target_path.exists():
    print(f"{colorama.Fore.RED}Помилка: Шлях '{target_path}' не існує.")
    return
  
  if not target_path.is_dir():
    print(f"{colorama.Fore.RED}Помилка: Шлях '{target_path}' не є директорією.")
    return

  # Виведення кореневої папки
  print(f"{colorama.Fore.MAGENTA}:{target_path.name}")
  visualize_directory_structure(target_path)


# Приклад використання функції
if __name__ == "__main__":
  main()