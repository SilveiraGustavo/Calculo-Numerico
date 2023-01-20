# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 22:01:27 2022

@author: Gustavo
"""

""" 
Autor       : Gustavo Silveira Dias 
Instituição : Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais
Disciplina  : Cálculo Numérico
"""
import numpy as np 
# Biblioteca utilizada para realizar a plotagem do grafico da função
import matplotlib.pyplot as plt 

# DEFINIÇÃO DA FUNÇÃO QUE DESEJAMOS BUSCAR A RAIZ NO MÉTODO DA POSIÇÃO FALSA
def eval_PF(Fx,x):
    return eval(Fx)

# Método da posição falsa que recebe parametros que são respectivos da entrada do usuário
# RECEBE O INTERVALO [A,B] A FUNÇÃO, NÚMERO DE ITERAÇÕES E A TOLERANCIA 
def posicao_falsa(f,a,b,t,n):
    # INICIALMENTE NÃO POSSUI NENHUM X ANTERIOR
    xAnterior = float ('nan')
    fa = eval_PF(f, a)
    fb = eval_PF(f, b)
    # laço de repetição com as iterações
    for k in range (n):
        # REALIZA O CALCULO DO MÉTODO E ARMAZENA EM "x"
        x = (a *fb - b *fa)/ (fb - fa)
        fx = eval_PF(f,x)
        # CALCULA O SINAL 
        sinal = fa * fx
        # CALCULA O ERRO 
        error = abs ((x - xAnterior)  / max(x,1))
        # X ANTERIOR VAI PASSAR A SER "x"
        xAnterior = x
        
        # IMPRIME
        print("Iteração {k:3d}: a={a:+.5f}, ".format(k = k, a = a) +
              "b+{b:+.5f}, error={err:+.5f},".format(b = b, err = error) +
              "x={x:+.5f}, f(x)={fx:+.5f},  ".format(x = x, fx = fx) +
              "sinal = {s:+.5f}".format(x = x, fx = fx, s = sinal))
        # VERIFICA SE A FUNÇÃO É IGUAL A 0 
        # VERIFICA SE O VALOR DO CALCULO DO ERRO É MENOR QUE A TOLERANCIA 
        if (fx == 0) or (error < t):
            print('Raiz aproximaa encontrada {r:+5.5f}' .format( r =x))
            break
        # VERFICA SE O VALOR ARMAZENADO NO "sinal" É MAIOR QUE 0
        # CASO SEJA "a" RECEBE O "x"
        # E "fa" RECEBE "fx"
        if sinal > 0 :
            a = x
            fa = fx
        # CASO SEJA FALSO 
        # "b" RECEBE "x"
        # E "fb" REC
        else:
             b = x
             fb = fx

# DEFINIÇÃO DA FUNÇÃO QUE DESEJAMOS BUSCAR A RAIZ NO MÉTODO DA BISSEÇÃO
def eval_f(x):
    # ENTRA A FUNÇÃO DIGITADA E ARMAZENA NA VARIÁVEL G E RETORNA O G 
    # PARA SER USADO NA FUNÇÃO "bissecao"
    g = eval(f)
    return g
# MÉTODO DA BISSEÇÃO RECEBENDO PARAMETROS DE ENTRADA
# RECEBE O INTERVALO [A,B] O NÚMERO DE ITERAÇÕES E A TOLERANCIA 
def bissecao(a,b,t,n):
    # NÃO POSSUI NENHUM X ANTERIOR
    x_anterior = float('nan')
    # LAÇO DE REPETIÇÃO COM AS ITERAÇÕES
    for i in range(n):
        # SOMANDO O INTERVALO [A,B] E DIVIDINDO POR DOIS E ARMAZENA EM "g"
        g = (a + b) / 2
        fx = eval_f(g)
        
        # PEGA O VALOR DE "a" E MULTIPLICA POR "fx"
        sinal = eval_f(a) * fx
        # CALCULO DO ERRO 
        error = abs((g - x_anterior) / max(g,1))
        
        x_anterior = g
        
        # IMRPRIME 
        print('It. {i:3d}:'.format(i=i), 'a={a:+.6f},'.format(a=a),
             'b={b:+.6f},'.format(b=b), 'error={e:+.6f},'.format(e=error),
             'g={g:+.6f},'.format(g=g), 'f(g)={fx:+.6f},'.format(fx=fx),
             'sinal={s:+.6f}'.format(s=sinal))
        # VERIFICA SE A FUNÇÃO É IGUAL A 0 
        # VERIFICA SE O VALOR DO CALCULO DO ERRO É MENOR QUE A TOLERANCIA 
        if (fx == 0) or (error < t):
            print('Raiz aproximada encontrada: {r:+.6f}'.format( r = g))
            break
        # VERIFICANDO SE O O F(A) * fx É MAIOR QUE 0, CASO SEJA "a" RECEBE "g"
        if sinal > 0:
            a = g
        # CASO SEJA FALSO "b" RECEBE "g"
        else:
            b = g
        # VERIFICANDO SE MEU "i" É IGUAL A "n"
    if i == n:
        print('Raiz aproximada encontrada: {r:+.6f}'.format( r = g))

   
# DEFINIÇÃO DA FUNÇÃO QUE DESEJAMOS PLOTAR O GRAFICO               
def eval_Plot(fx,x):
    return eval(fx)

# FUNÇÃO RECEBE INTERVALOS [A,B] E UM "fx" PARA PLOTAR O GRAFICO 
def plot_graph(fx,a,b):
    xx = np.linspace(a,b)
    plt.plot(xx, eval_Plot(fx, xx))
    plt.grid()
    plt.show()

# FUNÇÃO MENU ONDE POSSUI TODAS AS INFORMAÇÕES E TODAS CHAMADA DE FUNÇÃO DOS MÉTODOS NUMERICOS
def menu():
    while True:
        print('___________________')
        print('    Menu Inicial   ')
        print('___________________')
        print('|1| Método da Falsa Posição.')
        print('|2| Método da Bisseção.')
        print('|3| Trocar Intervalo.')
        print('|4| Plotar Graficos da Função.')
        print('|5| Método da secante.')
        print('|6| Sair.')

        Resposta = int(input('Digite uma opção valída do menu.'))
        
        if Resposta == 1:
            # ENTRADA DE DADOS DA FUNÇÃO QUE VOCE DESEJA CALCULAR
            f = input('Digite a função.')
            t = 0.00001 
            n = 20
            a = float(input('Digite o primeiro intervalo.'))
            b = float(input('Digite o segundo intervalo. '))  
            print(posicao_falsa(f, a, b, t, n))
            
        elif Resposta == 2:
            # ENTRADA DE DADOS DA FUNÇÃO QUE VOCE DESEJA CALCULAR
            f = input('Digite a função.')
            t = 0.00001
            n = 20
            a = float(input('Digite o primeiro intervalo.'))
            b = float(input('Digite o segundo intervalo.'))
            print(bissecao(a, b, t, n))
            
        elif Resposta == 3:
            # ENTRADA DE DADOS DA FUNÇÃO QUE VOCE DESEJA CALCULAR
            f = input('Digite a função.')
            t = 0.00001
            n = 20
            a = float(input('Digite o primeiro intervalo.'))
            b = float(input('Digite o segundo intervalo.'))
            print(plot_graph(f, a, b))
            
            # SUB MENU PARA PODER ESCOLHER QUAL O MÉTODO QUE VOCE DESEJA 
            # RESOLVER COM OS NOVOS INTERVALOS
            print('|1| Método da Falsa Posição.')
            print('|2| Método da Bisseção.')
            print('|3| Método da secante.')
            resp = int(input('Informe o método de resolução que deseja usar:'))
            if resp == 1:
                print(bissecao(a, b, t, n))
            elif resp == 2:
                print(posicao_falsa(f, a, b, t, n))
            elif resp == 3:
                def F(x):
                    g = eval(f)
                    return g
                for i in range(n):
                    f_X1 = F(a)
                    f_x2 = F(b)

                    print(' It.'+ str(i) + " x:" + str(b) + " f(x): " + str(f_x2))

                    if abs(f_x2) < t:
                        break
                    x_3 = b - f_x2 * (( b - a) / (f_x2 - f_X1))
                    a = b
                    b = x_3
                    print('seu zero esta localizado em :' + str(b) + ',' + str(f_x2))
                
            # CASO ESCOLHA UMA OPÇÃO ERRADA ELE CHAMA A FUNÇÃO DO MENU NOVAMENTE 
            elif resp == 4:
                print('ERRO!!!\n')
                print('Informe uma opção que seja valída!')
            menu()
            
        elif Resposta == 4:
            f = input('Digite a função.')
            t = 0.00001
            n = 20
            a = float(input('Digite o primeiro intervalo.'))
            b = float(input('Digite o segundo intervalo.'))
            print(plot_graph(f, a, b))
        elif Resposta == 5:
           
                f = input('Informe a função:')
                t = 0.00001
                n = 20
                a = float(input("Intervalo:"))
                b = float(input('Intervalo B:'))

                def F(x):
                    g = eval(f)
                    return g
                for i in range(n):
                    f_X1 = F(a)
                    f_x2 = F(b)

                    print(' It.'+ str(i) + " x:" + str(b) + " f(x): " + str(f_x2))

                    if abs(f_x2) < t:
                        break
                    x_3 = b - f_x2 * (( b - a) / (f_x2 - f_X1))
                    a = b
                    b = x_3
                    print('seu zero esta localizado em :' + str(b) + ',' + str(f_x2))
        elif Resposta == 6:
            print('Até a proxima!')
            break
        else: 
            print('Informe uma opção que seja valída!')
            menu()

menu()