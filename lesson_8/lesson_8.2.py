import requests
import re
import time

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
start = time.time()
logs = (log for log in requests.get(url).text.strip().split('\n'))
for row in logs:
    parser_row = re.findall(r'(.[^\s]*).*(\d\d/.*\+\d{4}).*\"([A-Z]{3,})\s(/[a-z]*/.*_\d+).*\s(\d+)\s(\d+)', row)[0]
    print(parser_row)
    
time_generator = time.time() - start
'''Решение для файлов размером больше чем ОЗУ, правильно я понимаю?
Не очень нравится что parser_row - список с одним кортежем.'''

start = time.time()
logs = requests.get(url).text.strip()
parser_row = re.findall(r'(.[^\s]*).*(\d\d/.*\+\d{4}).*\"([A-Z]{3,})\s(/[a-z]*/.*_\d+).*\s(\d+)\s(\d+)', logs)
print(*parser_row, sep='\n')

print(time.time() - start)
print('time_generator', time_generator)
''' Единственная заковырка, которую выявил: запросы "GET" и редко бывает "HEAD".
Работает генератор судя по всему немного быстрее, чем весь файл обрабатывать'''
