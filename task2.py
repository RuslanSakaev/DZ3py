# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

def pair_mult(nums: list[int]) -> list:
    pairs = []
    iterations = int(round((len(nums)+1)/2))
    print(iterations)
    for i in range(iterations):
        pairs.append(nums[i]*nums[-1-i])
    return pairs

print(pair_mult([2, 3, 5, 6]))