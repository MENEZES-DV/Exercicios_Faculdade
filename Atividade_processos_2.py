import psutil
import time

processos_ordenados = [] 

for processo in psutil.process_iter(['name', 'pid', 'username', 'memory_info']): 
    try:  
        processos_ordenados.append(processo) 
    except (psutil.AccessDenied): 
        pass 
         
#Ordenação dos Processos
processos_ordenados.sort(key=lambda x: x.info['memory_info'].rss, reverse=True) 
 
for processo in processos_ordenados[:]: 
    try: 
        nome_processo = processo.info['name'] 
        id_processo = processo.info['pid'] 
        user_processo = processo.info['username'] 
        memo_processo = processo.info['memory_info'] 
        memoria = memo_processo.rss / (1024 * 1024) 
        print(f"{id_processo} - {nome_processo} - {user_processo} - {memoria:.2f}") 
    except (psutil.AccessDenied): 
        pass 

#Fechar o processo      
def finalizar_proc():

    finalizar = int(input(" \nESCOLHA O ID DO PROCESSO QUE DESEJA FINALIZAR:")) 

    for processo in processos_ordenados:
        
        if processo.info['pid'] == finalizar:
            try: 
                fechar_processo = psutil.Process(finalizar) 
                if fechar_processo.is_running(): 
                    fechar_processo.terminate()
                    print ("\nFINALIZANDO PROCESSO...")
                    time.sleep(2)
                    print ("\nPROCESSO FINALIZADO \n") 
                else: 
                    print ("\nPROCESSO JÁ FINALIZADO \n")     
            
            except(psutil.NoSuchProcess): 
                pass
            break
        
    else:
        print("\nID NÃO ENCONTRADO NA LISTA, TENTE NOVAMENTE.")
        time.sleep(1)
        finalizar_proc()
        
finalizar_proc()