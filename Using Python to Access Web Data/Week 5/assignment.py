import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#  http://py4e-data.dr-chuck.net/comments_42.xml
#  http://py4e-data.dr-chuck.net/comments_1728924.xml
while True:
    counter = 0
    total = 0
    lst = list()

    url = input('Enter url: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    for count in counts:
        total += int(count.text)
        counter += 1

    print('Count:', counter)
    print('Sum:', total)