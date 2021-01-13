from pprint import pprint
import operator
import xml.etree.ElementTree as ET
def reader(address):
    parser = ET.XMLParser(encoding='utf-8')
    tree=ET.parse('newsafr.xml', parser) 
    root = tree.getroot()
    new_data = root.findall('channel/item')
    return new_data

data_from_file=reader('newsafr.json')    

def sorter(data_from_file, number):
    counter = {}
    for new in data_from_file:
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
    return result

data_from_file_two=sorter(data_from_file, 6)

def top(data_from_file_two):    
    count=0 
    for i in data_from_file_two:
        count+=1
        if count<=10:
            return i[0]

reader('newsafr.json')            
sorter(data_from_file, 6)    
top(data_from_file_two)               