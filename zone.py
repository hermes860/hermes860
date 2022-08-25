#!/usr/bin/python3
import dns.query
import dns.zone

fzone = 'nsztml.digi.ninja'
szone = 'zonetransfer.me'

tr = dns.zone.from_xfr(dns.query.xfr(fzone, szone))
domain = tr.nodes.keys()
sorted(domain)

for n in domain:
    print(tr[n].to_text(n))














######### Automaticaly Created Script /##########
