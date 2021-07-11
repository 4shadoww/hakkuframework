Hakku Framework
===============

Hakku is a simple framework that is made for penetration testing tools.
Hakku framework has a simple structure, basic CLI, and useful features for penetration testing modules development.

Getting started
---------------

Use the "help" command to see all available commands. Here is a Youtube video if you wish to see Hakku in action: https://www.youtube.com/watch?v=1R0slN0vVHU&t=15s

Installation
------------

If you want to make an installation to your system, you can do it with the "install.py" script. However, this is not required and hakku can be run as "portable" from the directory.

OS support
----------

Only GNU/Linux is supported. No Mac, Windows or even Android with termux is supported.

Modules
-------

24 modules are available in total.

* apache_users
* arp_dos
* arp_monitor
* arp_spoof
* bluetooth_pod
* cloudflare_resolver
* dhcp_dos
* dir_scanner
* dns_spoof
* email_bomber
* hostname_resolver
* mac_spoof
* mitm
* network_kill
* pma_scanner
* port_scanner
* proxy_detector
* whois
* web_killer
* webserver_info
* wifi_jammer
* zip_cracker
* rar_cracker
* wordlist_gen

Dependencies
------------

All external python dependencies are included except "NetfilterQueue". A "scan" command requires tcpdump.
All module dependencies are listed below:

- ethtool
- aircrack-ng
- ettercap-text-only
- dsniff
- xterm
- driftnet
- tcpdump
- libnetfilter-queue
- python 3
- hcitool
- sslstrip
- l2ping

License
-------

Hakku Framework is licensed under MIT license.


Bugs
----
Please leave bug reports to https://github.com/4shadoww/hakkuframework.
