# 1.
# Faça uma função em Python que solicite a digitação de dois valores quaisquer,
# informando-os em seguida em ordem crescente.

def ordem_2_crescente():
    valor1= float(input("Coloque o primeiro valor"))
    valor2= float(input("Coloque o segundo valor"))
    if valor1<=valor2:
        print(valor1, valor2)
    else:
        print(valor2, valor1)

# 2.
# Faça uma função em Python que solicite a digitação de três valores quaisquer,
# informando-os em seguida em ordem crescente.

def ordem_3_crescente():
    valor1= float(input("Coloque o primeiro valor"))
    valor2= float(input("Coloque o segundo valor"))
    valor3= float(input("Coloque o terceiro valor"))
    if valor1<=valor2 <= valor3:
        print(valor1, valor2, valor3)
    elif valor1<= valor3 <=valor2:
        print(valor1, valor3, valor2)
    elif valor2<= valor1 <= valor3:
        print(valor2, valor1, valor3)

    elif valor2<= valor3 <= valor1:
        print(valor2, valor3, valor1)

    elif valor3<= valor1 <= valor2:
        print(valor3, valor1, valor2)
    
    elif valor3<= valor2 <= valor1:
        print(valor3, valor2, valor1)

# 3.
# Faça uma função em Python que solicite a digitação de quatro valores quaisquer,
# informando-os em seguida em ordem crescente.

def ordem_4_crescente():

    valor1= float(input("Coloque o primeiro valor"))
    valor2= float(input("Coloque o segundo valor"))
    valor3= float(input("Coloque o terceiro valor"))
    valor4= float(input("Coloque o terceiro valor"))

    if valor1<= valor2 <= valor3 <= valor4:
        print(valor1, valor2, valor3, valor4)
    elif valor1<= valor2 <= valor4 <= valor3:
        print(valor1, valor2, valor4, valor3)
    elif valor1<= valor3 <= valor2 <= valor4:
          print(valor1, valor3, valor2, valor4)
    elif valor1 <= valor3 <= valor4 <= valor2:
        print(valor1, valor3, valor4, valor2)
    elif valor1 <= valor4 <= valor2 <= valor3:
        print( valor1, valor4, valor2, valor3)
    elif valor1 <= valor4 <= valor3 +valor2:
        print(valor1, valor4, valor3, valor2)
    elif valor2 <= valor1 <= valor3 <+ valor4:
        print(valor2, valor1, valor3, valor4)
    elif valor2 <= valor1 <= valor4 <= valor3:
        print(valor2, valor1, valor4, valor3)
    elif valor2 <= valor3 <= valor1 <= valor4:
        print(valor2, valor3, valor1, valor4)
    elif valor2 <= valor3 <= valor4 <= valor1:
        print(valor2, valor3, valor4, valor1)
    elif valor2 <= valor4 <= valor1 <= valor3:
        print(valor2, valor4, valor1, valor3)
    elif valor2 <= valor4 <= valor3 <= valor1:
        print(valor2, valor4, valor3, valor1)
    elif valor3 <= valor1 <= valor2 <= valor4:
        print(valor3, valor1, valor2, valor4)
    elif valor3 <= valor1 <= valor4 <=valor2:
        print(valor3, valor1, valor4, valor2)
    elif valor3 <= valor2 <= valor1 <= valor4:
        print(valor3, valor2, valor1, valor4)
    elif valor3 <= valor2 <= valor4 <= valor1:
        print(valor3, valor2, valor4, valor1)
    elif valor3 <= valor4 <= valor1 <= valor2:
        print(valor3, valor4, valor1, valor2)
    elif valor3 <= valor4 <= valor2 <= valor1:
        print(valor3, valor4, valor2, valor1)
    elif valor4 <= valor1 <= valor2 <= valor3:
        print(valor4, valor1, valor2, valor3)
    elif valor4 <= valor1 <= valor3 <= valor2:
        print(valor4, valor1, valor3, valor2)
    elif valor4 <= valor2 <= valor1 <= valor3:
        print(valor4, valor2, valor1, valor3)
    elif valor4 <= valor2 <= valor3 <= valor1:
        print(valor4, valor2, valor3, valor1)
    elif valor4 <= valor3 <= valor1 <= valor2:
        print(valor4, valor3, valor1, valor2)
    elif valor4 <= valor3 <= valor2 <= valor1:
        print(valor4, valor3, valor2, valor1)

    
    
