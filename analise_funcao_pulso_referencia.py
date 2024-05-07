# Projeto ATLAS - Reconstrução de sinal - Função pulso de referência.
# Autor: Guilherme Barroso Morett.
# Data: 07 de maio de 2024.

# Objetivo do código: Análise da função pulso de referência.

""" Organização do código:

Funções presentes:

1) Função para a leitura dos dados de pulso de referência.
Entrada: dados da função pulso de referêbcia no intervalo de tempo de [-75,5;124,5] ns.
Saída: matriz com os dados organizados (primeira coluna: tempo; segunda coluna: valores da função pulso de referência).
Obs.: essa matriz foi construída para a análise até o janelamento 19.

2) Função da análise da função pulso de referência de acordo com o janelamento.
Entrada: número de janelamento e a matriz dos dados dos pulsos de referência adaptada.
Saída: vetor do janelamento do tempo, vetor do janelamento do pulso de referencia, vetor do janelamento da derivada do pulso de referencia

3) Instrução para o plote do gráfico do pulso de referência ou sua derivada ao longo do tempo de acordo com o janelamento.
# Obs.: esse plote pode ser tanto da função pulsos de referência como da derivada primeira.
Entrada: tipo de gráfico ("A" ou "B"), vetor do tempo (ns) e vetor da função pulsos de referência ou a sua derivada.
Saída: nada.

4) Instrução principal para a análise da função pulso de referência.
Entrada: nada.
Saída: nada.

"""

# Importação de bibliotecas.
import numpy as np
import os
import matplotlib.pyplot as plt
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Análise da função pulso de referência:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ------------------------------ 1) FUNÇÃO PARA A LEITURA DOS DADOS DA FUNÇÃO PULSO DE REFERÊNCIA -------------------------------------------- ###

