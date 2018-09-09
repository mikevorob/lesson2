def sum (a, b):
    s=a+b
    return s


a=input("Введите 1ое слагаемое: ")
b=input("Введите 2ое слагаемое: ")
try:
    a=int(a)
    b=int(b)
except ValueError:
    print("неверный ввод данных")
else:
    print(sum(a,b))
 