# Conversões de temperatura

# 4.
# Faça uma função em Python que converta temperaturas de Celsius para Fahrenheit.
# A função deve solicitar o valor em Celsius (C).
# Fórmula:
# F = C / 1.8 + 32
# Menor temperatura possível em Celsius: -273.15

def c_to_f():

    graus_celsius=float(input("Temperatura em Graus Celsius"))

    graus_fahrenheit= graus_celsius *(9/5) + 32
    print( "A temperatura é de", graus_fahrenheit, "Graus Fahrenheit")

    if graus_celsius < -273.15:
        print("A menor temperatura possível é de 273.15 Graus Celsius")

# 5.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Celsius.
# A função deve solicitar o valor em Fahrenheit (F).
# Fórmula:
# C = 1.8 × (F − 32)
# Menor temperatura possível em Fahrenheit: -459.67

def f_to_c():
    graus_f= float(input("Temperatura em Fahrenheit"))
    if graus_f < -459.67:
        print("Erro, a menor temperatura em Fahrenheit é de -459.67")
    graus_c= 5/9 * (graus_f - 32)
    print("A temperatura é de", graus_c, "Graus Celsius")

    
# 6.
# Faça uma função em Python que converta temperaturas de Celsius para Kelvin.
# Fórmula:
# K = C + 273.15
# Menor temperatura possível em Celsius: -273.15

def c_to_k():
    graus_c=float(input("Temperatura em Graus Celsius"))
    if graus_c < 273.15:
        print("Erro, a menor temperatura possível em Graus Celsius é de -273.15")
    kelvin= graus_c + 273.15
    print("A temperatura em kelvin é de", kelvin)

# 7.
# Faça uma função em Python que converta temperaturas de Kelvin para Celsius.
# Fórmula:
# C = K − 273.15
# Menor temperatura possível em Kelvin: 0

def k_to_c():
    kelvin=float(input("Temperatura em Kelvin"))
    if kelvin < 0:
        print("Erro, a menor temperatura em Graus Kevin é 0")
    graus_c= kelvin - 273.15
    print("A temperatura em Graus Celsius é de", graus_c, "Graus Celsius")

# 8.
# Faça uma função em Python que converta temperaturas de Celsius para Rankine.
# Fórmula:
# R = (C + 491.67) × 1.8
# Menor temperatura possível em Celsius: -273.15

def c_to_r():
    graus_c=float(input("Temperatura em Graus Celsius"))
    if graus_c < -273.15:
        print("Erro, a menor temperatura em Graus Celsius é de -273.15")
    graus_r= (graus_c + 491.67) *1.8
    print("A temperatura em Graus Rankine é de",graus_r,"Graus Rankine")

# 9.
# Faça uma função em Python que converta temperaturas de Rankine para Celsius.
# Fórmula:
# C = (R / 1.8) − 491.67
# Menor temperatura possível em Rankine: 0

def r_to_c():
    graus_r=float(input("Temperatura em Graus Rankine"))
    if graus_r < 0:
        print("Erro, a menor temperatura em Graus Rankine é 0")
    graus_c= (graus_r/1.8) - 491.67
    print("A temperatura em Graus Celsius é de", graus_c)

# 10.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Kelvin.
# Menor temperatura possível em Fahrenheit: -459.67

def f_to_k():
    graus_f=float(input("Temperatura em Graus Fahrenheit"))
    if graus_f < -459.67:
        print("Erro, a menor temperatura em Graus Fahrenheit é de -459.67")
    kelvin= (graus_f -32) /1.8 + 273.15
    print("A temperatura em Graus Kelvin é de", kelvin)

# 11.
# Faça uma função em Python que converta temperaturas de Kelvin para Fahrenheit.
# Menor temperatura possível em Kelvin: 0

def k_to_f():
    kelvin=float(input("Temperatura em Kelvin"))
    if kelvin < 0:
        print("Erro, a menor temperatura em kelvin é 0")
    graus_f= (kelvin - 273.15) *1.8 + 32
    print("A temperatura em Graus Fahrenheit é de", graus_f)

# 12.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Rankine.
# Menor temperatura possível em Fahrenheit: -459.67

