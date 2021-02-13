import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'O site pudim não esta acessivel')
else:
    print(f'O site pudim esta acessivel')
    print(site.read())

