def get_cats_info(path: str) -> list:
  cats_list: list = []
    
  try:
    # Відкриваємо файл з явним вказанням кодування для уникнення проблем з символами
    with open(path, 'r', encoding='utf-8') as file:
      for line in file:
        # Очищуємо рядок від символів перенесення та зайвих пробілів
        clean_line = line.strip()
        
        # Пропускаємо порожні рядки, якщо вони є у файлі
        if not clean_line:
          continue
          
        try:
          # Розділяємо рядок за комою
          # Очікуємо формат: id, name, age
          cat_id, name, age = clean_line.split(',')
          
          # Створюємо словник для поточного кота
          cat_dict: dict = {
            "id": cat_id,
            "name": name,
            "age": age
          }
          
          # Додаємо словник до загального списку
          cats_list.append(cat_dict)
            
        except ValueError:
          print(f"Попередження: Рядок '{clean_line}' має некоректний формат і був пропущений.")
          continue
                
    return cats_list

  except FileNotFoundError:
    print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
    return []
  except Exception as e:
    print(f"Виникла непередбачена помилка: {e}")
    return []


# Приклад використання функції
if __name__ == "__main__":
  path: str = "cats.txt"

  cats_info = get_cats_info(path)
  print(cats_info)