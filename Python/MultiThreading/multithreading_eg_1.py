#in this file, there are 2 function executing parallelly using threading
from threading import Thread
import time 
done = False

def test_worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

def test_worker2():
    while not done:
        time.sleep(5)
        print('Hiii i am available !')

t1 = Thread(target=test_worker)
t2 = Thread(target=test_worker2)

t1.start()
t2.start()

