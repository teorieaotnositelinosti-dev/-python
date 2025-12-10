import csv
import random

target_file = 'books.csv'
output_file = 'biblio.txt'


all_books = []

with open(target_file, 'r', encoding='windows-1251') as csvfile:
    table = csv.DictReader(csvfile, delimiter=';')
    for row in table:
        all_books.append(row)


random_books = random.sample(all_books, 20)

print(f"Генерация библиографических ссылок в файл {output_file}...")

with open(output_file, 'w', encoding='utf-8') as f:
    for i, book in enumerate(random_books, 1):
        author = book['Автор']
        title = book['Название']
        
        
        try:
            year = book['Дата поступления'].split(' ')[0].split('.')[2]
        except:
            year = "н.д."
            
        
        ref_string = f"{i}. {author}. {title} - {year}\n"
        f.write(ref_string)

print("Готово.")