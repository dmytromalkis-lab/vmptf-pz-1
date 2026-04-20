while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        break
    except ValueError:
        print("Помилка! Потрібно вводити тільки числа. Спробуйте ще раз.\n")

sum_result = num1 + num2
print("Сума чисел:", sum_result)

input("Натисніть Enter, щоб завершити...")