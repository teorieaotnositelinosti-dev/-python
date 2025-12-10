import re
import csv

with open('task3.txt', 'r', encoding='utf-8') as f:
    content = f.read()

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
date_pattern = r'^\d{4}-\d{2}-\d{2}$'
url_pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/\S*)?$'
name_pattern = r'^[A-Z][a-z]+$'
id_pattern = r'^\d+$'

lines = content.strip().split('\n')

records = []

for line in lines:
    elements = line.strip().split()
    
    if not elements:
        continue
    
    record = {'ID': '', 'Name': '', 'Email': '', 'Date': '', 'URL': ''}
    
    for elem in elements:
        if re.match(id_pattern, elem):
            record['ID'] = elem
            break
    
    for elem in elements:
        if re.match(date_pattern, elem):
            record['Date'] = elem
            break
    
    for elem in elements:
        if '@' in elem and '.' in elem and not elem.startswith('http'):
            
            if re.match(r'^[^@]+@[^@]+\.[^@]+$', elem):
                record['Email'] = elem
                break
    
    for elem in elements:
        if re.match(url_pattern, elem) or elem.startswith('www.'):
            if elem.startswith('www.'):
                record['URL'] = 'http://' + elem
            else:
                record['URL'] = elem
            break
    
    for elem in elements:
        if (re.match(name_pattern, elem) and 
            not elem.startswith('http') and 
            '@' not in elem and
            not re.match(date_pattern, elem) and
            not re.match(id_pattern, elem)):
            record['Name'] = elem
            break
    
    if all(record.values()):
        records.append(record)

if len(records) < 100:
    
    all_elements = content.split()
    
    ids = []
    names = []
    emails = []
    dates = []
    urls = []
    
    for elem in all_elements:
        if re.match(id_pattern, elem):
            ids.append(elem)
        elif re.match(date_pattern, elem):
            dates.append(elem)
        elif '@' in elem and '.' in elem and not elem.startswith('http'):
            emails.append(elem)
        elif re.match(url_pattern, elem) or elem.startswith('www.'):
            if elem.startswith('www.'):
                urls.append('http://' + elem)
            else:
                urls.append(elem)
        elif re.match(name_pattern, elem) and elem not in ['http', 'https']:
            names.append(elem)
    
    min_len = min(len(ids), len(names), len(emails), len(dates), len(urls))
    
    records = []
    for i in range(min_len):
        record = {
            'ID': ids[i],
            'Name': names[i],
            'Email': emails[i],
            'Date': dates[i],
            'URL': urls[i]
        }
        records.append(record)

records.sort(key=lambda x: int(x['ID']))

# Если это не заработает я повешусь на шнурках от кросовок
with open('task3_sorted.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID', 'Name', 'Email', 'Date', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for record in records:
        writer.writerow(record)

print(f"Создан файл task3_sorted.csv с {len(records)} записями")
print("\nПримеры записей:")
for i in range(min(10, len(records))):
    print(f"{records[i]}")