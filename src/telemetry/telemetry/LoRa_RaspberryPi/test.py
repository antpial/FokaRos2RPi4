import loralib       
from time import sleep as Sleep

loralib.init(0, 434000000, 7) 
i=0; 
while True:
    message = f"Hello World {i}"   
    print(message)                                     
    loralib.send(message.encode())
    i+=1
    Sleep(2)  # Sleep for 1 second to avoid flooding the channel