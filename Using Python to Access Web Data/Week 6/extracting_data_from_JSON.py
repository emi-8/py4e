import urllib.request, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# https://py4e-data.dr-chuck.net/comments_42.json
# https://py4e-data.dr-chuck.net/comments_1728925.json

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
    info = json.loads(data)

    for item in info["comments"]:
        # print('Name', item['name'])
        total += int(item['count'])
        counter += 1

    print('Count:', counter)
    print('Sum:', total)