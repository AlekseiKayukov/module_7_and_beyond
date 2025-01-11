def personal_sum(*numbers):
    total = 0
    incorrect_data = 0

    for i in numbers:
        for j in i:
            try:
                total += j
            except TypeError as exc:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчета суммы - {j}. Ошибка: {exc}")

    result = total, incorrect_data
    return result

def calculate_average(*numbers):
    try:
        total = personal_sum(*numbers)
        return total[0] / (len(*numbers) - total[1])
    except ZeroDivisionError as exc:
        print(f"Ошибка деления на 0 - {exc}")
        return 0
    except TypeError as exc:
        print(f"В numbers записан некорректный тип данных. Ошибка: {exc}")
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать