import ssl
import socket
import datetime

def check_cert_expiration(hostname):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(), server_hostname=hostname)
    conn.settimeout(3.0)
    try:
        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()
        expires = ssl_info['notAfter']
        expires = datetime.datetime.strptime(expires, "%b %d %H:%M:%S %Y %Z")
        now = datetime.datetime.now()
        if expires > now:
            print("The SSL certificate for {} will expire on {}.".format(hostname, expires))
        else:
            print("The SSL certificate for {} has expired on {}.".format(hostname, expires))
    except ssl.SSLError as e:
        print("Error checking SSL certificate for {}: {}".format(hostname, e))
    except socket.timeout:
        print("Timed out checking SSL certificate for {}".format(hostname))

# read domains from txt file
with open("domains.txt", "r") as f:
    domains = f.readlines()
    domains = [x.strip() for x in domains]

for domain in domains:
    check_cert_expiration(domain)
