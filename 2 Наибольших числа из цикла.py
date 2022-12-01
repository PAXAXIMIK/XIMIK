num = int(input('Введите количество повторений: '))
large=0
largest=0
for i in range(num): #вводим количество повторений, которое необходимо
    n=int(input('Введите число: ')) #вводим сами числа
    if n > large: #если, n всегда больше предыдущего, то можно было обойтись и этим решением
        largest=large
        large=n
    elif n>largest:
        largest=n
print(f'Число меньше наибольшего из введенных чисел {largest}'), print (f'Наибольшее из введенных чисел {large}') 
