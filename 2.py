#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random 
number_n= int(input('Введите размерность массива \n'))
rand_list=[]
for i in range(number_n):
    rand_list.append(random.randint(0,10))
print(rand_list)
res=[]
def multiplication_el(rand_list):
    """произведение пар чисел из списка

    Args:
        rand_list (_список): список, заданный рандомно

    Returns:
      res (список)_: список, с произведением чисел_если у элемента списка нет пары он умножается сам на себя
    """
    if (len(rand_list))%2==1:
        for i in range (0,(len(rand_list)//2)+1):
            res.append(rand_list[i]*rand_list[len(rand_list)-i-1])
            
    else:
        for i in range (0,(len(rand_list)//2)):
            res.append(rand_list[i]*rand_list[len(rand_list)-i-1])
                   
    return res
print(multiplication_el(rand_list))