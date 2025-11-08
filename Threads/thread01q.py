import threading
import time

def imprimir_nome_thread(nome):
    while True:
        print(nome)
        time.sleep(2) #2 segundos 

for i in range(5):
    thread = threading.Thread(target=imprimir_nome_thread, args=(f"Thread {i+1}", i + 1, ))
                                        
    threading.start()
