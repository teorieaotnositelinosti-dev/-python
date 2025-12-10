import xml.etree.ElementTree as ET

xml_file = 'currency.xml'


with open(xml_file, 'r', encoding='windows-1251') as f:
    xml_content = f.read()

root = ET.fromstring(xml_content)


currency_dict = {}


for valute in root.findall('Valute'):
    name = valute.find('Name').text
    char_code = valute.find('CharCode').text
    
    
    currency_dict[name] = char_code


print("Словарь 'Name - CharCode' (Вариант 10):")
for name, code in currency_dict.items():
    print(f"{name}: {code}")