# Definição da função para a leitura dos dados da função pulso de referência.
def leitura_dados_pulso_referencia():
    
    # Nome da pasta em que se encontra o arquivo de entrada dos dados da função pulso de referência.
    pasta_dados_pulso_referencia = "Funcao_Pulso_Referencia"

    # Nome do arquivo de entrada dos dados da função pulso de referência.
    arquivo_dados_funcao_pulso_referencia = "funcao_pulso_referencia.txt"

    # O caminho para esse arquivo de entrada dos dados da função pulso de referência.
    caminho_arquivo_dados_pulso_referencia = os.path.join(pasta_dados_pulso_referencia, arquivo_dados_funcao_pulso_referencia)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_pulso_referencia):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_pulso_referencia,"r") as arquivo_entrada_pulso_referencia:
        
            # Armazena os dados na variável Matriz_dados_pulso_referencia.
            Matriz_dados_pulso_referencia = np.array(np.loadtxt(arquivo_entrada_pulso_referencia, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_funcao_pulso_referencia} não existe na pasta {pasta_dados_pulso_referencia}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar em uma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # Criação do vetor extendido do tempo A.
    vetor_extendido_tempo_A = np.arange(-226, -75.5, 0.5)
    
    # A variável tamanho_vetor_extendido_tempo_A recebe a quantidade de elementos presentes no vetor_extendido_tempo_A.
    tamanho_vetor_extendido_tempo_A = len(vetor_extendido_tempo_A)
    
    # Criação do vetor extendido dos pulsos de referência do tempo A.
    vetor_extendido_pulsos_A = np.zeros(tamanho_vetor_extendido_tempo_A)
    
    # Os dois vetores são concatenados como colunas para formar a Matriz_extendida_A.
    Matriz_extendida_A = np.column_stack((vetor_extendido_tempo_A, vetor_extendido_pulsos_A))
    
    # Criação do vetor extendido do tempo B.
    vetor_extendido_tempo_B = np.arange(125.0, 226.5, 0.5)
    
    # A variável tamanho_vetor_extendido_B recebe a quantidade de elementos presentes no vetor_extendido_tempo_B.
    tamanho_vetor_extendido_pulsos_B = len(vetor_extendido_tempo_B)
    
    # Criação do vetor extendido dos pulsos de referência do tempo B.
    vetor_extendido_pulsos_B = np.zeros(tamanho_vetor_extendido_pulsos_B)
    
    # Os dois vetores são concatenados como colunas para formar a Matriz_extendida_B.
    Matriz_extendida_B = np.column_stack((vetor_extendido_tempo_B, vetor_extendido_pulsos_B))
    
    # AS três matrizes são concatenadas de maneira vertical para formar uma única adaptada para a análise até o janelamento 19.
    Matriz_dados_pulso_referencia_adaptada = np.concatenate((Matriz_extendida_A, Matriz_dados_pulso_referencia, Matriz_extendida_B), axis = 0)
    
    # A função retorna a matriz Matriz_dados_pulso_referencia_adaptada.
    return Matriz_dados_pulso_referencia_adaptada

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------- 2) FUNÇÃO DA ANÁLISE DA FUNÇÃO PULSO DE REFERÊNCIA DE ACORDO COM O JANELAMENTO ------------------------------------- ###
# Definição da função para exibição do intervalo da função de referência de acordo com o janelamento.
def funcao_referencia(n_janelamento, Matriz_dados_pulso_referencia_adaptada):
    
    # Criação da lista inicialmente vazia lista_janelamento_tempo.
    lista_janelamento_tempo = []
    
    # Criação da lista inicialmente vazia lista_janelamento_pulso_referencia.
    lista_janelamento_pulso_referencia = []
    
    # Criação da lista incialmente vazia lista_janelamento_derivada_pulso_referencia.
    lista_janelamento_derivada_pulso_referencia = []
    
    # caso n_janelamento seja igual a 7.
    if n_janelamento == 7:
    
        # A variável indice_inicial_janelamento recebe o índice referente ao tempo -75.0 ns.
        indice_inicial_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == -75.0)[0][0]
    
        # A variável indice_final_janelamento recebe o índice referente ao tempo 75.0 ns.
        indice_final_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == 75.0)[0][0]
        
    # Caso n_janelamento seja igual a 9.
    elif n_janelamento == 9:
        
        # A variável indice_inicial_janelamento recebe o índice referente ao tempo -100.0 ns.
        indice_inicial_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == -100.0)[0][0]
    
        # A variável indice_final_janelamento recebe o índice referente ao tempo 100.0 ns.
        indice_final_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == 100.0)[0][0]
        
    # Caso n_janelamento seja igual a 11.
    elif n_janelamento == 11:
        
        # A variável indice_inicial_janelamento recebe o índice referente ao tempo -100.0 ns.
        indice_inicial_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == -125.0)[0][0]
    
        # A variável indice_final_janelamento recebe o índice referente ao tempo 100.0 ns.
        indice_final_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == 125.0)[0][0]
        
    # Caso n_janelamento seja igual a 13.
    elif n_janelamento == 13:
        
        # A variável indice_inicial_janelamento recebe o índice referente ao tempo -150.0 ns.
        indice_inicial_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == -150.0)[0][0]
    
        # A variável indice_final_janelamento recebe o índice referente ao tempo 150.0 ns.
        indice_final_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == 150.0)[0][0]
        
    # Caso n_janelamento seja igual a 15.
    elif n_janelamento == 15:
        
        # A variável indice_inicial_janelamento recebe o índice referente ao tempo -175.0 ns.
        indice_inicial_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == -175.0)[0][0]
    
        # A variável indice_final_janelamento recebe o índice referente ao tempo 175.0 ns.
        indice_final_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == 175.0)[0][0]
        
    # Caso n_janelamento seja igual a 17.
    elif n_janelamento == 17:
    
        # A variável indice_inicial_janelamento recebe o índice referente ao tempo -200.0 ns.
        indice_inicial_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == -200.0)[0][0]
    
        # A variável indice_final_janelamento recebe o índice referente ao tempo 200.0 ns.
        indice_final_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == 200.0)[0][0]
        
    # Caso n_janelamento seja igual a 19.
    elif n_janelamento == 19:
        
        # A variável indice_inicial_janelamento recebe o índice referente ao tempo -225.0 ns.
        indice_inicial_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == -225.0)[0][0]
    
        # A variável indice_final_janelamento recebe o índice referente ao tempo 225.0 ns.
        indice_final_janelamento = np.argwhere(Matriz_dados_pulso_referencia_adaptada[:, 0] == 225.0)[0][0]
          
    # A variável incremento_janelamento aramzena a quantiade de incremento para o janelamento.
    incremento_janelamento = 50
    
    # Impressão de mensagem no terminal.
    print("\n-------------------------- Função pulso de referência normalizado -------------------------------------")
    
    # Para o indíce de janelamento com seu valor inicial até o final com o incremento.
    for indice_linha in range(indice_inicial_janelamento, indice_final_janelamento+1, incremento_janelamento):
        
        # A variável valor_tempo aramzena o valor do tempo presente na matriz. 
        valor_tempo = Matriz_dados_pulso_referencia_adaptada[indice_linha, 0]
        
        # A variável valor_pulso armazena o valor de pulso presente na matriz.
        valor_pulso = Matriz_dados_pulso_referencia_adaptada[indice_linha, 1]
        
        # Impressão no terminal dos valores para a função de referência normalizada no intervalo de tempo de acordo com o janelamento.
        print(f"Tempo: {valor_tempo} ns.\nFunção pulso de referência normalizado: {valor_pulso}.")
    
        # A lista lista_janelamento_tempo recebe o valor valor_tempo.
        lista_janelamento_tempo.append(valor_tempo)
        
        # A lista_janelamento_pulso_referencia recebe o valor valor_pulso.
        lista_janelamento_pulso_referencia.append(valor_pulso)
    
    # Impressão de mensagem no terminal.
    print("---------------------------------------------------------------------------------------------------------------------")    
        
    # Impressão de mensagem no terminal.
    print("\n---------------------- Derivada da função pulso de referência normalizado ------------------------------")
        
    # Definição do passo h apra a derivada numérica.
    h = 0.5
        
    # Para o indíce de janelamento com seu valor inicial até o final com o incremento.
    for indice_linha in range(indice_inicial_janelamento, indice_final_janelamento+1, incremento_janelamento):
        
        # A variável valor_tempo aramzena o valor do tempo presente na matriz. 
        valor_tempo = Matriz_dados_pulso_referencia_adaptada[indice_linha, 0]
        
        # A variável valor_pulso_central armazena o valor de pulso central presente na matriz.
        valor_pulso_central = Matriz_dados_pulso_referencia_adaptada[indice_linha, 1]
        
        # A variável valor_pulso_central_menos_dois armazena o valor referente ao pulso central deslocado 1 ns para trás.
        valor_pulso_central_menos_dois = Matriz_dados_pulso_referencia_adaptada[indice_linha-2, 1]
        
        # A variável valor_pulso_central_menos_um armazena o valor referente ao pulso central deslocado 0.5 ns para trás.
        valor_pulso_central_menos_um = Matriz_dados_pulso_referencia_adaptada[indice_linha-1, 1]
        
        # A variável valor_pulso_central_mais_um armazena o valor referente ao pulso central deslocado 0.5 ns para frente.
        valor_pulso_central_mais_um = Matriz_dados_pulso_referencia_adaptada[indice_linha+1, 1]
        
        # A variável valor_pulso_central_mais_dois armazena o valor referente ao pulso central deslocado 1 ns para frente.
        valor_pulso_central_mais_dois = Matriz_dados_pulso_referencia_adaptada[indice_linha+2, 1]
        
        # Cálculo da derivada numérica pela diferença central com quatro pontos.
        # Obs.: o erro de truncamento é de quarta ordem para esse método numérico.
        valor_derivada_funcao_pulso_referencia = (valor_pulso_central_menos_dois-8*valor_pulso_central_menos_um+8*valor_pulso_central_mais_um-valor_pulso_central_mais_dois)/(12*h)
        
        # Impressão no terminal dos valores para a derivada da função pulso de referência normalizada no intervalo de tempo de acordo com o janelamento.
        print(f"Tempo: {valor_tempo} ns.\nFunção pulso de referência normalizado: {valor_derivada_funcao_pulso_referencia}.")
        
        
        # A lista lista_janelamento_derivada_pulso_referencia recebe o valor da derivada_funcao_pulso_referencia.
        lista_janelamento_derivada_pulso_referencia.append(valor_derivada_funcao_pulso_referencia)
        
    # Impressão de mensagem no terminal.
    print("--------------------------------------------------------------------------------------------------------------------------")
    
    # Conversão da lista lista_janelamento_tempo para numpy array.
    vetor_janelamento_tempo = np.array(lista_janelamento_tempo)
    
    # Conversão da lista lista_janelamento_pulso_referencia para numpy array.
    vetor_janelamento_pulso_referencia = np.array(lista_janelamento_pulso_referencia)
    
    # Conversão da lsita lista_janelamento_derivada_pulso_referencia para numpy array.
    vetor_janelamento_derivada_pulso_referencia = np.array(lista_janelamento_derivada_pulso_referencia)
    
    # A funçaõ retorna os vetores vetor_janelamento_tempo e vetor_janelamento_pulso_referencia.
    return vetor_janelamento_tempo, vetor_janelamento_pulso_referencia, vetor_janelamento_derivada_pulso_referencia
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------- 3) Instrução para o plote do gráfico do pulso de referência ou sua derivada ao longo do tempo de acordo com o janelamento ---------- ###

