from multiprocessing import Process
import time

def task():
    for i in range(10):
        time.sleep(2)
        print("Task done")
def task2():
    for i in range(5):
        time.sleep(3)
        print("hello wolrd")


if __name__ == "__main__":  # 🔒 Required for multiprocessing
    p2 = Process(target=task2)
    p1 = Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("processed finished") # ye line jbtk execute nhi hogi ab tbtk pichhli dono process finished n ho jaye, kyuki join lga hua he.