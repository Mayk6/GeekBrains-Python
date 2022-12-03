import json
import requests
from bs4 import BeautifulSoup
from random import randint

headers = {
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
}


def pars_jokes():
    url = "https://www.anekdot.ru/release/anekdot/week/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    jokes_card = soup.find_all("div", class_="topicbox")
    jokes_dict = {}
    for jokes in jokes_card:
        if jokes.find("a", class_="auth") is not None:
            joke_author = jokes.find("a", class_="auth").text.strip()
            joke = jokes.find("div", class_="text").text.strip()
            id_joke = str(jokes.find('div', class_="btn2"))
            jokes_dict[id_joke[45:51]] = {
                "joke_author": joke_author,
                "joke": joke
            }
    with open("jokes_list.json", "w") as file:
        json.dump(jokes_dict, file, indent=4, ensure_ascii=False)


def random_joke():
    pars_jokes()
    jokes_list = []
    with open("jokes_list.json", "r") as file:
        jokes_dict = json.load(file)
        for i, j in jokes_dict.items():
            jokes_list.append(f'{j["joke"]} Автор: {j["joke_author"]}')
    return jokes_list[randint(0, 30)]


def pars_horoscope():
    url = "https://74.ru/horoscope/daily/"
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    horo_card = soup.find_all("article", class_="IGRa5")
    horo_dict = {}
    horo_id = 0
    for horo in horo_card:
        horo_name = horo.find("h3", class_="_4K6U+ _9dcVo").text.strip()
        horo_date = horo.find("p", class_="vpvdP _9TfK4").text.strip()
        horoscope = horo.find('div', class_="BDPZt KUbeq").text.strip()
        horo_dict[horo_id] = {
            "horo_name": horo_name,
            "horo_date": horo_date,
            "horoscope": horoscope
        }
        horo_id += 1
    with open("horo_list.json", "w") as file:
        json.dump(horo_dict, file, indent=4, ensure_ascii=False)


def get_horoscope(text):
    pars_horoscope()
    horo_list = []
    with open("horo_list.json", "r") as file:
        horo_dict = json.load(file)
        for i, j in horo_dict.items():
            horo_list.append(j["horo_name"])
            horo_list.append(j["horo_date"])
            horo_list.append(j["horoscope"])

    for i in range(len(horo_list)):
        if horo_list[i] == text:
            return f'Знак зодиака: {horo_list[i]}\n' \
                   f'Дата: {horo_list[i + 1]}\n' \
                   f'Гороскоп: {horo_list[i + 2]}'
    return 'Такого знака нет или допущена ошибка'
