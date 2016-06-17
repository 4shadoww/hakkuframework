#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from core import bcolors
from collections import OrderedDict


database = OrderedDict((
#wireless bluetooth
(bcolors.UNDERLINE+bcolors.OKBLUE+'Wireless / Bluetooth'+bcolors.END, bcolors.UNDERLINE+bcolors.OKBLUE+'Description'+bcolors.END),
('wifi_jammer', 'jam wifi'),
('bluetooth_pod', 'bluetooth ping of death'),
#end
(' ',''),
#web modules
(bcolors.UNDERLINE+bcolors.OKBLUE+'Web Modules'+bcolors.END, bcolors.UNDERLINE+bcolors.OKBLUE+'Description'+bcolors.END),
('cloudflare_resolver', 'tries to resolve real ip address from sub domains'),
('dir_scanner', 'scan dirs from target address'),
('web_killer', 'TCP Attack'),
('apache_users', 'scan directory of apache users'),
('pma_scanner', 'PHPMyAdmin login page scanner'),
('port_scanner', 'scan open ports'),
('email_bomber', 'spam emails'),
('hostname_resolver', 'resolve hostname using ip'),
('webserver_scout', 'get information from webserver'),
#end
('  ',''),
#network modules
(bcolors.UNDERLINE+bcolors.OKBLUE+'Network Modules'+bcolors.END, bcolors.UNDERLINE+bcolors.OKBLUE+'Description'+bcolors.END),
('network_kill', 'kicks out target device from network'),
('arp_dos', 'arp cache denial of service attack'),
('arp_spoof', 'arp spoof'),
('mac_spoof', 'use fake mac address'),
('mitm', 'man in the middle attack'),
('dns_spoof', 'dns spoof'),

#end
('   ',''),
))