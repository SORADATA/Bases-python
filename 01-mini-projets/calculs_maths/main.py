# 1. Calculs arithmétiques

a = 9  # variable
print("a= ", a, "et type(a) = ", type(a))

x = "bonjour"
print("type(x)=", type(x))

# division entière et reste

a = 5
b = 2
c = 5.0
d = 2.0

print(a,"/", b, "=", a / b )
print(a,"/", d, "=", a / d )
print(a,"//", d, "=", a //d )

# Le reste de la div euclidienne ou Modulo = a%b

# Exple : a = bq + r
a = 17
b = 5

divmod(a, b)  
a // b        
a % b         

a, b = 17,5
print("a,b=", a,",",b)
print("q,r=",divmod(a,b))

# Valeur absolue d'un nombre

x=-3.14
print("x=",x,"donc valeur absolue de x=",abs(x))


# Priorité des opérateurs
a=6
b=10
c=6
x=a*b//c
y=a*(b//c)
print("x=", x)
print("x=", y)

### Nombre complexe
#z = x + iy comme z = complex(x,y)

a=2-1j
b=-10-5j
c=3+11j
print("a=", a, ", b=", b, ", c=", c)
D=b**2-4*a*c
print("Discriminant=", D)
d=D**(1/2)
print("delta=", d)
z1=(-b-d)/(2*a)
z2=(-b+d)/(2*a)
print("solutions de l'équation az**2+bz+c=0")
print("z1=",z1)
print("z2",z2)

x="Boileau a dit : \n"
y1="\t Hâtez-vous lentement, et sans perdre courage, \n"
y2="\t Vingt fois sur le métier remetez votre ouvrage :\n"
y3="\t Polissez-le sans cesse et le repolissez ! \n"
print(x, y1, y2, y3)


x=3
y=5
print("x =", x , end=" & ")
print("y = ",y)