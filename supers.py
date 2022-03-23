import requests

chars = []


def name_search(name):
    url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
    res_name = requests.get(url)
    return res_name.json()['results'][0]['id']


def id_stats(char_id):
    url = f"https://superheroapi.com/api/2619421814940190/{char_id}/powerstats"
    res_id = requests.get(url)
    return chars.append(res_id.json())


def int_comp(chars_ist: list):

    ints = []

    for char in chars_ist:
        for a, b in char.items():
            if a == 'intelligence':
                ints.append(int(b))

    hi_int = sorted(ints)[-1]

    for char in chars_ist:
        if char['intelligence'] == str(hi_int):
            print(f"name: {char['name']}\nintelligence: {char['intelligence']}\n+++++")


if __name__ == '__main__':

    id_stats(name_search('Hulk'))
    id_stats(name_search('Captain America'))
    id_stats(name_search('Deadpool'))
    id_stats(name_search('MODOK'))
    id_stats(name_search('Thanos'))

    int_comp(chars)
