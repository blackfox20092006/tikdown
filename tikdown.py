import os
import threading
from func import *
banner = '''
 ███████████ █████ █████   ████ ██████████ █████ █████ ███████████
░█░░░███░░░█░░███ ░░███   ███░ ░░███░░░░░█░░███ ░░███ ░█░░░███░░░█
░   ░███  ░  ░███  ░███  ███    ░███  █ ░  ░░███ ███  ░   ░███  ░ 
    ░███     ░███  ░███████     ░██████     ░░█████       ░███    
    ░███     ░███  ░███░░███    ░███░░█      ███░███      ░███    
    ░███     ░███  ░███ ░░███   ░███ ░   █  ███ ░░███     ░███    
    █████    █████ █████ ░░████ ██████████ █████ █████    █████   
   ░░░░░    ░░░░░ ░░░░░   ░░░░ ░░░░░░░░░░ ░░░░░ ░░░░░    ░░░░░      v1.0   
                                                                  
                                    Author: t.me/blackfox2006/
'''
def download(list_url, num):
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
                print(f'\x1b[32mTHREAD {num} : Đã tải thành công {url} ==> {name}!\x1b[0m [{count}/{total}]')
                count += 1
            f.close()
        except:
            rfnow()
            print(f'\x1b[31mTHREAD {num} : Link \x1b[32m{url}\x1b[31m bị lỗi!\x1b[0m')
    driver.close()
if __name__ == '__main__':
    print(f'\x1b[36m{banner}\n\n')
    print('1. Tải hàng loạt video Tiktok (link trong links.txt) \n2. Lọc video Beta Tiktok ')
    choice = int(input('Mode : '))
    if choice == 1:
        with open('links.txt', 'r') as f:
            links = f.readlines()
        links = [i.replace('\n', '') for i in links]
        total = len(links)
        num_threads = int(input('Threads : '))
        data, temp = data_dividing(links, num_threads)
        count = 1
        threads = []
        for i in range(num_threads):
            threads.append(threading.Thread(target=download, args=(data[i], i+1,)))
        for i in threads:
            i.start()
        for i in threads:
            i.join()
        download(temp, 1)
        print(f'Successful downloads : {count}')
    elif choice == 2:
        path = input('Video folder path: ')
        if not os.path.exists(path):
            print(f'Not found {path}!')
            exit(-1)
        else:
            os.chdir(path)
            files = os.listdir()
            for i in files:
                if not i.endswith('mp4'):
                    files.remove(i)
            data, temp = data_dividing(files, 10)
            threads = []
            for i in range(10):
                threads.append(threading.Thread(target=beta, args=(data[i], i+1,)))
            for i in range(10):
                threads[i].start()
            for i in threads:
                i.join()
            beta(temp, 1)