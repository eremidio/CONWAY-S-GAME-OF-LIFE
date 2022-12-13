#Vamos escrever um programa para escrever o jogo da vida usando Python3

#*****************************************************************************************************************************
#
#
#
#0: Importando as bibliotecas usadas
import time
import random

#*****************************************************************************************************************************
#
#
#
#1:Cabeçalho e instruções do jogo

#Boas vindas ao jogador
print(' ***   *         *      *  *  *')
print('*   *  *        * *     *  *  *')
print('*   *  *       *****    *  *  *')
print('*   *  *      *     *          ')
print(' ***   ****  *       *  *  *  *')
print('')
print('')
print('Seja bem vindo ao jogo da vida!!!!\n')
print("Este programa é uma adaptação de Conway's Game Of Life feito em Python.\n\n")

stop=input('\n')

#Explicação do jogo
print('O jogo da vida é um exemplo de automaton celular.\nUm automaton celular consiste em dois conjuntos distintos.\nTemos uma malha que é um conjunto de células e um conjunto de regras (funções) que determinam a evolução do sistema.\n')

stop=input('\n')

print('Cada célula pode ser pensada como uma entidade matemática que é caracterizada por um conjunto de variáveis.\nOs valores destas variáveis determinam o estado de cada célula individualmente.\n')

stop=input('\n')

print('As funções determinam a evolução do sistema como um todo, alterando o estado de todas as células simultaneamente.\nEstas funções podem ter um caráter determinístico ou probabilístico.\n\n')

#Instruções do jogo

stop=input('\n')

print('No jogo da vida proposto pelo matemático inglês John Horton Conway cada celula é caracterizada por duas variáveis.\nUma variável de estado (booleana) que pode assumir os valores "vivo" (verdadeiro) ou "morto" (falso).\nUma variável númerica que indica o número de células vizinhas que estão "vivas".\n')

stop=input('\n')

print('Eis as regras do jogo:\n1.Uma célula ativada (viva) permance nesta condição se e somente se houver 2 ou 3 células vivas adjacentes.\nCaso este número seja inferior a 2 ou superior a 3 a célula morre.\n2.Uma célula desativada (morta) só se ativa quando o número de células ativadas adjacentes for igual a 3.\n\n')

stop=input('\n')

#*****************************************************************************************************************************
#
#
#
#2: Criando a malha quadrada e o tabuleiro

print('O jogo da vida será jogado num tabuleiro 15x15 que será mostrado abaixo.\nEste sistema de coordenadas deverá ser usado para ajustar a configuração inicial do tabuleiro manualmente.\n')
#Imprimindo a malha quadrada (tabuleiro)
for i in range(15):
 print('+---'*15+'+')
 print('|   '*15+'| {}'.format(14-i))
print('+---'*15+'+')
print('  0   1   2   3   4   5   6   7   8   9  10  11  12   13  14')

#Vamos criar o tabuleiro como um array 2D 15x15
tabuleiro:list=[[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],]


#Vamos criar um segundo tabuleiro como um array 2D 15x15
#Este será usado como uma variável intermediária ao se atualizar o estado do sistema durante as iterações
tabuleiro2:list=[[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],]


