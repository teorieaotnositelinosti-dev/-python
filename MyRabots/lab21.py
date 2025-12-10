import csv

target_file = 'books.csv'

count = 0

with open(target_file, 'r', encoding='windows-1251') as csvfile:
    
    table = csv.DictReader(csvfile, delimiter=';')
    
    for row in table:
        
        if len(row['Название']) > 30:
            count += 1

print(f"Количество записей, у которых Название длиннее 30 символов: {count}")