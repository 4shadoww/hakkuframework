Hakku Framework
===============

Hakku is a simple framework that is made for penetration testing tools.
Hakku framework offers a simple structure, basic CLI, and useful features for penetration testing modules development.

Getting started
----------------------

Documentation is available in Github wiki and in "docs" directory.

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
* proxy_scout
* whois
* web_killer
* web_scout
* wifi_jammer
* zip_cracker
* rar_cracker
* wordlist_gen

Dependencies
------------

All external python dependencies are included. Network scanner requires tcpdump.
All module dependencies are listed below:

- ethtool
- aircrack-ng
- ettercap-text-only
- dsniff
- xterm
- driftnet
- tcpdump
- libnetfilter-queue-dev
- python3.5-dev
- hcitool
- sslstrip
- l2ping

License
-------

Hakku Framework is licensed under MIT license.
