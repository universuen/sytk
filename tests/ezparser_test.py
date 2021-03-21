from sytk import EzParser

if __name__ == '__main__':
    html = open('test.html', 'r', encoding='utf8').read()
    ezp = EzParser(html)
    tags = ezp.find_all('div', {'class': 'para'})
    for i in tags:
        print(i.text)