# Definição da função para o plote do gráfico.
def grafico_funcao_pulso_referencia(tipo_grafico, vetor_janelamento_tempo, vetor_janelamento_pulsos_referencia):
    
    # Definição dos elementos do eixo x.
    eixo_x = vetor_janelamento_tempo
    
    # Tamanho dos números presentes no eixo x.
    plt.xticks(fontsize = 16)
    
    # Nomeação do eixo x.
    plt.xlabel("Tempo (ns)", fontsize = 18)
    
    # Definição dos vetores do eixo y.
    eixo_y = vetor_janelamento_pulsos_referencia
    
    # Tamanho dos números presentes no eixo y.
    plt.yticks(fontsize = 16)
    
    # Caso tipo_grafico for "A".
    if tipo_grafico == "A":
    
        # nomeação do eixo y.
        plt.ylabel("Função pulso de referência normalizada", fontsize = 18)
        
    # Caso tipo_grafico for "B".
    elif tipo_grafico == "B":
        
        # nomeação do eixo y.
        plt.ylabel("Derivada da função pulso de referência normalizada", fontsize = 18)
    
    # Comando para o plote do gráfico.
    plt.plot(eixo_x, eixo_y, linestyle = '--', marker = "o")
    
    # Comando para acrescentar o grid no gráfico.
    plt.grid()
    
    # Comando para mostrar o gráfico.
    plt.show()

