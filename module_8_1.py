def add_everything_up(a, b):
    try:
        # Пробуем сложить a и b
        result = a + b
        # Если результат - float, округляем до 6 знаков после запятой
        if isinstance(result, float):
            return round(result, 6)
        return result
    except TypeError:
        # Если возникает TypeError (например, int + str), возвращаем строковое представление
        return f"{a}{b}"

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456