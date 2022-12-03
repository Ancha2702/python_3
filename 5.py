#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n= int(input("Введите число N \n"))

def fibbonachi(n):
    """Расчет негафибоначчи

    Args:
        n (_int_): число до которого идет расчет (зеркальное) например, вводим 3 
        выводится интервал чисел от [-3...3]

    Returns:
        fib_list список_: _возвращает список чисел негафибоначчи и фибоначчи_в заданном интервале
    """
    fib_list=[]
    a, b = 1, 1
    for i in range(0,n-1):
        fib_list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fib_list.insert(0, a)
        a, b = b, a - b
    return fib_list
fib_list = fibbonachi(n)
print(fibbonachi(n))

