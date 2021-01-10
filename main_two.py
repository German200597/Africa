from pprint import pprint
import operator
import xml.etree.ElementTree as ET
def reader():
    parser = ET.XMLParser(encoding='utf-8')
    tree=ET.parse('newsafr.xml', parser) 
    root = tree.getroot()
    global new_data
    new_data = root.findall('channel/item')
# print(len(new_data))
def sorter():
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
    global result                
    result=sorted(counter.items(), key=operator.itemgetter(1), reverse=True) 
def top():    
    count=0 
    for i in result:
        count+=1
        if count<=10:
            print(i[0])
reader()            
sorter()    
top()               