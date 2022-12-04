# 5'. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Должно быть введено целое число")
    return number

def fib(n):
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def neg_fib(n: int) -> int: 
    return (-1)**(n+1)*fib(n)

def sequense_of_fibs(n: int) -> list[int]: 
    list1 = [neg_fib(i) for i in range(n+1)][::-1]
    list2 = [fib(i) for i in range(1, n+1)]
    return list1 + list2

num = InputNumbers("Введите число: ")

print(sequense_of_fibs(num))