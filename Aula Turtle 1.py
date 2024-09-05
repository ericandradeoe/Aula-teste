import turtle

#Criando o objeto tartaruga
tartaruga = turtle.Turlte()

#Apontando para baixo e removendo a caneta
tartaruga.right(90)
tartaruga.penup()

#Configurando as fontes
fonte1 = ("Comic Sans", 20, "italic")
fonte2 = ("Comic Sans", 20, "normal")
fonte3 = ("Comic Sans", 30, "bold")

#Escrevendo "Curso"
tartaruga.write("Curso", False, "center", fonte1)
tartaruga.foward(40)

#Escrevendo "de"
tartaruga.write("de"), false, "center", fonte2)