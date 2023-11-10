import requests
import json
from time import sleep

# the path in which your AES keys that are generated will be stored. Keep empty to save in current path you run the code in.
path = "" 

response = requests.get('https://fortnite-api.com/v2/aes')
json = response.json()['data']
main = json['mainKey']
dynamic = response.json()['data']['dynamicKeys']

v = requests.get('https://fortnitecentral.genxgames.gg/api/v1/aes')
version = v.json()['version']

f= open(f'{path}v{version} AES KEYS.txt', 'w')

f.write(f'Main AES Key for v{version}:\n0x{main}\n\n\nDynamic Keys:\n')

for dynamickeys in dynamic:
    key = dynamickeys['key']
    pak = dynamickeys['pakFilename']
    f.write(f'{pak}: \n0x{key}\n\n')

x = len(dynamic)

f.write(f'''
Total Dynamic Keys: {x}
-----------------------------
https://twitter.com/xdFNLeaks
''') # you can remove https://twitter.com/xdFNLeaks if u want

print(f'{x} keys detected for v{version}! saved to path.')
f.close()
print("This program will now close in 3 seconds...")
sleep(3)
exit()
