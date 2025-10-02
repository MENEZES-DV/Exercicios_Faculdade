
import psutil
import time
from datetime import timedelta

lista_id = [] # criei um array antes do looping, pois ele ficava armazenando sempre o ultimo valor digitado.
print ("LISTA DE PROCESSOS EM EXECUÇÃO")

for processo in psutil.process_iter():
    processo_nome = processo.name()
    processo_id = processo.pid
    lista_id.append(processo_id) # append para que a cada pasada ele apenas adicione um novo id e não sobreescreva.
    print (f"id do processo: {processo_id} | nome do processo {processo_nome}")

id_escolhido = int(input("Digite o id do processo que deseja consultar: ")) # o usuario escolhe o id que é atribuido a variavel id_escolhido.

if id_escolhido in lista_id: # verifica o id_escolhido está dentro da lista_id.  
    proc = psutil.Process(id_escolhido) # defini um objeto na varialvel proc, pra poder "puxar as informações".

    print(f"PROCESSO PARA CONSULTA: {proc.name()}") 

    print (f"PORCENTAGEM DE MEMÓRIA UTILIZADA PELO PROCESSO: {proc.memory_percent():.2f}%")

    print (f"PORCENTAGEM DE PROCESSAMENTO UTILIZADA PELO PROCESSO: {proc.cpu_percent(interval=10):.2f}%")

    tempo_execucao = (time.time() - proc.create_time()) # calcula o "tempo de vida" do processo.
    duracao = timedelta(seconds =int(tempo_execucao)) # transforma esse tempo de vida em formato padrão de horas, minutos e segundos.
    
    print (f"TEMPO EM HORAS DE EXECUÇÃO DO PROCESSO: {duracao}")

else: 
    print("Este processo não existe ou não está em execução.")