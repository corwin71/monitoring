import ssl
import socket
import datetime
import os

sitename = "profstomtula.ru"

def ssl_expiry_datetime(host, port=443):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=host,
    )
    conn.settimeout(3.0)
    conn.connect((host, port))
    ssl_info = conn.getpeercert()
    print(ssl_info)
    res = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
    return res


delta_cert_time = (ssl_expiry_datetime(sitename) - datetime.datetime.now()).days

print(delta_cert_time)


if delta_cert_time > 100:
    print ("warning")



os.system("echo Hello from the other side!")