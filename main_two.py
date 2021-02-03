from pprint import pprint
import operator
import xml.etree.ElementTree as ET
def reader(address):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(address, parser) 
    root = tree.getroot()
    new_data = root.findall('channel/item')
    return new_data

data_from_file = reader('newsafr.json')

def sorter(data_from_file, max_number_of_letters):
    counter = {}
    for new in data_from_file:
        finder = new.find('description')
        text = finder.text
        news = list(text.split())
        count = 0
        for word in news: 
            if len(word) > number_of_letters:
                if word in counter:
                    counter[word] = counter[word] + 1
                else:
                    counter[word] = 1               
    result=sorted(counter.items(), key=operator.itemgetter(1), reverse=True) 
    return result

data_from_file_two=sorter(data_from_file, 6)

def top(data_from_file_two, number_of_top_words):    
    count = 0 
    for i in data_from_file_two:
        count += 1
        if count <= number_of_top_words:
            print(i[0])

reader('newsafr.json')            
sorter(data_from_file, 6)    
top(data_from_file_two, 10)               