import  socket 
import  time 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
my_ip="127.0.0.1"
# -- 52.2.116.225 -- 
my_port=9999
my_address=(my_ip,my_port)
# let me start above defined address 
s.bind(my_address)

while 3 > 2 :
    data=s.recvfrom(100)
    # only filetring message 
    new_data=data[0]
    ip_address = data[1]
    final_msg=new_data.decode('ascii')
    print(final_msg)
    with open(str(ip_address[0]),'a+')  as file: 
        file.write(final_msg+'\n')
    # implement file handing print 
    time.sleep(1)