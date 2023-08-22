import os
import datetime
from time import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import requests
import threading
def fnow():
    current_time = datetime.datetime.now()
    print(f'\x1b[94m[{current_time}] \x1b[0m', end='')
def rfnow():
    current_time = datetime.datetime.now()
    print(f'\x1b[31m[{current_time}] \x1b[0m', end='')
def data_dividing(a, m):
    try:
        n = len(a) // m
        data = []
        for i in range(m):
            data.append([])
        for i in range(m):
            data[i] = a[:n+1]
            del a[:n+1]
    except:
        temp = a
    if a != []:
        temp = a
    return data, temp
def download(list_url):
    global count
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-features=NetworkService')
    options.add_argument('--log-level=3')
    options.add_argument('--silent')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-dev-tools")
    driver = webdriver.Chrome(options=options)
    for url in list_url:
        name = os.getcwd() + f'\\downloads\\{count}.mp4'
        driver.get('https://snaptik.com/')
        e = driver.find_element(By.NAME, 'url').send_keys(url)
        e = driver.find_element(By.NAME, 'url').send_keys(Keys.ENTER)
        sleep(2)
        try:
            WebDriverWait(driver, timeout=0.2)
            sleep(2)
            download_button = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[2]/a[1]')
            download_url = download_button.get_attribute("href")
            data = requests.get(download_url)
            with open(name, 'wb') as f:
                f.write(data.content)
                fnow()
                print(f'\x1b[32mĐã tải thành công {url} ==> {name}!\x1b[0m [{count}/{total}]')
                count += 1
            f.close()
        except:
            rfnow()
            print(f'\x1b[31mLink \x1b[32m{url}\x1b[31m bị lỗi!\x1b[0m')
    driver.close()
if __name__ == '__main__':
    with open('links.txt', 'r') as f:
        links = f.readlines()
    links = [i.replace('\n', '') for i in links]
    total = len(links)
    num_threads = int(input('Threads : '))
    data, temp= data_dividing(links, num_threads)
    count = 1
    threads = []
    for i in range(num_threads):
        threads.append(threading.Thread(target=download, args=(data[i],)))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    while True:
        if len(temp) % num_threads == 0:
            data, temp = data_dividing(temp, num_threads)
            for i in range(num_threads):
                threads.append(threading.Thread(target=download, args=(data[i],)))
            for i in threads:
                i.start()
            for i in threads:
                i.join()
        else:
            num_threads -= 1
    print(f'successful downloads : {count}')