def f_to_r():
    graus_f=float(input("Temperatura em Graus Fahrenheit"))
    if graus_f < -459.67:
        print("Erro, a menor temperatura em Graus Fahrenheit é de -459.67")
    graus_r= graus_f + 459.67   
    print("A temperatura em Graus Rankine é de", graus_r)

# 13.
# Faça uma função em Python que converta temperaturas de Rankine para Fahrenheit.
# Menor temperatura possível em Rankine: 0

def r_to_f():
    graus_r=float(input("Temperatura em Graus Rankine"))
    if graus_r < 0:
        print("Erro, a menor temperatura em Graus Rankine é 0")
    graus_f= graus_r - 459.67
    print("A temperatura em Graus Fahrenheit é de", graus_f)

# 14.
# Faça uma função em Python que converta temperaturas de Kelvin para Rankine.
# Menor temperatura possível em Kelvin: 0

def k_to_r():
    kelvin=float(input("Temperatura em Kelvin"))
    if kelvin < 0:
        print("Erro, a menor temperatura em kelvin é 0")
    graus_r= kelvin * 1.8
    print("A temperatura em Graus Rankine é de", graus_r)

# 15.
# Faça uma função em Python que converta temperaturas de Rankine para Kelvin.
# Menor temperatura possível em Rankine: 0

def r_to_k():
    graus_r=float(input("Temperatura em Graus Rankine"))
    if graus_r < 0:
        print("Erro, a menor temperatura em Graus Rankine é 0")
    kelvin= graus_r/ 1.8
    print("A temperatura em Graus Kelvin é de", kelvin)

# Perímetros

# 16.
# Faça uma função em Python que calcule o perímetro de um triângulo.
# Entradas: lado A, lado B, lado C

def peri():
    print("Programa para calcular perímetro de triângulo")
    try:
        l1= float(input("Valor do lado 1: "))
    except ValueError:
        print("Insira um número válido")
    else:
        try:    
            l2= float(input("Valor do lado 2 "))
        except ValueError:
            print("Insira um número válido")
        else:
            try:
                l3= float(input("Valor do lado 3 "))
            except ValueError:
                print("Inaira um número válido")

    peri= l1 + l2 + l3

    print("O perímetro do triângulo é de", peri)

    print("Programa encerrado")



    

# 17.
# Faça uma função em Python que calcule o perímetro de um quadrado/losango.
# Entrada: lado L

# 18.
# Faça uma função em Python que calcule o perímetro de um retângulo/paralelogramo.
# Entradas: lado menor (m) e lado maior (M)

# 19.
# Faça uma função em Python que calcule o perímetro de um trapézio.
# Entradas: lado paralelo menor (m), lado paralelo maior (M) e outro lado (O)

# 20.
# Faça uma função em Python que calcule o perímetro de um polígono regular.
# Entradas: quantidade de lados (Q) e tamanho do lado

# 21.
# Faça uma função em Python que calcule o perímetro de um círculo.
# Entrada: raio (R)
# Fórmula: Perímetro = 2 × π × R
# π ≈ 3.1415

# Áreas

# 22.
# Área de um triângulo
# Entradas: base (B) e altura (A)
# Fórmula: Área = (B × A) / 2

# 23.
# Área de um quadrado
# Entrada: lado (L)
# Fórmula: Área = L²

# 24.
# Área de um retângulo
# Entradas: lado menor (m) e lado maior (M)
# Fórmula: Área = m × M

# 25.
# Área de um losango
# Entradas: diagonal menor (d) e diagonal maior (D)
# Fórmula: Área = (d × D) / 2

# 26.
# Área de um trapézio
# Entradas: base menor (b), base maior (B) e altura (A)
# Fórmula: Área = ((b + B) × A) / 2

# 27.
# Área de um polígono regular
# Entradas: número de lados (Q), base (B) e apótema (A)
# Fórmula: Área = (Q × B × A) / 2

# 28.
# Área de um círculo
# Entrada: raio (R)
# Fórmula: Área = π × R²

# Outros exercícios

# 29.
# Faça uma função que calcule o IMC (Índice de Massa Corporal).
# Entradas: peso (kg) e altura (m)
# Fórmula: IMC = peso / altura²

# 30.
# Faça uma função que resolva uma equação do 1º grau.
# Forma: AX + B = 0
# Entradas: A e B

