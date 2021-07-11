# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)
import sys
import http.client
import re
import urllib.request
import socket

from core.hakkuframework import *
from core import colors


conf = {
    "name": "proxy_detector",
    "version": "1.0",
    "shortdesc": "detect http proxy",
    "author": "4shadoww",
    "github": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "2016-05-19",
    "lastmod": "2016-12-29",
    "apisupport": False

}

# List of the variables
variables = OrderedDict((
    ('target', ['192.168.1.2', 'target address']),
    ('port', ['80', 'target port']),
    ('timeout', ['1', 'timeout (default: 1)']),
    ('port_range', ['1-100000', 'port range (default: 1-100000)']),
    ('use_range', ['0', 'scan port range(1=yes/0=no)']),
    ('scan_common', ['0', 'scan commonly used ports(1=yes/0=no)']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    commonports = ['80', '8080', '8888', '25', '3128', '8003', '9529', '8088', '8118', '4624', '9090', '82', '8090', '5555', '81', '7004', '9797', '7777', '8998', '9999', '10200']
    variables['target'][0] = variables['target'][0].replace("http://", "").replace("https://", "")
    if variables['target'][0] == 'google.com':
        print_error('not a valid address')
        return
    try:
        try:
            socket.setdefaulttimeout(int(variables['timeout'][0]))
        except ValueError:
            print_error('not valid timeout')
            return
        if variables['use_range'][0] != '1' and variables['scan_common'][0] != '1':
            proxy_support = urllib.request.ProxyHandler({"http":variables['target'][0]+':'+variables['port'][0]})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)

            html = urllib.request.urlopen("http://www.google.com").read()
            print_success('proxy server detected')
        if variables['scan_common'][0] == '1':
            for port in commonports:
                try:
                    status = colors.yellow+'[*] scanning port '+ port+colors.end
                    sys.stdout.write("\r%s" % status)
                    sys.stdout.flush()
                    proxy_support = urllib.request.ProxyHandler({"http":variables['target'][0]+':'+port})
                    opener = urllib.request.build_opener(proxy_support)
                    urllib.request.install_opener(opener)

                    html = urllib.request.urlopen("http://www.google.com").read()
                    print(' :'+colors.green+' proxy detected'+colors.end)

                except http.client.BadStatusLine:
                    print_success('\nproxy server detected')
                    break

                except urllib.error.URLError:
                    pass
                
                except socket.timeout:
                    pass
                
                except ConnectionResetError:
                    print(' :'+colors.green+' proxy detected'+colors.end)
            print_success('\ndone')

        if variables['use_range'][0] == '1':
            ports = re.sub("-", " ",  variables['port_range'][0]).split()
            for port in range(int(ports[0]), int(ports[1])):
                try:
                    status = colors.yellow+'[*] scanning port '+ str(port)+colors.end
                    sys.stdout.write("\r%s" % status)
                    sys.stdout.flush()
                    proxy_support = urllib.request.ProxyHandler({"http":variables['target'][0]+':'+str(port)})
                    opener = urllib.request.build_opener(proxy_support)
                    urllib.request.install_opener(opener)

                    html = urllib.request.urlopen("http://www.google.com").read()
                    print(' :'+colors.green+' proxy detected'+colors.end)

                except http.client.BadStatusLine:
                    print_success('\nproxy server detected')
                    break

                except urllib.error.URLError:
                    pass
                
                except socket.timeout:
                    pass
                
                except ConnectionResetError:
                    print(' :'+colors.green+' proxy detected'+colors.end)
            print_success('\ndone')

    except http.client.BadStatusLine:
        print_success('proxy server detected')

    except urllib.error.URLError:
        print_error('URLError')
    
    except socket.timeout:
        print_error('timeout')
    
    except ConnectionResetError:
        print_success('proxy detected')
