import re
from .exceptions import FailedParsingWhoisOutput
from . import tld_regexpr

TLD_RE = {}


def get_tld_re(tld):
    if tld in TLD_RE:
        return TLD_RE[tld]
    elif tld == "in":
        return "in_"
    v = getattr(tld_regexpr, tld)
    extend = v.get('extend')

    if extend:
        e = get_tld_re(extend)
        tmp = e.copy()
        tmp.update(v)
    else:
        tmp = v

    if 'extend' in tmp:
        del tmp['extend']

    TLD_RE[tld] = dict((k, re.compile(v, re.IGNORECASE) if isinstance(v, str) else v) for k, v in tmp.items())
    return TLD_RE[tld]


[get_tld_re(tld) for tld in dir(tld_regexpr) if tld[0] != '_']


def do_parse(whois_str, tld):
    r = {}

    if whois_str.count('\n') < 5:
        s = whois_str.strip().lower()
        if s == 'not found':
            return
        if s.startswith('no such domain'):
            # could feed startswith a tuple of strings of expected responses
            return
        if s.count('error'):
            return
        raise FailedParsingWhoisOutput(whois_str)

    # check the status of DNSSEC
    r['DNSSEC'] = False
    whois_dnssec = whois_str.split("DNSSEC:")
    if len(whois_dnssec) >= 2:
        whois_dnssec = whois_dnssec[1].split("\n")[0]
        if whois_dnssec.strip() == "signedDelegation" or whois_dnssec.strip() == "yes":
            r['DNSSEC'] = True

    # split whois_str to remove first IANA part showing info for TLD only
    whois_splitted = whois_str.split("source:       IANA")
    if len(whois_splitted) == 2:
        whois_str = whois_splitted[1]

    sn = re.findall(r'Server Name:\s?(.+)', whois_str, re.IGNORECASE)
    if sn:
        whois_str = whois_str[whois_str.find('Domain Name:'):]

    for k, v in TLD_RE.get(tld, TLD_RE['com']).items():
        if v is None:
            r[k] = ['']
        else:
            r[k] = v.findall(whois_str) or ['']

    return r
