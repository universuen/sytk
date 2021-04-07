
from sytk import EzParser
if __name__ == '__main__':
    html = open('tests\\test.html', 'r', encoding='utf8').read().encode()
    ezp = EzParser(html)
    tags = ezp.find_all(args={'href': None})
    for i in tags:
        print(i)
    print(ezp.text)


