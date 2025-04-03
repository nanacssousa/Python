
### **Exercício 05 - Desenho com ColabTurtlePlus**
import ColabTurtlePlus.Turtle as turtle

# Inicializa a tartaruga e configura o ambiente
turtle.initializeTurtle()
turtle.speed(5)

LADO = 100  # Define o tamanho do lado do quadrado e o raio do círculo

# Desenhar o círculo
turtle.penup()
turtle.goto(0, -LADO)
turtle.pendown()
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.circle(LADO)
turtle.end_fill()

# Desenhar o quadrado
turtle.penup()
turtle.goto(-LADO/2, LADO/2)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(LADO)
    turtle.right(90)
turtle.end_fill()

### **Exercício 01 - Correção do Código de Bhaskara**
O código apresentado não corresponde à fórmula de Bhaskara, mas sim ao cálculo da área de um triângulo usando a fórmula de Heron. Aqui está a correção para Bhaskara:

import math

# Entrada dos coeficientes da equação quadrática
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Cálculo do discriminante
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes da equação são {x1:.2f} e {x2:.2f}")
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação tem uma raiz única: {x:.2f}")
else:
    print("A equação não possui raízes reais.")
```

---

### **Lista de alunos - Manipulação de Listas**
```python
# Lista de alunos e notas
alunos = [["Vanessa", "Pietro", "Janaina", "Gregório", "Quitéria"],
          [5.0, 7.5, 10.0, 6.0, 7.5]]

# a) Acessar o nome e a nota do quarto aluno
nome_quarto = alunos[0][3]
nota_quarto = alunos[1][3]
print(f"Nome: {nome_quarto}, Nota: {nota_quarto}")

# b) Remover Pietro da lista
indice_pietro = alunos[0].index("Pietro")
alunos[0].pop(indice_pietro)
alunos[1].pop(indice_pietro)

# c) Adicionar Ricardo e sua nota 8.5
alunos[0].append("Ricardo")
alunos[1].append(8.5)

# d) Calcular a média das notas
media = sum(alunos[1]) / len(alunos[1])
print(f"Média da turma: {media:.2f}")
```

Esses códigos devem resolver os problemas conforme descrito nas imagens. Se precisar de ajustes ou explicações, me avise! 🚀