# -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------- 4) INSTRUÇÃO PRINCIPAL PARA A ANÁLISE DA FUNÇÃO PULSO DE REFERÊNCIA ---------------------------------------------- ###

# Definção da instrução principal para o código.
def principal_funcao_pulso_referencia():
    
    # Impressão de mensagem no terminal.
    print("\nTipos de gráficos:\nTempo versus a função pulso de referência: A\nTempo versus a derivada numérica da função pulso de referência: B")
    
    # A variável tipo_grafico armazena a string digitada pelo usuário via terminal.
    tipo_grafico = str(input("Digite o tipo de gráfico desejado: "))
    
    tipo_grafico = tipo_grafico.upper()
    
    # Se a variável tipo_grafico for diferente de 'A' ou 'B'.
    if tipo_grafico != "A" and tipo_grafico != "B":
        
        # Exibição de uma mensagem de alerta de que o tipo de gráfico solicitado é inválido.
        print("Por favor digite uma tipo válido de gráfico: A ou B!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de dois.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)

    # Chamada ordenada das funções e instruções.
    Matriz_dados_pulso_referencia_adaptada = leitura_dados_pulso_referencia()
    vetor_janelamento_tempo, vetor_janelamento_pulso_referencia, vetor_janelamento_derivada_pulso_referencia = funcao_referencia(n_janelamento, Matriz_dados_pulso_referencia_adaptada)
    
    # Caso tipo_grafico seja 'A'.
    if tipo_grafico == "A":
    
        # Chamada da função com os dados a função pulso de referência.
        grafico_funcao_pulso_referencia(tipo_grafico, vetor_janelamento_tempo, vetor_janelamento_pulso_referencia)
        
    # Caso tipo_grafico seja 'B'.
    elif tipo_grafico == "B":
        
        # Chamada da função com os dados da derivada da função pulso de referência.
        grafico_funcao_pulso_referencia(tipo_grafico, vetor_janelamento_tempo, vetor_janelamento_derivada_pulso_referencia)
    
# Chamada da instrução principal.
principal_funcao_pulso_referencia()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")   

    