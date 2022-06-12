import random

# Variaves de tipo int

a = 1
b = 35091381074309824
c = -1532

print((type(a)))
print((type(b)))
print((type(c)))

d = 1.10
e = 1.0
f = -35.9
g = 34E4
h = 12e0
i = -87.4e12


print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

j = 3+5j # Esse j indica que esse valor (3+5) é um number complexo
k = 5j # Outro numero complexo
l = -5j # numero complexo negativo

print(type(j))
print(type(k))
print(type(l))

# converter de int para float
x = float(1)

# converter de float para int
y = int(3.8)

# converter de int para complex
z = complex(x)

print(x)
print(y)
print(z)
# O tipo das variveis
print(type(x))
print(type(y))
print(type(z))
# Não se converte complex para nenhum outro tipo, mas o contrario pode

# Gera numeros aletorios entre 1 a 10
rnd = random.randrange(1,10)
print(rnd)
# ou
print(random.randrange(1, 10))
print("\n")

