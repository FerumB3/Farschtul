print(f"NameError - {type(NameError)}- {issubclass(NameError,BaseException)}")

# try:
#     print("start code")
#     print(error)
#     print("No errors")
#
# except:
#     print("We have an error")
#
# print('code after caplus')

# try:
#     print(10/0)
#     print(error)
# except NameError:
#     print("u have NameError")
#
# try:
#     print(10 / 0)
# except NameError:
#     print("u have NameError")
#
# except ZeroDivisionError:
#     print("ZeroDivisionError")

# try:
#     a=int(input("first number"))
#     b = int(input("second numb"))
#     c = a / b
# print(c
# except ValueError:
#       print('not correct value')
# exept ZeroDivisionError:
#       print("u can not divide")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вийти")

    while True:
        choice = input("Введіть номер операції (1-5): ")


        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))
        elif choice == '3':
            print("Результат:", multiply(num1, num2))
        elif choice == '4':
            if num2 != 0:
                print("Результат:", divide(num1, num2))
            else:
                print("Помилка: Ділення на нуль!")
        else:
            print("Невірний вибір операції. Спробуйте ще раз.")
