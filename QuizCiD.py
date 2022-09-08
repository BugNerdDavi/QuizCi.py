from os import system
from time import sleep
system('cls')
print('-' * 30)
print('')
respInicial = str(input('Pressione enter para começar: '))
print('')
print('-' * 30)
while True:
  system('cls')
  print('-' * 30)
  print('')
  print('[1]-Fácil')
  print('[2]-Médio')
  print('[3]-Dificil')
  print('[4]-EINSTEIN INSANO')
  print('')
  print('-' * 30)
  respi2 = int(input('Escolha:'))
  if respi2 == 1:
      while True:
          system('cls')
          pontos = 0
          print('-' * 42)
          print('')
          print('Quiz: Ciências (nível: Fácil).')
          print('')
          print('Notas: 0 a 10')
          print('')
          print('-' * 42)
          sleep(5)
          system('cls')
          print('-' * 30)
          print('')
          print('           Iniciando')
          print('')
          print('-' * 30)
          sleep(3)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual o primeiro órgão a se formar na gestação?')
          print('[1] Fígado')
          print('[2] Cérebro')
          print('[3] Pulmão')
          print('[4] Coração')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp1 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp1 == 1:
                  pontos += 0
                  break
              elif resp1 == 2:
                  pontos += 0
                  break
              elif resp1 == 3:
                  pontos += 0
                  break
              elif resp1 == 4:
                  pontos += 1
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Quantos ossos têm um adulto em média?')
          print('[1] 206')
          print('[2] 98')
          print('[3] 280')
          print('[4] 130')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp2 == 1:
                  pontos += 1
                  break
              elif resp2 == 2:
                  pontos += 0
                  break
              elif resp2 == 3:
                  pontos += 0
                  break
              elif resp2 == 4:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Como são chamadas as células presentes no sangue?')
          print('[1] Neurônios')
          print('[2] Hemácias')
          print('[3] Célula Tronco')
          print('[4] Glóbulos Brancos')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2e = int(input('Escolha [1, 2]: '))
              if resp2e == 1:
                  pontos += 0
                  break
              elif resp2e == 2:
                  pontos += 1
                  break
              elif resp2e == 3:
                  pontos += 0
                  break
              elif resp2e == 4:
                  pontos += 0
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual o maior órgão do corpo?')
          print('[1] Fígado')
          print('[2] Cérebro')
          print('[3] Coracão')
          print('[4] Pele')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp3 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp3 == 1:
                  pontos += 0
                  break
              elif resp3 == 2:
                  pontos += 0
                  break
              elif resp3 == 3:
                  pontos += 0
                  break
              elif resp3 == 4:
                  pontos += 1
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual o tipo sanguíneo considerado doador universal?')
          print('[1] O positivo')
          print('[2] A')
          print('[3] O negativo')
          print('[4] AB positivo')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp4 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp4 == 1:
                  pontos += 0
                  break
              elif resp4 == 2:
                  pontos += 0
                  break
              elif resp4 == 3:
                  pontos += 1
                  break
              elif resp4 == 4:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual das alternativas contem apenas órgãos que estão')
          print('em pares no corpo humano?')
          print('[1] Orelha, Braço, Coração')
          print('[2] Pulmão, Olhos, Rim')
          print('[3] Rim, Fígado, Cérebro')
          print('[4] Olhos, Náriz, Orelha ')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp5 = int(input('Escolha [1, 2]: '))
              if resp5 == 1:
                  pontos += 0
                  break
              elif resp5 == 2:
                  pontos += 1
                  break
              elif resp5 == 2:
                  pontos += 0
                  break
              elif resp5 == 2:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('____ é responsável por 70% do peso do corpo.')
          print('O que completa a frase?')
          print('[1] Sangue')
          print('[2] Ossos')
          print('[3] Água')
          print('[4] Músculos')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp6 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp6 == 1:
                  pontos += 0
                  break
              elif resp6 == 2:
                  pontos += 0
                  break
              elif resp6 == 3:
                  pontos += 1
                  break
              elif resp6 == 4:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual o nome da parte colorida do olho?')
          print('[1] Córnea')
          print('[2] Esclera')
          print('[3] Retina')
          print('[4] Íris')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp7 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp7 == 1:
                  pontos += 0
                  break
              elif resp7 == 2:
                  pontos += 0
                  break
              elif resp7 == 3:
                  pontos += 0
                  break
              elif resp7 == 4:
                  pontos += 1
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Cabelo e unha continuam crescendo depois da morte.')
          print('[1] Verdadeiro')
          print('[2] Falso')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp8 = int(input('Escolha [1, 2]: '))
              if resp8 == 1:
                  pontos += 1
                  break
              elif resp8 == 2:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('>:)DESAFIO: quantos cromossomos nós temos')
          print('[1] 3')
          print('[2] Mais de 1 milhão')
          print('[3] 46')
          print('[4] 209')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp9 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp9 == 1:
                  pontos += 0
                  break
              elif resp9 == 2:
                  pontos += 0
                  break
              elif resp9 == 3:
                  pontos += 1
                  break
              elif resp9 == 4:
                  pontos += 0
                  break
              else:
                  continue
          system('cls')
          sleep(1)
          print('-' * 40)
          print('')
          print('Seus pontos:')
          print(pontos)
          print('')
          print('-' * 40)
          sleep(10)
          system('cls')
          print('-' * 40)
          print('')
          while True:
            resp11 = str(input('Deseja Reiniciar o Quiz? [S/N] ')).upper()
            if resp11 == 'S':
                break
            elif resp11 == 'N':
                system('cls')
                break
          if resp11 == 'S':
              continue
          elif resp11 == 'N':
              system('cls')
              break

  elif respi2 == 2:
      while True:
          system('cls')
          pontos = 0
          print('-' * 42)
          print('')
          print('Quiz: Ciências (nível: Médio).')
          print('')
          print('Notas: 0 a 10')
          print('')
          print('-' * 42)
          sleep(5)
          system('cls')
          print('-' * 30)
          print('')
          print('           Iniciando')
          print('')
          print('-' * 30)
          sleep(3)
          system('cls')
          print('-' * 50)
          print('')
          print('Quantas vezes em média seus olhos')
          print('piscam por minuto?:')
          print('[1] 25 vezes')
          print('[2] 20 vezes')
          print('[3] 30 vezes')
          print('[4] 15 vezes')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp1 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp1 == 1:
                  pontos += 0
                  break
              elif resp1 == 2:
                  pontos += 1
                  break
              elif resp1 == 3:
                  pontos += 0
                  break
              elif resp1 == 4:
                  pontos += 0
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual dedo que sozinho é responsável')
          print('por 50% da força da mão?:')
          print('[1] Indicador')
          print('[2] Mindinho')
          print('[3] Anelar')
          print('[4] Polegar')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp2 == 1:
                  pontos += 0
                  break
              elif resp2 == 2:
                  pontos += 1
                  break
              elif resp2 == 3:
                  pontos += 0
                  break
              elif resp2 == 4:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Ao acordar de manhã você é um centimetro.')
          print('mais alto, do que quando você vai dormir')
          print('[1] verdadeiro')
          print('[2] falso')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2e = int(input('Escolha [1, 2]: '))
              if resp2e == 1:
                  pontos += 1
                  break
              elif resp2e == 2:
                  pontos += 0
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual a média de vezes em que um coração')
          print('de um adulto saudável bate por dia?')
          print('[1] Entre 80 mil a 140 mil batimentos')
          print('[2] Entre 90 mil a 100 mil batimentos')
          print('[3] Entre 100 mil a 140 mil batimentos')
          print('[4] Entre 100 mil a 120 mil batimentos')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp3 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp3 == 1:
                  pontos += 0
                  break
              elif resp3 == 2:
                  pontos += 1
                  break
              elif resp3 == 3:
                  pontos += 0
                  break
              elif resp3 == 4:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual o maior e mais pesado órgão do corpo')
          print('[1] Pulmão')
          print('[2] Intestinos')
          print('[3] Pele')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp4 = int(input('Escolha [1, 2, 3]: '))
              if resp4 == 1:
                  pontos += 0
                  break
              elif resp4 == 2:
                  pontos += 0
                  break
              elif resp4 == 3:
                  pontos += 1
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('A cada segundo, seu corpo produz produz')
          print('30 milhões de novas células:')
          print('[1] Falso')
          print('[2] Verdadeiro')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp5 = int(input('Escolha [1, 2]: '))
              if resp5 == 1:
                  pontos += 1
                  break
              elif resp5 == 2:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Em qual parte do corpo do ser humano')
          print('fica o maior osso?:')
          print('[1] Tórax')
          print('[2] Parte inferior da perna')
          print('[3] coxa')
          print('[4] Braço')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp6 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp6 == 1:
                  pontos += 0
                  break
              elif resp6 == 2:
                  pontos += 0
                  break
              elif resp6 == 3:
                  pontos += 1
                  break
              elif resp6 == 4:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Em qual parte do corpo fica o menor osso')
          print('do ser humano?')
          print('[1] mão')
          print('[2] pé')
          print('[3] ouvido')
          print('[4] nariz')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp7 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp7 == 1:
                  pontos += 0
                  break
              elif resp7 == 2:
                  pontos += 0
                  break
              elif resp7 == 3:
                  pontos += 1
                  break
              elif resp7 == 4:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Apesar de representar 2% de nossa massa corporal,')
          print('o cérebro usa 20% de nosso oxigênio e suprimento de sangue.')
          print('[1] Verdadeiro')
          print('[2] Falso')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp8 = int(input('Escolha [1, 2]: '))
              if resp8 == 1:
                  pontos += 1
                  break
              elif resp8 == 2:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('O corpo é formado por quantos por cento de agua?:')
          print('[1] 60%')
          print('[2] 90%')
          print('[3] 70%')
          print('[4] 80%')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp9 = int(input('Escolha [1, 2]: '))
              if resp9 == 1:
                  pontos += 0
                  break
              elif resp9 == 2:
                  pontos += 0
                  break
              elif resp9 == 3:
                  pontos += 1
                  break
              elif resp9 == 4:
                  pontos += 0
                  break
              else:
                  continue
          system('cls')
          sleep(1)
          print('-' * 40)
          print('')
          print('Seus pontos:')
          print(pontos)
          print('')
          print('-' * 40)
          sleep(10)
          system('cls')
          print('-' * 40)
          print('')
          while True:
            resp11 = str(input('Deseja Reiniciar o Quiz? [S/N] ')).upper()
            if resp11 == 'S':
                break
            elif resp11 == 'N':
                system('cls')
                break
          if resp11 == 'S':
              continue
          elif resp11 == 'N':
              system('cls')
              break
  elif respi2 == 3:
      while True:
          system('cls')
          pontos = 0
          print('-' * 42)
          print('')
          print('Quiz: Ciências (nível: Difícil).')
          print('')
          print('Notas: 0 a 10')
          print('')
          print('-' * 42)
          sleep(5)
          system('cls')
          print('-' * 30)
          print('')
          print('           Iniciando')
          print('')
          print('-' * 30)
          sleep(3)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é o nome das junções do corpo humano')
          print('que permitem a mobilidade dos ossos?')
          print('[1] Cartilagens')
          print('[2] Articulações')
          print('[3] Artérias')
          print('[4] Esqueleto')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp1 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp1 == 1:
                  pontos += 0
                  break
              elif resp1 == 2:
                  pontos += 0
                  break
              elif resp1 == 3:
                  pontos += 1
                  break
              elif resp1 == 4:
                  pontos += 0
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Como é chamado o tecido que reveste')
          print('a superfície e as cavidades do nosso corpo?')
          print('[1] Tecido nervoso')
          print('[2] Tecido conjuntivo')
          print('[3] Tecido epitelial')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2 = int(input('Escolha [1, 2, 3]: '))
              if resp2 == 1:
                  pontos += 0
                  break
              elif resp2 == 2:
                  pontos += 0
                  break
              elif resp2 == 4:
                  pontos += 1
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('As pessoas que têm habilidade com a')
          print('mão direita são chamadas de destras.')
          print('[1] verdadeiro')
          print('[2] falso')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2e = int(input('Escolha [1, 2]: '))
              if resp2e == 1:
                  pontos += 1
                  break
              elif resp2e == 2:
                  pontos += 0
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é a parte dos nossos olhos que pode se contrair e dilatar, controlando')
          print('assim a quantidade de luz que entra no globo ocular?')
          print('[1] Pupila')
          print('[2] Retina')
          print('[3] Córnea')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp3 = int(input('Escolha [1, 2, 3]: '))
              if resp3 == 1:
                  pontos += 1
                  break
              elif resp3 == 2:
                  pontos += 0
                  break
              elif resp3 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é o nome do movimento respiratório que faz com')
          print('que o ar entre nos pulmões?')
          print('[1] Inspirção')
          print('[2] Expiração')
          print('[3] Pulsação')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp4 = int(input('Escolha [1, 2, 3]: '))
              if resp4 == 1:
                  pontos += 1
                  break
              elif resp4 == 2:
                  pontos += 0
                  break
              elif resp4 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é o órgão do sistema respiratório')
          print('onde ocorrem as trocas gasosas?')
          print('[1] Faringe')
          print('[2] Traqueia')
          print('[3] Alvéolos')
          print('[4] Laringe')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp5 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp5 == 1:
                  pontos += 0
                  break
              elif resp5 == 2:
                  pontos += 0
                  break
              elif resp5 == 3:
                  pontos += 1
                  break
              elif resp5 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('As células que defendem o nosso corpo de microrganismos ')
          print('intrusos são as plaquetas.')
          print('')
          print('[1] Verdadeiro')
          print('[2] Falso')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp6 = int(input('Escolha [1, 2]: '))
              if resp6 == 1:
                  pontos += 0
                  break
              elif resp6 == 2:
                  pontos += 1
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Quem tem mais ossos?')
          print('[1] Bebês')
          print('[2] Adultos')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp7 = int(input('Escolha [1, 2]: '))
              if resp7 == 1:
                  pontos += 1
                  break
              elif resp7 == 2:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é o maior órgão do corpo humano?')
          print('[1] Pulmão')
          print('[2] Intestino')
          print('[3] Estômago')
          print('[4] Pele')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp8 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp8 == 1:
                  pontos += 0
                  break
              elif resp8 == 2:
                  pontos += 0
                  break
              elif resp8 == 3:
                  pontos += 0
                  break
              elif resp8 == 4:
                  pontos += 1
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Também conhecida como tutano, é um tecido, é um tecido gelatinoso que preenche')
          print('a cavidade interna de vários ossos e fabrica os elementos figurados do')
          print('sangue periférico como: hemácias, leucócitos e plaquetas. Qual é seu nome?')
          print('[1] Pele')
          print('[2] Medula Óssea')
          print('[3] Nervo')
          print('[4] Artéria')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp9 = int(input('Escolha [1, 2, 3, 4]: '))
              if resp9 == 1:
                  pontos += 0
                  break
              elif resp9 == 2:
                  pontos += 1
                  break
              elif resp9 == 3:
                  pontos += 0
                  break
              elif resp9 == 4:
                  pontos += 0
                  break
              else:
                  continue
          system('cls')
          sleep(1)
          print('-' * 40)
          print('')
          print('Seus pontos:')
          print(pontos)
          print('')
          print('-' * 40)
          sleep(10)
          system('cls')
          print('-' * 40)
          print('')
          while True:
            resp11 = str(input('Deseja Reiniciar o Quiz? [S/N] ')).upper()
            if resp11 == 'S':
                break
            elif resp11 == 'N':
                system('cls')
                break
          if resp11 == 'S':
              continue
          elif resp11 == 'N':
              system('cls')
              break
  elif respi2 == 4:
      while True:
          system('cls')
          pontos = 0
          print('-' * 42)
          print('')
          print('Quiz: Ciências (nível: EINSTEIN INSANO).')
          print('')
          print('Notas: 0 a 10')
          print('')
          print('-' * 42)
          sleep(5)
          system('cls')
          print('-' * 30)
          print('')
          print('           Iniciando')
          print('')
          print('-' * 30)
          sleep(3)
          system('cls')
          print('-' * 50)
          print('')
          print('Quais glândulas são responsáveis pela produção de suor?')
          print('[1] Glândulas endócrinas')
          print('[2] Glândulas sudoríparas')
          print('[3] Glândulas suprarrenais')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp1 = int(input('Escolha [1, 2, 3]: '))
              if resp1 == 1:
                  pontos += 0
                  break
              elif resp1 == 2:
                  pontos += 1
                  break
              elif resp1 == 3:
                  pontos += 0
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('A artéria mais importante do sistema circulatório é qual?')
          print('[1] Artéria Pulmonar')
          print('[2] Artéria Aorta')
          print('[3] Artéria Coronária')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2 = int(input('Escolha [1, 2, 3]: '))
              if resp2 == 1:
                  pontos += 0
                  break
              elif resp2 == 2:
                  pontos += 1
                  break
              elif resp2 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual nome do manor osso do corpo humano?')
          print('[1] Estribo')
          print('[2] Fêmur')
          print('[3] Clávicula')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp2e = int(input('Escolha [1, 2]: '))
              if resp2e == 1:
                  pontos += 1
                  break
              elif resp2e == 2:
                  pontos += 0
                  break
              elif resp2e == 3:
                  pontos += 0
                  break
              else:
                  continue 
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual desses órgãos influência todo nosso pensamento e é')
          print('conhecido como "segundo cérebro"')
          print('[1] Rins')
          print('[2] Intestino')
          print('[3] Coração')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp3 = int(input('Escolha [1, 2, 3]: '))
              if resp3 == 1:
                  pontos += 0
                  break
              elif resp3 == 2:
                  pontos += 1
                  break
              elif resp3 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual a velocidade que o espirro humano pode chegar?')
          print('[1] Até 123 Km/h')
          print('[2] Até 160 Km/h')
          print('[3] Até 156 Km/h')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp4 = int(input('Escolha [1, 2, 3]: '))
              if resp4 == 1:
                  pontos += 0
                  break
              elif resp4 == 2:
                  pontos += 1
                  break
              elif resp4 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Onde inicia a digestão das proteínas em nosso corpo?')
          print('[1] Fígado')
          print('[2] Pulmão')
          print('[3] Estômago')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp5 = int(input('Escolha [1, 2, 3]: '))
              if resp5 == 1:
                  pontos += 0
                  break
              elif resp5 == 2:
                  pontos += 0
                  break
              elif resp5 == 3:
                  pontos += 1
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é o maior seio facial?')
          print('')
          print('[1] Maxilar')
          print('[2] Etmoidal')
          print('[3] Esfenoidal')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp6 = int(input('Escolha [1, 2, 3]: '))
              if resp6 == 1:
                  pontos += 1
                  break
              elif resp6 == 2:
                  pontos += 0
                  break
              elif resp6 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é o menor órgão do corpo humano?')
          print('[1] Pineal')
          print('[2] Endócrinas')
          print('[3] Pâncreas')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp7 = int(input('Escolha [1, 2, 3]: '))
              if resp7 == 1:
                  pontos += 1
                  break
              elif resp7 == 2:
                  pontos += 0
                  break
              elif resp7 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Qual é o músculo mais forte do corpo humano?')
          print('[1] Masseter')
          print('[2] Quadríceps')
          print('[3] Língua')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp8 = int(input('Escolha [1, 2, 3]: '))
              if resp8 == 1:
                  pontos += 1
                  break
              elif resp8 == 2:
                  pontos += 0
                  break
              elif resp8 == 3:
                  pontos += 0
                  break
              else:
                  continue
          sleep(1)
          system('cls')
          print('-' * 50)
          print('')
          print('Aproximadamente quanto pesa o coração?')
          print('[1] 400 gramas')
          print('[2] 200 gramas')
          print('[3] 300 gramas')
          print('')
          print('-' * 50)
          print('')
          while True:
              resp9 = int(input('Escolha [1, 2, 3]: '))
              if resp9 == 1:
                  pontos += 0
                  break
              elif resp9 == 2:
                  pontos += 0
                  break
              elif resp9 == 3:
                  pontos += 1
                  break
              else:
                  continue
          system('cls')
          sleep(1)
          print('-' * 40)
          print('')
          print('Seus pontos:')
          print(pontos)
          print('')
          print('-' * 40)
          sleep(10)
          system('cls')
          print('-' * 40)
          print('')
          while True:
            resp11 = str(input('Deseja Reiniciar o Quiz? [S/N] ')).upper()
            if resp11 == 'S':
                break
            elif resp11 == 'N':
                system('cls')
                break
          if resp11 == 'S':
              continue
          elif resp11 == 'N':
              system('cls')
              break
  else:
      print('Finalizando')
      sleep(5)
      system('cls')
      break
