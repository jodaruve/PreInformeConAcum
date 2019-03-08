## mayor numero ingresado
num1=0
i=0
while i < 6:
  num=int(input("ingrese un numero"))
  i=i+1
  num1=num
  if num > num1:
    num1 = num
print(num1)