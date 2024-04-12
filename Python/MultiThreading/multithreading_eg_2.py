from threading import Thread
import time 
done = False

def test_worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)
        if counter >= 15:
            break

def test_worker2():
    while not done:
        time.sleep(5)
        print('Hiii i am available !')

t1 = Thread(target=test_worker)
t2 = Thread(target=test_worker2)

t1.start()
 # if you want to complete first it thread, then apply join() function on it,
# untill and unless that thread will not be complete, it will not start any other thread or line of program
t1.join() 

# after completing t1 then t2 start.
t2.start()

# output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# Hiii i am available !
# Hiii i am available !
# Hiii i am available !
# Hiii i am available !
# Hiii i am available !
# Hiii i am available !
# Hiii i am available !
# .
# .
# ...