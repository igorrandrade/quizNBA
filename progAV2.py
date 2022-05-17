import random
def quiz():
  while True:
    cria_dicionario()
    global nome 
    global pontos
    nome = input('Digite seu nome: ')
    pontos = 0
    perg = 0
    for pg in perguntas:
      pg = random.choice(perguntas)
      print(pg["pergunta"])
      perg += 1
      respostas = pg["respostas"]
      for letra,resp in respostas.items():
        print(f'{letra}): {resp}')
          
      resp = input('\nDigite a letra da sua resposta: ')
      print()
      
      if resp in pg["resposta_correta"]:
        print('\n--- RESPOSTA CORRETA!!! ----\n')
        pontos += 1
      else:
          print('\n---- RESPOSTA INCORRETA----\n')
      x = random.randint(5,10)
      if perg == x:
        pontos = (pontos/perg)*100
        pontos = round(pontos,2)
        print(f'ACABOU A PARTIDA, VOCÊ ACERTOU:{pontos}%')
        print('\n---FIM DE JOGO---\n')
        registrar_ranking()
        break
        break
def registrar_ranking():     
  with open('ranking.txt','a') as arquivo:
    arquivo.write(f'{nome}#{pontos}\n')

def cria_dicionario():
  global perguntas
  perguntas = []
  arquivo = open("perguntas.txt","r")
  for linha in arquivo.readlines():
    coluna = linha.split("#")
    pergunta = {
          'pergunta': coluna[0],                      
'respostas':{'a':coluna[1],'b':coluna[2],'c':coluna[3],'d':coluna[4]},
    'resposta_correta': coluna[5].strip()}
    perguntas.append(pergunta)
  arquivo.close()
  return perguntas
def add_pergunta():
  
  arquivo = open("perguntas.txt","a")
  perg = input('Digite a pergunta: ')
  a = input('Digite a alternativa "a)": ')
  b = input('Digite a alternativa "b)": ')
  c = input('Digite a alternativa "c)": ')
  d = input('Digite a alternativa "d)": ')
  correct = input('Digite a letra da alternativa correta: ')
  arquivo.write(f'\n{perg}#{a}#{b}#{c}#{d}#{correct}')
  arquivo.close()
  
quiz()