import  math
m=float(input("Comprimento do cateto oposto "))
n=float(input("Comprimento do cateto adjacente"))
h=math.hypot(m,n)
print (f"A  hipotenusa vai medir {h:.2f}")
