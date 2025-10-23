import random
import time

print("bem vindo ao jogo de matematica!")
print("responda o máximo que pude. digite 'sair' para encerrar.\n")

pontos = 0
pontos = 1
 
 while true:
     #gera dois números e uma operaçao aleatória
     n1 = random.randint(1,10)
     n2 = random.randint(1,10)
     operaçao = random.choice(["+","-","*"])
     
     #calcula o resultado certo 
     if operaçao =="+":
         resultado_certo = n1+n2
         elif operaçao =="-":
             resultado_certo = n1-n2
             else:
                 resultado_certo = n1*n2
                 
                 print(f"Pergunta{rodada}:quanto é {n1}{operaçao}{n2}?")
                 resposta = input(">")
                 
                 if resposta.lower() == "sair".
                 break
             
             #verifique se é número
             if resposta.isdigit()and not (resposta.startswith("-")and resposta[1:].isdigit()):
                 print("por favor, digite um numero ou 'sair'. ")
               continue 
           
           if int(resposta) ==resultado_certo:
               pontos +=1
               print("correto!")
             else:
                 print(f"errado! a resposta certa era{resultado_certo}.")
                  
                  rodada+=1
                  time.sleep(1)
                  print("-"*30)
print(f"\n Fim do jogo! Você faz{pontos}ponto(s).")
         
         
         
         