# Programas com menu

# 31.
# Faça uma função com menu que reúna os exercícios 4 a 15 (conversões de temperatura).
def c_to_f():

    graus_celsius=float(input("Temperatura em Graus Celsius"))

    graus_fahrenheit= graus_celsius *(9/5) + 32
    print( "A temperatura é de", graus_fahrenheit, "Graus Fahrenheit")

    if graus_celsius < -273.15:
        print("A menor temperatura possível é de 273.15 Graus Celsius")

def f_to_c():
    graus_f= float(input("Temperatura em Fahrenheit"))

    graus_c= 5/9 * (graus_f - 32)
    print("A temperatura é de", graus_c, "Graus Celsius")

    if graus_f < -459.67:
        print("Erro, a menor temperatura em Fahrenheit é de -459.67")

def c_to_k():
    graus_c=float(input("Temperatura em Graus Celsius"))
    if graus_c < 273.15:
        print("Erro, a menor temperatura possível em Graus Celsius é de -273.15")
    kelvin= graus_c + 273.15
    print("A temperatura em kelvin é de", kelvin)

def k_to_c():
    kelvin=float(input("Temperatura em Kelvin"))
    if kelvin < 0:
        print("Erro, a menor temperatura em Graus Kevin é 0")
    graus_c= kelvin - 273.15
    print("A temperatura em Graus Celsius é de", graus_c, "Graus Celsius")


def c_to_r():
    graus_c=float(input("Temperatura em Graus Celsius"))
    if graus_c < -273.15:
        print("Erro, a menor temperatura em Graus Celsius é de -273.15")
    graus_r= (graus_c + 491.67) *1.8
    print("A temperatura em Graus Rankine é de",graus_r,"Graus Rankine")

def r_to_c():
    graus_r=float(input("Temperatura em Graus Rankine"))
    if graus_r < 0:
        print("Erro, a menor temperatura em Graus Rankine é 0")
    graus_c= (graus_r/1.8) - 491.67
    print("A temperatura em Graus Celsius é de", graus_c)

def f_to_k():
    graus_f=float(input("Temperatura em Graus Fahrenheit"))
    if graus_f < -459.67:
        print("Erro, a menor temperatura em Graus Fahrenheit é de -459.67")
    kelvin= (graus_f -32) /1.8 + 273.15
    print("A temperatura em Graus Kelvin é de", kelvin)

def k_to_f():
    kelvin=float(input("Temperatura em Kelvin"))
    if kelvin < 0:
        print("Erro, a menor temperatura em kelvin é 0")
    graus_f= (kelvin - 273.15) *1.8 + 32
    print("A temperatura em Graus Fahrenheit é de", graus_f)

def f_to_r():
    graus_f=float(input("Temperatura em Graus Fahrenheit"))
    if graus_f < -459.67:
        print("Erro, a menor temperatura em Graus Fahrenheit é de -459.67")
    graus_r= graus_f + 459.67   
    print("A temperatura em Graus Rankine é de", graus_r)

def r_to_f():
    graus_r=float(input("Temperatura em Graus Rankine"))
    if graus_r < 0:
        print("Erro, a menor temperatura em Graus Rankine é 0")
    graus_f= graus_r - 459.67
    print("A temperatura em Graus Fahrenheit é de", graus_f)

def k_to_r():
    kelvin=float(input("Temperatura em Kelvin"))
    if kelvin < 0:
        print("Erro, a menor temperatura em kelvin é 0")
    graus_r= kelvin * 1.8
    print("A temperatura em Graus Rankine é de", graus_r)

def r_to_k():
    graus_r=float(input("Temperatura em Graus Rankine"))
    if graus_r < 0:
        print("Erro, a menor temperatura em Graus Rankine é 0")
    kelvin= graus_r/ 1.8
    print("A temperatura em Graus Kelvin é de", kelvin)

