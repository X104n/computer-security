from socket import socket, timeout, AF_INET, SOCK_DGRAM
import pickle 

sock = socket(AF_INET,SOCK_DGRAM)
sock.settimeout(3)

oslotemps = []
bergentemps = []
karmøytemps = []



def oslo(x=''):
    text = f"oslo {x}"
    sock.sendto(text.encode(),("localhost",2222))
    oslotemps.clear()


    while True:
            try:
                data = sock.recv(2048)
                d = pickle.loads(data)
                oslotemps.append(d)
            except timeout:
                break
            except:
                print("this local server is down!")
                break
# oslo()

def bergen(x=''):
    text = f"bergen {x}"
    sock.sendto(text.encode(),("localhost",4444))
    bergentemps.clear()
    while True:
            try:
                data = sock.recv(2048)
                d = pickle.loads(data)
                bergentemps.append(d)
            except timeout:
                break
            except:
                print("this local server is down!")
                break
# bergen()


def karmøy(x=''):
    text = f"karmøy {x}"
    sock.sendto(text.encode(),("localhost",4444))
    karmøytemps.clear()
    while True:
            try:
                data = sock.recv(2048)
                d = pickle.loads(data)
                karmøytemps.append(d)
            except timeout:
                break
            except:
                print("this local server is down!")
                break
# karmøy()

"""
this is the homepage example, this just shows how everything will look
"""

homepage = [
    {
        'location' : 'Bergen',
        'temp': 9, 
        'rain': 0.5,
        'date': '3th of May',
        'loclower': 'bergen'

    },
    {
        'location' : 'Karmøy',
        'temp': 6, 
        'rain': 1.5,
        'date': '3th of May',
        'loclower': 'karmøy'

    },
    {
        'location' : 'Oslo',
        'temp': 15, 
        'rain': 0,
        'date': '3th of May',
        'loclower': 'oslo'

    }
    
]