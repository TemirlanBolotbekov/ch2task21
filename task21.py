#Напишите функцию которая будет суммировать введенные 
#три случайные цифры.

def add(a,b,c):
    summ = a+c+b
    return summ
a = int(input("Enter number :"))
b = int(input("Enter number :"))
c = int(input("Enter number :"))
print(add(a,b,c))
 