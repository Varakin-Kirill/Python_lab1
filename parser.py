from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
def parser(url):
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    filtered = []
    all_inf = []
    soup = BeautifulSoup(page.text, "html.parser")# передаем страницу в bs4
    all_inf=soup.findAll('span', itemprop="fio")# находим  контейнер с нужным классом
    for data in all_inf: # проходим циклом по содержимому контейнера
        if (data.find(target='_blank') is not None):
            filtered.append(data.text)
    f = open('surnames.txt','w') # создаем текстовый докумет для записи фио
    for data in filtered: # проходимся по отфильтрованной информации
        if (data[1] == "В"): # если первая буква в, то записать в файл
            f.write(data)
