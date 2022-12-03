#3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
import random 
number_n= int(input('Введите размерность массива \n'))
rand_list=[]
rand_int_list=[]
for i in range(number_n):
    rand_list.append(random.random())
    rand_int_list.append(0)
print(rand_list)
def round_numb(rand_int_list):
    for i, el in enumerate(rand_list):
        rand_int_list[i] = round((el % 1) * 1000000000)
    return(rand_int_list)
max_n= max(round_numb(rand_int_list))
min_n=min(round_numb(rand_int_list))
print(round_numb(rand_int_list))
print(f'Разница между максимальным и минимальным значением: {(max_n)-min_n}')
  