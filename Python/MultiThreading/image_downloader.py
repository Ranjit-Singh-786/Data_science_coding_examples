import requests,os,time
from threading import Thread
import random
import string
from concurrent.futures import ThreadPoolExecutor

random_img_generator_url = "https://picsum.photos/2000/3000"

def image_downloader(num_images,url):
    for i in range(num_images):
        response = requests.get(url)
        os.makedirs("downloaded_image",exist_ok=True)
        unique_id = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        file_path = os.path.join(os.getcwd(),"downloaded_image","image_"+str(unique_id)+".jpg")
        with open(file_path,"wb") as file:
            file.write(response.content)
            print(f"Successfully Downloaded :{file_path}")

# ???????????   DIFFERENT WAY TO EXECUTE YOUR FUNCTION     ???????????????????
# #<<<<<<<<<<< 1. TO DOWNLOAD IN SEQUENTIAL MANNER    >>>>>>>>>>>>
t1 = time.perf_counter()
image_downloader(5,random_img_generator_url)
t2 = time.perf_counter()
print("Time Taken by normal execution !")

# # #<<<<<<<<<<< 2. TO DOWNLOAD IN PARALLEL MANNER WITH THREAD   >>>>>>>>>>>>

downloading_thread_1 = Thread(target=image_downloader,args=[5,random_img_generator_url])
downloading_thread_1.start()

downloading_thread_2 = Thread(target=image_downloader,args=[10,random_img_generator_url])
downloading_thread_2.start()

downloading_thread_3 = Thread(target=image_downloader,args=[20,random_img_generator_url])
downloading_thread_3.start()
print('Images are downloading in background !')


# #<<<<<<<<< 3. Syntex with using ThreadPoolExecutor    >>>>>>>>>>>>>>>>

with ThreadPoolExecutor() as executor:
    pool1 = executor.submit(image_downloader,10,random_img_generator_url)
    print(pool1.result())

    pool2 = executor.submit(image_downloader,5,random_img_generator_url)
    print(pool2.result())

    pool3 = executor.submit(image_downloader,8,random_img_generator_url)
    print(pool3.result())

# if you r using .result() it means, utill and unless your entire pool will not be
# executed, because .result() wait for output of the pool execution,
# due to .result our pool execution wait to finish the execution.
print('Images are downloading in background !')



# #<<<<<<<<<  Syntex with using ThreadPoolExecutor without result    >>>>>>>>>>>>>>>>
#Now we are sending our execution in background, and moving to executing on further lines of code.
executor =  ThreadPoolExecutor()
pool1 = executor.submit(image_downloader, 10, random_img_generator_url)
pool2 = executor.submit(image_downloader, 5, random_img_generator_url)
pool3 = executor.submit(image_downloader, 8, random_img_generator_url)

# Continue executing further lines of code here
print('Images are downloading in background !')


# <<<<<<<<<<<   4. instead of submit() use map() to optimize the code    >>>>>>>>>>>>>>>>>>>>>>>

# Define the arguments for the image downloader function
num_images_list = [5, 5, 5]
url_list = [random_img_generator_url] * len(num_images_list)

with ThreadPoolExecutor() as executor:
    # all are poolexecuting parallel, but untill, all it will not be complete, further line
    # of code will not get execute.
    results = executor.map(image_downloader, num_images_list, url_list)




