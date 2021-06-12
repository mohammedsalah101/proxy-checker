''' Скрипт проверяет работоспособность прокси из списка proxy_list.txt и записывает рабочие в working_proxy.txt '''
import requests
from multiprocessing import Pool


proxies = {'http': None, 'https': None}


def check_proxy(proxy):
    ''' Проверяем работоспособность конкретного прокси '''
    url = 'https://httpbin.org/get' 
    proxies['http'], proxies['https'] = proxy, proxy
    try:
        requests.get(url, proxies = proxies, timeout=5)
        print(f'Successfully: {proxy}')
        with open('working_proxy.txt', 'a') as New_file:
            New_file.write(proxy + '\n')
    except:
        print(f'Failed: {proxy}')


if __name__ == '__main__':
    # получаем список прокси в формате http://ip:port
    with open('proxy_list.txt', 'r') as File:
        proxy_list = File.read().split('\n')
        http_proxy_list = list(map(lambda f: 'http://' + f, proxy_list))

    # выполняем параллельно проверку списка прокси
    with Pool() as p:
        p.map(check_proxy, http_proxy_list)

    print('Check complete!')
