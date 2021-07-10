import subprocess
import time
import sys
import os
import platform
from .exceptions import WhoisCommandFailed


PYTHON_VERSION = sys.version_info[0]
CACHE = {}
CACHE_MAX_AGE = 60*60*48    # 48h

try:
    import json
except:
    import simplejson as json


def cache_load(cf):
    if not os.path.isfile(cf):
        return

    global CACHE
    f = open(cf, 'r')

    try:
        CACHE = json.load(f)
    except:
        pass
    f.close()


def cache_save(cf):
    global CACHE
    f = open(cf, 'w')
    json.dump(CACHE, f)
    f.close()


def do_query(dl, force=0, cache_file=None, slow_down=0, ignore_returncode=0):
    k = '.'.join(dl)
    if cache_file:
        cache_load(cache_file)
    if force or k not in CACHE or CACHE[k][0] < time.time() - CACHE_MAX_AGE:
        CACHE[k] = (
            int(time.time()),
            _do_whois_query(dl, ignore_returncode),
        )
        if cache_file:
            cache_save(cache_file)
        if slow_down:
            time.sleep(slow_down)

    return CACHE[k][1]


def _do_whois_query(dl, ignore_returncode):
    if platform.system() == 'Windows':
        """
            Windows 'whois' command wrapper
        """
        if not os.path.exists('whois.exe'):
            print("downloading dependencies")
            folder = os.getcwd()
            copy_command = r"copy \\live.sysinternals.com\tools\whois.exe "+folder
            print(copy_command)
            p = subprocess.call(copy_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        # print(p.stdout.read()+' '+p.stderr.read())
        p = subprocess.Popen([r'.\whois.exe ', '.'.join(dl)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    else:
        """
            Linux 'whois' command wrapper
        """
        p = subprocess.Popen(['whois', '.'.join(dl)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    r = p.communicate()[0]
    r = r.decode(errors='ignore') if PYTHON_VERSION == 3 else r
    if not ignore_returncode and p.returncode != 0 and p.returncode != 1:
        raise WhoisCommandFailed(r)
    return r
