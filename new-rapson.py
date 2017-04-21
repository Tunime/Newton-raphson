from sympy import *
x=Symbol('x')

#f=x*sin(1/x)-0.2*E**-x
f=1980*(1-E**(-(x/10)))-98*x
#f=(-E**(-x))-1
fd=diff(f,x)
print("Funcion : ",f)
print("derivada : ",fd)

numax=int(input("Numero de iteraciones : "))
tol=float(input("Tolerancia : "))
print("tiene intervalos s/n")
p=input("S/N : ")
if(p=="s"):
  xo=float(input("Valor inicial : "))
  print("Interfalos")
  a=float(input("a : "))
  b=float(input("b : "))

else:
  a=float(input("rango a : "))
  b=float(input("rango b : "))
  ban=(b-a)/2
  ab=a+ban
  ax=1
  while(ax==1):
    fa=f.subs(x,a)
    fb=f.subs(x,ab)
    if(fa*fb<0):
      a=a
      b=ab
      ban=(b-a)/2
      ab=a+ban
    else:
      a=ab
      b=b
      ban=(b-a)/2
      ab=a+ban
    if(((ab+1)/b)<=1):
      ax=0
      xo=a
      print("Intervalo : [",a,"-",b,"]")
      print("valor inicial  xo : ",a)
    else:
      ax=1


fa=f.subs(x,a)
fb=f.subs(x,b)
#print(fa*fb)
if(fa*fb<0):
  i=1
  b=0
  while(i<=numax):
    fxo=f.subs(x,xo)
    fdxo=fd.subs(x,xo)
    xa=xo-(fxo)/fdxo
    if(abs(xa-xo)<tol):
      i=numax+1
      b=1
    else:
      xo=xa
      i=i+1
  if(b==1):
    print("El resultado es : ",xa)
  else:
    print("supera las iteraciones")

else:
  print("Esta seguro que existe la raiz")