#Função que define a posição do tabuleiro do jogo da vida
def posicao(tabuleiro:list)->list:
 '''Função que define a posição do tabuleiro do jogo da vida'''
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 14'.format(tabuleiro[0][14], tabuleiro[1][14],tabuleiro[2][14],tabuleiro[3][14], tabuleiro[4][14],tabuleiro[5][14],tabuleiro[6][14], tabuleiro[7][14],tabuleiro[8][14],tabuleiro[9][14], tabuleiro[10][14],tabuleiro[11][14],tabuleiro[12][14], tabuleiro[13][14],tabuleiro[14][14]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 13'.format(tabuleiro[0][13], tabuleiro[1][13],tabuleiro[2][13],tabuleiro[3][13], tabuleiro[4][13],tabuleiro[5][13],tabuleiro[6][13], tabuleiro[7][13],tabuleiro[8][13],tabuleiro[9][13], tabuleiro[10][13],tabuleiro[11][13],tabuleiro[12][13], tabuleiro[13][13],tabuleiro[14][13]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 12'.format(tabuleiro[0][12], tabuleiro[1][12],tabuleiro[2][12],tabuleiro[3][12], tabuleiro[4][12],tabuleiro[5][12],tabuleiro[6][12], tabuleiro[7][12],tabuleiro[8][12],tabuleiro[9][12], tabuleiro[10][12],tabuleiro[11][12],tabuleiro[12][12], tabuleiro[13][12],tabuleiro[14][12]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 11'.format(tabuleiro[0][11], tabuleiro[1][11],tabuleiro[2][11],tabuleiro[3][11], tabuleiro[4][11],tabuleiro[5][11],tabuleiro[6][11], tabuleiro[7][11],tabuleiro[8][11],tabuleiro[9][11], tabuleiro[10][11],tabuleiro[11][11],tabuleiro[12][11], tabuleiro[13][11],tabuleiro[14][11]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 10'.format(tabuleiro[0][10], tabuleiro[1][10],tabuleiro[2][10],tabuleiro[3][10], tabuleiro[4][10],tabuleiro[5][10],tabuleiro[6][10], tabuleiro[7][10],tabuleiro[8][10],tabuleiro[9][10], tabuleiro[10][10],tabuleiro[11][10],tabuleiro[12][10], tabuleiro[13][10],tabuleiro[14][10]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 9'.format(tabuleiro[0][9], tabuleiro[1][9],tabuleiro[2][9],tabuleiro[3][9], tabuleiro[4][9],tabuleiro[5][9],tabuleiro[6][9], tabuleiro[7][9],tabuleiro[8][9],tabuleiro[9][9], tabuleiro[10][9],tabuleiro[11][9],tabuleiro[12][9], tabuleiro[13][9],tabuleiro[14][9]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 8'.format(tabuleiro[0][8], tabuleiro[1][8],tabuleiro[2][8],tabuleiro[3][8], tabuleiro[4][8],tabuleiro[5][8],tabuleiro[6][8], tabuleiro[7][8],tabuleiro[8][8],tabuleiro[9][8], tabuleiro[10][8],tabuleiro[11][8],tabuleiro[12][8], tabuleiro[13][8],tabuleiro[14][8]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+ eixo y')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 7'.format(tabuleiro[0][7], tabuleiro[1][7],tabuleiro[2][7],tabuleiro[3][7], tabuleiro[4][7],tabuleiro[5][7],tabuleiro[6][7], tabuleiro[7][7],tabuleiro[8][7],tabuleiro[9][7], tabuleiro[10][7],tabuleiro[11][7],tabuleiro[12][7], tabuleiro[13][7],tabuleiro[14][7]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 6'.format(tabuleiro[0][6], tabuleiro[1][6],tabuleiro[2][6],tabuleiro[3][6], tabuleiro[4][6],tabuleiro[5][6],tabuleiro[6][6], tabuleiro[7][6],tabuleiro[8][6],tabuleiro[9][6], tabuleiro[10][6],tabuleiro[11][6],tabuleiro[12][6], tabuleiro[13][6],tabuleiro[14][6]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 5'.format(tabuleiro[0][5], tabuleiro[1][5],tabuleiro[2][5],tabuleiro[3][5], tabuleiro[4][5],tabuleiro[5][5],tabuleiro[6][5], tabuleiro[7][5],tabuleiro[8][5],tabuleiro[9][5], tabuleiro[10][5],tabuleiro[11][5],tabuleiro[12][5], tabuleiro[13][5],tabuleiro[14][5]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 4'.format(tabuleiro[0][4], tabuleiro[1][4],tabuleiro[2][4],tabuleiro[3][4], tabuleiro[4][4],tabuleiro[5][4],tabuleiro[6][4], tabuleiro[7][4],tabuleiro[8][4],tabuleiro[9][4], tabuleiro[10][4],tabuleiro[11][4],tabuleiro[12][4], tabuleiro[13][4],tabuleiro[14][4]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 3'.format(tabuleiro[0][3], tabuleiro[1][3],tabuleiro[2][3],tabuleiro[3][3], tabuleiro[4][3],tabuleiro[5][3],tabuleiro[6][3], tabuleiro[7][3],tabuleiro[8][3],tabuleiro[9][3], tabuleiro[10][3],tabuleiro[11][3],tabuleiro[12][3], tabuleiro[13][3],tabuleiro[14][3]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 2'.format(tabuleiro[0][2], tabuleiro[1][2],tabuleiro[2][2],tabuleiro[3][2], tabuleiro[4][2],tabuleiro[5][2],tabuleiro[6][2], tabuleiro[7][2],tabuleiro[8][2],tabuleiro[9][2], tabuleiro[10][2],tabuleiro[11][2],tabuleiro[12][2], tabuleiro[13][2],tabuleiro[14][2]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 1'.format(tabuleiro[0][1], tabuleiro[1][1],tabuleiro[2][1],tabuleiro[3][1], tabuleiro[4][1],tabuleiro[5][1],tabuleiro[6][1], tabuleiro[7][1],tabuleiro[8][1],tabuleiro[9][1], tabuleiro[10][1],tabuleiro[11][1],tabuleiro[12][1], tabuleiro[13][1],tabuleiro[14][1]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 0'.format(tabuleiro[0][0], tabuleiro[1][0],tabuleiro[2][0],tabuleiro[3][0], tabuleiro[4][0],tabuleiro[5][0],tabuleiro[6][0], tabuleiro[7][0],tabuleiro[8][0],tabuleiro[9][0], tabuleiro[10][0],tabuleiro[11][0],tabuleiro[12][0], tabuleiro[13][0],tabuleiro[14][0]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('  0   1   2   3   4   5   6   7   8   9  10  11  12   13  14')
 print('                     eixo x                        ')

'''Módulo de teste da função tabuleiro, use um # após os testes'''
#tabuleiro[0][0]='a'
#tabuleiro[0][14]='b'
#tabuleiro[14][0]='c'
#tabuleiro[14][14]='d'
#posicao(tabuleiro)

#*****************************************************************************************************************************
#
#
#
#3:Definindo a configuração inicial do tabuleiro e o modo de jogo

#Variável que define se a configuração incial do tabuleiro será definida manualmente ou não
modo:str=str(input('Digite "auto" para definir a configuração inicial do tabuleiro automaticamente \nou "manual" para definí-la manualmente:'))

print('\n')

#Variável que define o símbolo usado para indicar que uma célula está ocupada(viva)
marcador:str=str(input('Digite a primeira letra do seu nome:'))

print('\n')

#Variável que define o número de casas iniciais ocupadas (vivas) no tabuleiro
n_inicial:int=int(input('Digite quantas células "vivas" (casas ocupadas) você deseja na configuração inicial do tabuleiro:'))

print('\n')

#Funções que ajustam a configuração inicial do tabuleiro manualmente ou automaticamente
def setup_auto(tabuleiro:list, n_inicial:int, marcador:str)->list:
 '''Função que define automaticamente a configuração inicial do tabuleiro'''
 contador:int=0
 while(contador<n_inicial):
  x1:int=random.randint(0,14)
  y1:int=random.randint(0,14)
  if(tabuleiro[x1][y1]==' '):
   tabuleiro[x1][y1]=marcador
   contador=contador+1
  else:
   continue
 return tabuleiro

def setup_manual(tabuleiro:list, n_inicial:int, marcador:str)->list:
 '''Função que define automaticamente a configuração inicial do tabuleiro'''
 contador:int=0
 while(contador<n_inicial):
  x2:int=int(input('Digite a primeira coordenada (eixo x) da célula que você deseja ativar:'))
  y2:int=int(input('Digite a segunda coordenada (eixo y) da célula que você deseja ativar:'))
  if(tabuleiro[x2][y2]==' '):
   tabuleiro[x2][y2]=marcador
   contador=contador+1
   print(f'Célula nº{contador} ativada.\n')
  else:
   print('Esta célula já se encontra ativada.\n')
   continue
 return tabuleiro

#Ajustando a configuração inicial do tabuleiro
if (modo=='manual'):
 setup_manual(tabuleiro, n_inicial, marcador)
if (modo=='auto'):
 setup_auto(tabuleiro, n_inicial, marcador)

#Exibindo o tabuleiro na sua configuração inicial
posicao(tabuleiro)


stop=input('\n')

#*****************************************************************************************************************************
#
#
#
#4:Funções que atualizam o status do tabuleiro

#Função de contagem que contá o número de células vivas no enrtorno de uma  célula específica
def contagem(tabuleiro:list, a:int, b:int, simbolo:str):
 '''Função que contabiliza o número de células vivas ao redor de uma determinada célula'''
 contador:int=0
 if(a>=0 and b>=0 and a<14 and b<14):
  #Horizontal
  if(a+1>=0 and a+1<14 and tabuleiro[a+1][b]==simbolo):
   contador=contador+1
  if(a-1>=0 and a-1<14 and tabuleiro[a-1][b]==simbolo):
   contador=contador+1
  #Vertical
  if(b+1>=0 and b+1<14 and tabuleiro[a][b+1]==simbolo):
   contador=contador+1
  if(b-1>=0 and b-1<14 and tabuleiro[a][b-1]==simbolo):
   contador=contador+1
  #Diagonal
  if(a+1>=0 and a+1<14 and b+1>=0 and b+1<14 and tabuleiro[a+1][b+1]==simbolo):
   contador=contador+1
  if(a+1>=0 and a+1<14 and b-1>=0 and b-1<14 and tabuleiro[a+1][b-1]==simbolo):
   contador=contador+1
  if(a-1>=0 and a-1<14 and b+1>=0 and b+1<14 and tabuleiro[a-1][b+1]==simbolo):
   contador=contador+1
  if(a-1>=0 and a-1<14 and b-1>=0 and b-1<14 and tabuleiro[a-1][b-1]==simbolo):
   contador=contador+1
 return contador

'''Módulo de teste da função de contagem, use um # após o teste'''
#print(contagem(tabuleiro, 5, 5, marcador))

#Funções que atualizam o status de um célula do tabuleiro
def celula_viva(tabuleiro:list, a:int, b:int, simbolo:str)->bool:
 '''Função que define o status (ação que ocorrerá na próxima iteração) de uma célula ativada'''
 if(tabuleiro[a][b]==simbolo):
  if(contagem(tabuleiro, a, b, simbolo)==2 or contagem(tabuleiro, a, b, simbolo)==3):
   return True
  elif(contagem(tabuleiro, a, b, simbolo)!=2 or contagem(tabuleiro, a, b, simbolo)!=3):
   return False

def celula_morta(tabuleiro:list, a:int, b:int, simbolo:str)->bool:
 '''Função que define o status (ação que ocorrerá na próxima iteração) de uma célula ativada'''
 if(tabuleiro[a][b]==' '):
  if(contagem(tabuleiro, a, b, simbolo)==3):
   return True
  elif(contagem(tabuleiro, a, b, simbolo)!=3):
   return False


#*****************************************************************************************************************************
#
#
#
#5:Executando o jogo

#Variável que define o número de iterações a serem executadas no jogo e variável de controle do loop principal
iteracoes:int=int(input('Digite quantas iterações você deseja realizar:'))
execucoes:int=0

print('\n')
print('\n')

#Atualizando o tabuleiro
while(execucoes<iteracoes):
 #Atualizando o status da variável que determina a execução do loop principal
 execucoes=execucoes+1
 #Atualizando o tabuleiro2 (variável intermediária)
 for i in range(15):
  for j in range(15):
   if(tabuleiro[i][j]==marcador and celula_viva(tabuleiro, i, j, marcador)==True):
    tabuleiro2[i][j]= marcador
   if(tabuleiro[i][j]==marcador and celula_viva(tabuleiro, i, j, marcador)==False):
    tabuleiro2[i][j]= ' '
   if(tabuleiro[i][j]==' ' and celula_morta(tabuleiro, i, j, marcador)==True):
    tabuleiro2[i][j]= marcador
   if(tabuleiro[i][j]==' ' and celula_morta(tabuleiro, i, j, marcador)==False):
    tabuleiro2[i][j]= ' '

 #Atualizando o tabuleiro principal do jogo
 tabuleiro2=tabuleiro2
 tabuleiro=tabuleiro2
 #Atualizando o tabuleiro secundário do jogo
 tabuleiro2:list=[[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],]
 #Exibindo tabuleiro
 time.sleep(0.4)
 posicao(tabuleiro)
 print('\n')
 print('\n')




#*****************************************************************************************************************************
#
#
#
#6: Encerramento
print(' ')
print(' ')
print('\033[94m'+'\033[01m'+'Esperamos que tenha se divertido!!!')
print(' ')
print(' ')
print('\033[94m'+'\033[01m'+' ***   ****   ****    *   ***       *      ****    ***     *  *  *')
print('\033[94m'+'\033[01m'+'*   *  *   *  *   *   *  *   *     * *     *   *  *   *    *  *  *')
print('\033[94m'+'\033[01m'+'*   *  ****   ****    *  *        *****    *   *  *   *    *  *  *')
print('\033[94m'+'\033[01m'+'*   *  *   *  *   *   *  * ***   *     *   *   *  *   *           ')
print('\033[94m'+'\033[01m'+' ***   ****   *    *  *   ***   *       *  ****    ***     *  *  *')