def menu_conversao_temp():
    print("Menu de conversão")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Celsius para Rankine")
    print("6. Rankine para Celsius")
    print("7. Fahrenhieit para Kelvin")
    print("8. Kelvin para Fahrenheit")
    print("9. Fahrenheit para Rankine")
    print("10. Rankine para Fahrenheit")
    print("11. Kelvin para Rankine")
    print("12. Rankine para Kelvin")

    escolha = int(input("Escolha um número de 1 a 12"))

    try:
        if escolha== 1:
            c_to_f()
        elif escolha== 2:
            f_to_c()
        elif escolha == 3:
            c_to_k()
        elif escolha == 4:
            k_to_c()
        elif escolha == 5:
            c_to_r()
        elif escolha == 6:
            r_to_c()
        elif escolha == 7:
            f_to_k()
        elif escolha == 8:
            k_to_f()
        elif escolha == 9:
            f_to_r()
        elif escolha == 10:
            r_to_f()
        elif escolha == 11:
            k_to_r()
        elif escolha == 12:
            r_to_k() 
        else: 
            print("Opção inválida")
    except ValueError: 
        print("Erro, insira um número válido")




# 32.
# Faça uma função com menu que reúna os exercícios 16 a 21 (perímetros).

# 33.
# Faça uma função com menu que reúna os exercícios 22 a 28 (áreas).

# Validações

# 34.
# Crie uma função que receba horas, minutos e segundos
# e verifique se formam um horário válido.

def receberHMS():
    hora= int(input("Coloque aqui as horas "))
    min= int(input("Coloque aqui os minutos "))
    seg= int(input("Coloque aqui os segundos "))




#34.1
# Faça um programa em Python que solicite a digitação de três valores representando, 
# respectivamente, as horas, os minutos e os segundos de um horário, verificando, a seguir se os 
# mesmos representam ou não um horário válido. Sendo válido o programa deverá solicitar a 
# digitação de uma quantidade de segundos, calcular e mostrar na tela o horário que se obtem ao 
# adiantar o horário digitado a quantidade de segundo também digitada

def tempo():
    try:  
        hr= int(input("Coloque a hora: "))
    except ValueError:
        print("Erro, insira um horário válido")
    else:
        if hr <0 or hr >23:
            print("Hora somente entre 0 e 23")
        else:
            try:
                min= int(input("Coloque os minutos: "))
            except ValueError:
                print("Erro,digite um horário válido")
            else:
                if min <0 or min >59:
                    print("Número inválido, coloque um número entre 0 e 59")
                else:
                    try:
                        seg= int(input("Coloque os segundos "))
                    except ValueError:
                        print("Digite um horário válido!")
                    else:
                        if seg <0 or seg >59:
                            print("Coloque um número entre 0 e 59")
                        else:
                            try:
                                segadd= int(input("Digite os segundos a serem adicionados"))
                            except ValueError:
                                print("Número inválido!")
                            else:
                                hrSeg = hr * 3600
                                minSeg = min * 60
                                total = hrSeg + minSeg + seg + segadd

                                hrFinal = total//60
                                minFinal = total%60
                                print(hrFinal, minFinal)
                                
                            

tempo()


                    





# 35.
# Crie uma função que receba 3 segmentos de reta
# e verifique se podem formar um triângulo.

# 36.
# Se puder formar um triângulo, classifique:
# Equilátero (3 lados iguais)
# Isósceles (2 lados iguais)
# Escaleno (todos diferentes)

# 37.
# Verifique se 3 ângulos podem formar um triângulo.

# 38.
# Classifique o triângulo pelos ângulos:
# Acutângulo (todos < 90°)
# Retângulo (um = 90°)
# Obtusângulo (um > 90°)

# 39.
# Resolva uma equação do 2º grau:
# ax² + bx + c = 0
# Informar:
# nenhuma raiz
# uma raiz
# duas raízes

# 40.
# Crie uma função que verifique se uma data é válida.
# Entradas: dia, mês, ano
# Considerar meses de 30 e 31 dias, fevereiro e anos bissextos.

# 41.
# Receba um número até 9 e escreva por extenso.
# Exemplo: 5 → cinco

# 42.
# Receba um número até 99 e escreva por extenso.

# 43.
# Receba um número até 999 e escreva por extenso.

# 44.
# Faça uma função em Python que solicite a digitação de um número natural entre -9 e 9,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 45.
# Faça uma função em Python que solicite a digitação de um número natural entre -99 e 99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 46.
# Faça uma função em Python que solicite a digitação de um número natural entre -999 e 999,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 47.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -9,99 e R$ 9,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.

# 48.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -99,99 e R$ 99,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.

# 49.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -999,99 e R$ 999,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.