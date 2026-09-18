#Zadanie 3
try:
    num1 = int(input("Введите первое целое число (num1): "))
    num2 = int(input("Введите второе целое число (num2): "))
    result = num1 + num2
    print(f"Результат сложения: {num1} + {num2} = {result}")

except ValueError:
    print("Вводите только целые ЧИСЛА")
