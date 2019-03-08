## mayor numero ingresado
num1=0
i=0
num=int(input("ingrese un numero"))
while i < 6:
  i=i+1
  num1=num
  if num > num1:
    num1 = num
  num=int(input("ingrese un numero"))
print(num1)