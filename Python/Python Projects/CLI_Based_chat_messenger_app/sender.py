import  socket 
#number of functions in socket module / library 
#print(dir(socket))
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
#               ipaddress ,  prototocol 
# finally s is having capabilty to create UDP socket 
# target system address
target_ip="127.0.0.1"
target_port=9999
final_target=(target_ip,target_port)
# taking input from user
quiet = True
while quiet:
    msg=input("Plz enter your message : ")
    # since python3 is supporting minimum encoding 
    new_msg=msg.encode('ascii')
    # final lets send data 
    s.sendto(new_msg,final_target)

    # code to quiet the sender program
    user_input = input("do you want to quiet it ? press Y/N : ")
    if user_input == "y" or user_input=='Y':
        quiet = False