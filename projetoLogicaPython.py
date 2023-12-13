

import random
import time


fim_cad = time.time() + 30.
cadastro=dict()
lista_de_clientes=list()



while time.time() < fim_cad:
    cadastro["NOME"]=str(input("Para participar da promoção, digite aqui o seu nome completo: "))
    cadastro["TELEFONE"]=str(input("Para participar da promoção, digite aqui o seu telefone com DDD:\n "))
    lista_de_clientes.append(cadastro.copy())
    if time.time() == fim_cad:
        print("Acabou o expediente, por consequência, também finalizaremos o cadastro para participação da Promoção!\n")
        break
time.sleep(1)
print("Segue abaixo os participantes que se habilitaram para concorrer a promoção:\n")
for x in lista_de_clientes:
    for chave, valor in x.items():
        print(f"{chave}->{valor}")
time.sleep(1)
print("Vamos ao sorteio do vencedor!\n")
time.sleep(2)
sorteado=random.choice(lista_de_clientes)
print(f"O participante sorteado foi: {sorteado['NOME']}, telefone:{sorteado['TELEFONE']}\n")
