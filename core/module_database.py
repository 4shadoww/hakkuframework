#        Copyright [C] 2015 Noa-Emil Nissinen [4shadoww]

from core import colors


database = [
# Wireless, bluetooth
[colors.uline+colors.red+"Wireless / Bluetooth"+colors.end, colors.uline+colors.red+"Description"+colors.end],
["wifi_jammer", "jam wifi"],
["bluetooth_pod", "bluetooth ping of death"],
# End of wireless, bluetooth modules
["",""],

# Web modules
[colors.uline+colors.red+"Web Modules"+colors.end, colors.uline+colors.red+"Description"+colors.end],
["cloudflare_resolver", "tries to resolve real ip address from sub domains"],
["dir_scanner", "scan dirs from target address"],
["web_killer", "TCP Attack"],
["apache_users", "scan directory of apache users"],
["pma_scanner", "PHPMyAdmin login page scanner"],
["port_scanner", "scan open ports"],
["email_bomber", "spam emails"],
["hostname_resolver", "resolve hostname using ip"],
["webserver_scout", "get information from webserver"],
["proxy_scout", "scan http proxy from ip"],
["whois", "perform whois query"],
# End of web modules
["",""],

# Network modules
[colors.uline+colors.red+"Network Modules"+colors.end, colors.uline+colors.red+"Description"+colors.end],
["network_kill", "kicks out target device from network"],
["arp_dos", "arp cache denial of service attack"],
["arp_spoof", "arp spoof"],
["mac_spoof", "use fake mac address"],
["mitm", "man in the middle attack"],
["dns_spoof", "dns spoof"],
# End of network modules
["",""],

# File modules
[colors.uline+colors.red+"File modules"+colors.end, colors.uline+colors.red+"Description"+colors.end],
["zip_cracker", "zip file brute-force attack using dictionary"],
["rar_cracker", "rar file brute-force attack using dictionary"],

# End of file modules
]