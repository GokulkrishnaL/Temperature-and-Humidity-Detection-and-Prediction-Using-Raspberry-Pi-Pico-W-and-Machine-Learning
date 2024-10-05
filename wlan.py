import network
import socket
from time import sleep
import machine
import urequests
ssid = '12345678'
password = '12345678'
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip


connect()
url='https://api.thingspeak.com/update?api_key=HED54B47AZ4Y6FRH&field1=26&field2=82'
data=urequests.post(url)
print(data.json())
