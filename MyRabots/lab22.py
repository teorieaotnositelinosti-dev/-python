import csv

target_file = 'books.csv'
search_author = input("Введите имя автора (или часть имени) для поиска: ").lower()

print(f"\nРезультаты поиска (фильтр: год >= 2018):")
print("-" * 50)

with open(target_file, 'r', encoding='windows-1251') as csvfile:
    table = csv.DictReader(csvfile, delimiter=';')
    
    found = False
    for row in table:
        
        author = row['Автор'].lower()
        full_author = row['Автор (ФИО)'].lower()
        date_str = row['Дата поступления'] 
        
        
        try:
            
            year_str = date_str.split(' ')[0].split('.')[2]
            year = int(year_str)
        except:
            year = 0
            
        
        if (search_author in author or search_author in full_author) and year >= 2018:
            print(f"Автор: {row['Автор']}")
            print(f"Название: {row['Название']}")
            print(f"Год поступления: {year}")
            print("-" * 20)
            found = True

if not found:
    print("Книг данного автора за указанный период не найдено.")