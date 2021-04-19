import nmap3
import netifaces as ni
nmap = nmap3.NmapHostDiscovery()
#Below is what is deciding what to do in different cases, then its doing the scan
try:
    ni.ifaddresses('wlan0')
    ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    ip = str(ip+'/24')
    results = nmap.nmap_no_portscan(ip)
except:
    try:
        interface = str(input('Enter Your Interface name e.g. wlan0: '))
        ni.ifaddresses(interface)
        ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        ip = str(ip+'/24')
        results = nmap.nmap_no_portscan(ip)
    except KeyboardInterrupt:
        print("\nGood Bye!")


#Below is what's printing the result to the user
try:
    for result in results:
        try:
            mac = results[result]['macaddress']['addr']
            name = results[result]['macaddress']['vendor']
            print(F'{mac}       ||       {name}')
        except:
            pass

except NameError:
    pass