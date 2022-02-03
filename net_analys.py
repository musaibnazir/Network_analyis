# importing libraries
import subprocess
import os
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")





def net_info():
    ifconfig = subprocess.run(["ifconfig", "-a"])
    interface=str(input("Interface: "))
    ifconfig = subprocess.run(["ifconfig",interface])


def show_interface():
    int = subprocess.run(["ip addr"])
    interface =str(input("Enter interface:"))
    int = subprocess.run(["ip address show", interface])
                         
def traceroute():
    destination = str(input("Enter the Destination IP: "))
    int = subprocess.run(["traceroute", destination])
    
       
def nslookup():
    int = subprocess.run(["nslookup -h"])  
    domain=str(input("Enter Domain: "))
    int = subprocess.run(["nslookup", domain])  
   
def dig():
    int = subprocess.run(["dig -h"])  
    domain = str(input("Enter Domain:"))
    int = subprocess.run(["dig", domain])  
                                   
def route():
    int = subprocess.run(["route"])  

def host():
    int = subprocess.run(["host"]) 
    arg=str(input("Enter Domain:")) 
    int = subprocess.run(["host",arg])  
    
def arp():
    int = subprocess.run(["arp -a"])   
 
def iwconfig():
    int = subprocess.run(["iwconfig"])  
    arg = str(input("Enter Interface: "))
    int = subprocess.run(["iwconfig",arg])  
 
def curl():
    int = subprocess.run(["curl -h"])  
    int = subprocess.run(["curl ifconfig.me"])  
 
 
def whois():
    int = subprocess.run(["whois -h"]) 
    url=str(input("Enter URL: ")) 
    int = subprocess.run(["whois",url])  

def ifplugd():
    int = subprocess.run(["ifplugstatus -h"]) 
    interface = str(input("Enter Interface: ")) 
    int = subprocess.run(["ifplugstatus",interface])  
 
def nload():
    int = subprocess.run(["nload"])  
    
def w():
    int = subprocess.run(["w"]) 
  
def ifstat():
    int = subprocess.run(["ifstat"])       

def ethtool():
    int = subprocess.run(["ethtool"])  
    interface = str(input("Enter Interface: "))
    int = subprocess.run(["ethtool",interface])  
     
def iftop():
    int = subprocess.run(["iftop -h"]) 
    interface = str(input("Enter Interface: ")) 
    int = subprocess.run(["iftop -i",interface])  
    
def hostname():
    int = subprocess.run(["hostname"])  
    int = subprocess.run(["hostname -i"])  
    

def tcpdump():
    int = subprocess.run(["tcpdump"]) 
    interface=str(input("Enter Interface: "))
    int = subprocess.run(["tcpdump -i",interface]) 

def dstat():
    int = subprocess.run(["dstat"]) 
 
def tshark():
    int = subprocess.run(["tshark -D"]) 
    interface = str(input("Enter Interface: "))
    int = subprocess.run(["tshark -i",interface]) 
    
def hping3():
    int = subprocess.run(["hping3 -h"]) 
    interface=str(input("Enter Interface: "))
    int = subprocess.run(["hping3 recv",interface]) 


   

if __name__ == '__main__':
    print("/n****************************************\n1NETWORK ANALYSIS | Dated: "+dt_string+ " | MNR\n\n")
    while True:
        print('''
              ENTER THE NO TO USE THE APP;
            1. NET INFO
            2. SH INTERFACE
            3. TRACEROUTE
            4. NSLOOKUP
            5. DIG
            6. ROUTE
            7. HOST
            8. ARP
            9. WIFI INFO
            10. WHATS MY EXTERNAL IP
            11. WHOIS
            12. IF PLUGGED
            13. N LOAD
            14. CHECK USER
            15. IF STATICS
            16. ETHTOOLS
            17. IF TOP
            18. HOSTNAME
            19. TCPDUMP
            20. D STATS
            21. TSHARK
            22. HPING3
            
        ''')
        option=str(input("Enter Option:(or q to quit) "))
        if option == '1':
            net_info()
            continue
        elif option == '2':
            show_interface()
            continue
        elif option == '3':
            traceroute()
            continue
        elif option == '4':
            nslookup() 
            continue
        elif option == '5':
            dig()
            continue
        elif option == '6':
            route()
            continue          
        elif option == '7':
            host() 
            continue   
        elif option == '8':
            arp()
            continue    
        elif option == '9':
            iwconfig() 
            continue  
        elif option == '10':
            curl()
            continue
        elif option == '11':
            whois()
            continue
        elif option == '12':
            ifplugd()
            continue
        elif option == '13':
            nload()
            continue
        elif option == '14':
            w()
            continue
        elif option == '15':
            ifstat()
            continue
        elif option == '16':
            ethtool()
            continue
        elif option == '17':
            iftop()
            continue
        elif option == '18':
            hostname()
            continue
        elif option == '19':
            tcpdump()
            continue
        elif option == '20':
            dstat()
            continue
        elif option == '21':
            tshark()
            continue
        elif option == '22':
            hping3()
            continue  
        elif option == 'q':
            print('Thankyou for using this Program..BYE')
            break  
        else:
            print("Wrong Option..Plese check and try correctly or press q to quit.")  
            continue                        
                                 