def add_everything_up(a, b):
    try:
        return float(a) + float(b)
    except ValueError as exc:
        return str(a) + str(b)
    except TypeError as exc:
        print(f"Ошибка {exc}. Невозможно сложить значение {a} и {b}!")
        return None

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))