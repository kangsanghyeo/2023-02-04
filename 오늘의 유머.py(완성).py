import requests

headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('subject"><a href="')

for i in range(count):
      pos1 = source_data.find('"subject"><a href="')+ len('"subject"><a href="')
      source_data = source_data[pos1:]

      pos2 = source_data.find('=1" target="')
      a_data = source_data[: pos2]

      pos3 = source_data.find('=1" target="_top">')+ len('=1" target="_top">')
      source_data = source_data[pos3:]

      pos4 = source_data.find('</a><span class=')
      b_data = source_data[: pos4]

      source_data = source_data[pos4+1:]
      print(i+1, a_data, b_data)
