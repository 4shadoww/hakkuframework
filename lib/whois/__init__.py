"""
    Python module/library for retrieving WHOIS information of domains.

    By DDarko.org  ddarko@ddarko.org  http://ddarko.org/
    License MIT  http://www.opensource.org/licenses/mit-license.php

    Usage example
    >>> import whois
    >>> domain = whois.query('google.com')
    >>> print(domain.__dict__)

    {'expiration_date': datetime.datetime(2020, 9, 14, 0, 0), 'last_updated': datetime.datetime(2011, 7, 20, 0, 0), 'registrar': 'MARKMONITOR INC.', 'name': 'google.com', 'creation_date': datetime.datetime(1997, 9, 15, 0, 0)}

    >>> print(domain.name)
    google.com

    >>> print(domain.expiration_date)
    2020-09-14 00:00:00

"""
from ._1_query import do_query
from ._2_parse import do_parse, TLD_RE
from ._3_adjust import Domain
from .exceptions import UnknownTld, FailedParsingWhoisOutput, UnknownDateFormat, WhoisCommandFailed


CACHE_FILE = None
SLOW_DOWN = 0


def query(domain, force=0, cache_file=None, slow_down=0, ignore_returncode=0):
    """
        force=1             <bool>      Don't use cache.
        cache_file=<path>   <str>       Use file to store cache not only memory.
        slow_down=0         <int>       Time [s] it will wait after you query WHOIS database. This is useful when there is a limit to the number of requests at a time.
    """
    assert isinstance(domain, str), Exception('`domain` - must be <str>')
    cache_file = cache_file or CACHE_FILE
    slow_down = slow_down or SLOW_DOWN
    domain = domain.lower().strip().rstrip('.')  # Remove the trailing dot to support FQDN.
    d = domain.split('.')

    if d[0] == 'www':
        d = d[1:]
    if len(d) == 1:
        return None

    if domain.endswith('.ac.uk') and len(d) > 2:
        tld = 'ac_uk'
    elif domain.endswith('co.il') and len(d) > 2:
        tld = 'co_il'
    elif domain.endswith('.co.jp') and len(d) > 2:
        tld = 'co_jp'
    elif domain.endswith('.com.au') and len(d) > 2:
        tld = 'com_au'
    elif domain.endswith('com.tr') and len(d) > 2:
        tld = 'com_tr'
    elif domain.endswith('global'):
        tld = 'global_'
    elif domain.endswith('.id'):
        tld = 'id_'
    elif domain.endswith('.in'):
        tld = 'in_'
    elif domain.endswith('.is'):
        tld = 'is_'
    elif domain.endswith('.name'):
        d[0] = 'domain=' + d[0]
        tld = d[-1]
    elif domain.endswith('.xn--p1ai'):
        tld = 'ru_rf'
    else:
        tld = d[-1]

    if tld not in TLD_RE.keys():
        print(f'Unknown TLD: .{tld}\nValid TLDs: ', end="")
        for valid_tld in sorted(list(TLD_RE.keys())):
            print(f'.{valid_tld}', end=" ")
        raise UnknownTld(f"The TLD .{tld} is currently not supported by this package.")

    while 1:
        pd = do_parse(do_query(d, force, cache_file, slow_down, ignore_returncode), tld)
        if (not pd or not pd['domain_name'][0]) and len(d) > 2:
            d = d[1:]
        else:
            break

    return Domain(pd) if pd['domain_name'][0] else None
