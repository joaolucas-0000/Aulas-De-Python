'João' # String
"Lucas" # String
c = """A expressão Lorem ipsum em design gráfico e editoração é um texto padrão em latim utilizado na produção gráfica para preencher os espaços de texto em publicações para testar e ajustar aspectos visuais antes de utilizar conteúdo real""" #String Mult line

print(c)


e = "hello word"
print(e[4]) # Coloque [] para decorrer numa cadeira de str

# cadeia de str literal
for x in "Gabriel":
    print(x + " - ") #ele vai imprimir o valor contido (cadeia de caracteres) na var x

aws = len(e) #retorna em num a qntd de caracteres que uma str tem
print(aws)
print(len(e))

txt = "Seja bem vindo ao curso de python"

x = "vindo" in txt # Verifica se essa palavra está presente na str txt
print(x)
print("carro" in txt) 

if "vindo" in txt:
    print("Sim, 'vindo' ok")

if "arroz" not in txt:        # Verifica se não está na var txt
    print("não está presente")



