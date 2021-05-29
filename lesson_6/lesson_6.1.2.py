import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
req = (el for el in requests.get(url).text.strip().split('\n'))

list_turpls = []
spamer = {}
for el in req:
    el = el.split(' ')
    remote_addr = el[0]
    request_type = el[5][1:]
    requested_resourse = el[6]
    list_turpls.append((remote_addr, request_type, requested_resourse))
    if el[0] not in spamer:
        spamer[el[0]] = 1
    else:
        spamer[el[0]] += 1

spamer = dict([max(spamer.items(), key=lambda k_v: k_v[1])])
print(list_turpls)
print(f'Спамер: id: {list((i for i in spamer.keys()))}, количество запросов: {list((i for i in spamer.values()))}')
