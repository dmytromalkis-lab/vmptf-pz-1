try:
    num = int(input("Введіть число: "))
    if num <= 1:
        print("Число не є простим.")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Число є простим.")
        else:
            print("Число не є простим.")
except ValueError:
    print("Помилка! Потрібно вводити тільки ціле число.")