#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random 
number_n= int(input('Введите размерность массива \n'))
rand_list=[]
for i in range(number_n):
    rand_list.append(random.randint(0,100))
print(rand_list)
def summ_neg_elem(rand_list):
    """Cумма элементов списка, стоящих на нечетных позициях

    Args:
        rand_list (список): генерируемый список, элементы которого будут суммироваться

    Returns:
       summ_n _int_: переменная, куда записыватся сумма элементов, стоящих на нечетной позиции_
    """
    summ_n=0
    for i in range (1, len(rand_list),2):
        summ_n+=rand_list[i]
    return summ_n
print (summ_neg_elem(rand_list))
