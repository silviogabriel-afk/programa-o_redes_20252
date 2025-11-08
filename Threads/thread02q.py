import threading
import time


def imprimir():
    for i in 100000:
        print(i)
        time.sleep(2)  # 2 segundos


tt = threading.Thread(target=imprimir,)
tt.start()

ttt= threading.Thread(target=imprimir,)
ttt.start()

threading.Thread()