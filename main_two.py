from pprint import pprint
import operator
import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8')
tree=ET.parse('newsafr.xml', parser)
root = tree.getroot()


new_data = root.findall('channel/item')
# print(len(new_data))
counter = {}
for new in new_data:
    finder = new.find('description')
    text = finder.text
    news=list(text.split())
    count=0
    for word in news: 
        if len(word)>6:
            if word in counter:
                count+=1
                counter[word] = int(count)
            else:
                count=1
                counter[word] = count
result=sorted(counter.items(), key=operator.itemgetter(1), reverse=True) 
count=0 
for i in result:
    count+=1
    if count<=10:
        print(i[0])