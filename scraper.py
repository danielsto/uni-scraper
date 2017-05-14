import bs4
import requests
import simplejson as json

url = 'http://www.elmundo.es/especiales/ranking-universidades/grados.html'
req = requests.get(url)
status_code = req.status_code
git_calendar = []


def print_unis(list_unis):
    for uni in list_unis:
        print(uni)


def get_unis(rows, ranks):
    unis = []
    for item in rows:
        if item.contents[0].string not in ranks and item.contents[0].string \
                not in unis:
            unis.append(item.contents[0].string)
    return unis


def uni_to_dicts(unis):
    uni_data = {}
    for uni in unis:
        uni_data[uni] = 0
    return uni_data


def rank_to_points(rank):
    if rank == '1º':
        points = 5
    elif rank == '2º':
        points = 4
    elif rank == '3º':
        points = 3
    elif rank == '4º':
        points = 2
    elif rank == '5º':
        points = 1
    return points


if status_code == 200:
    html = bs4.BeautifulSoup(req.text, "html.parser")
    rankings = html.find_all('tbody')
    rows = html.find_all('td')
    filas = html.find_all('tr')
    ranks = ['1º', '2º', '3º', '4º', '5º']

unis = get_unis(rows, ranks)

uni_data = uni_to_dicts(unis)

for item in filas:
    position = item.contents[1].string
    uni = item.contents[3].string
    if position in ranks:
        points = rank_to_points(position)
        uni_data[uni] += points

with open('university_rankings.json', 'w') as fp:
    json_prueba = json.dumps(uni_data, sort_keys=True, ensure_ascii=False, indent=4, encoding='utf-8')
    fp.write(json_prueba)

with open('university_rankings.json', 'r') as fr:
    print(fr.read())