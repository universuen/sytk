from sytk import EzParser

if __name__ == '__main__':
    html = open('test.html', 'r', encoding='utf8').read().encode()
    ezp = EzParser(html)
    tags = ezp.find_all(args={'href': None})
    for i in tags:
        print(i['href'])
    print(ezp.text)


