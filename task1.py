def total_salary(path: str) -> tuple:
  total: int = 0
  count: int = 0
    
  try:
    # Відкриваємо файл за допомогою менеджера контексту 'with'
    # Вказуємо кодування utf-8 для коректного читання символів
    with open(path, 'r', encoding='utf-8') as file:
        
      for line in file:
        # Видаляємо зайві пробіли/символи перенесення рядка та розділяємо по комі
        line = line.strip()
      
        if not line:
          # Пропускаємо порожні рядки, якщо вони є
          continue
          
        try:
          _, salary_str = line.split(',')
          total += float(salary_str)
          count += 1
    
        except ValueError:
          print(f"Помилка обробки рядка: '{line}'. Невірний формат.")
          continue
      
    if count == 0:
        return 0, 0
          
    average = total / count
    
    return total, average

  except FileNotFoundError:
    print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
    return 0, 0
  except Exception as e:
    print(f"Виникла непередбачена помилка: {e}")
    return 0, 0


# Приклад використання функції
if __name__ == "__main__":
  path: str = 'salaries.txt'
  
  total, average = total_salary(path)
  print(f"Загальна сума заробітної плати: {round(total, 2)}, Середня заробітна плата: {round(average, 2)}")