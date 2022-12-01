a=int(input())
total=''
while a!=0:
    c=a%10
    total+=str(c)
    a//=10
print('Максимальная цифра равна',max(total))
print('Минимальная цифра равна',min(total)) 
