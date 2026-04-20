class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Помилка: ділення на нуль!"
        return a / b

calc = Calculator()

try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    
    print("\nОберіть операцію:")
    print("1 - Додавання")
    print("2 - Віднімання")
    print("3 - Множення")
    print("4 - Ділення")
    
    choice = input("Ваш вибір: ")
    
    if choice == "1":
        print("Результат:", calc.add(a, b))
    elif choice == "2":
        print("Результат:", calc.subtract(a, b))
    elif choice == "3":
        print("Результат:", calc.multiply(a, b))
    elif choice == "4":
        print("Результат:", calc.divide(a, b))
    else:
        print("Невірний вибір операції.")
        
except ValueError:
    print("Помилка! Потрібно вводити тільки числа.")