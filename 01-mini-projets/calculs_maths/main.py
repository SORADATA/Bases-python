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