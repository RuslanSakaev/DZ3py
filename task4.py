# 4'. Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Должно быть введено целое число")
    return number

def ordinary_bin(num: int) -> str:
    return bin(num)[2::]

num = InputNumbers("Введите число: ")
print(ordinary_bin(num))