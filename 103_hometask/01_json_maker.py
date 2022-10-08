import requests
import json

# Требуемые вакансии для поискового запроса
vacancies = 'python разработчик'

# Текст поискового запроса
search_text = ' and '.join(['\''+ elem + '\'' for elem in vacancies.split(', ')])

# url для парсинга
url = 'https://api.hh.ru/vacancies'

vacancy_list = []

page_counts = requests.get(url, params={'text': search_text, 'per_page': 10, }).json()['pages']

for i in range(page_counts):
    par = {'text': search_text, 'per_page':'10', 'page':i}
    temp_json = requests.get(url, params=par).json()
    for elem in temp_json['items']:        
        try:
            temp_json_2 = requests.get(url + '/' + str(elem['id'])).json()
            work_dict = {

                        }
            vacancy_list.append({
                                    "title":temp_json_2['name'],                                                                       # название вакансии
                                    "work experience":temp_json_2['experience']['name'],                                               # требуемый опыт
                                    "salary":str(str(temp_json_2['salary']['from']) + ' ' + str(temp_json_2['salary']['currency'])),   # заработная плата
                                    "region":temp_json_2['address']['city']                                                            # город
                                })
        except:
            pass
    print('Page ' + str(i) + ' from ' + str(page_counts) + ' is ready')

result = {'data':vacancy_list}

with open('vacancy.json', 'w', encoding="utf-8") as json_file:                                                                         # для корректного сохранения
    json.dump(result, json_file, ensure_ascii=False)                                                                                   # требуется кодирование utf-8