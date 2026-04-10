from sys import exit
import requests
import socket 
import time
import matplotlib.pyplot as plt
from tkinter import *


def main():


    client = socket.socket()

    print ("enter url(ex: example.com): ")

    url = str(input())

    client.connect((url, 80))

    message = (
    f"GET / HTTP/1.1\r\n"
    f"Host: {url}\r\n"
    f"Connection: close\r\n\r\n"
)
    

    print("Connected...")

    client.send(message.encode())  
    data = client.recv(1024) 

    if not url.startswith("http"):
        url = "http://" + url

    times = []

#------
    for i in range(20):
        start = time.time()
        response = requests.get(url)
        enapsed = time.time() - start
        times.append(enapsed)

    print(response.status_code, "\n and ", data.decode(), "\n and enapsed: ", enapsed)

    

    if response.status_code == 200:
        print("server is alive")

    plt.plot(times)

    plt.ylabel("Response times (s)")
    plt.xlabel("Request #")
#------
    plt.show()

    root = Tk()
    root.title("is evelible syte")
    root.geometry()
    #root.geometry("300x250")


    label = Label(text= f"response.status_code, \n and , {data.decode()}, \n and enapsed: , {enapsed}")

    label.pack(anchor="nw")
    

    root.mainloop()


    client.close()

    

main()