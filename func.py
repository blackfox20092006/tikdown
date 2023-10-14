import datetime
from time import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import requests
import moviepy.editor as mp
import os
def fnow():
    current_time = datetime.datetime.now()
    print(f'\x1b[94m[{current_time}] \x1b[0m', end='')
def rfnow():
    current_time = datetime.datetime.now()
    print(f'\x1b[31m[{current_time}] \x1b[0m', end='')
def data_dividing(a, m):
    data = []
    temp = []
    try:
        n = len(a) // m
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
def beta(files, thread_num):
    for i in files:
        try:
            video = mp.VideoFileClip(i)
            duration = video.duration
            video.close()
            if duration < 60:
                os.remove(i)
                print(f'THREAD {thread_num} : {i} [{duration}s] --> REMOVED !!')
            else:
                continue
        except:
            try:
                video.close()
                os.remove(i)
                print(f'THREAD {thread_num} : {i} [NO CONTENT FILE] --> REMOVED !!')
                continue
            except:
                try:
                    os.remove(i)
                    print(f'THREAD {thread_num} : {i} [NO CONTENT FILE] --> REMOVED !!')
                    continue
                except:
                    continue
