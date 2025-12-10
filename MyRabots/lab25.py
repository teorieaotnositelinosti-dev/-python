import csv

target_file = 'books.csv'

unique_tags = set()
books_popularity = []

with open(target_file, 'r', encoding='windows-1251') as csvfile:
    table = csv.DictReader(csvfile, delimiter=';')
    
    for row in table:
        
        tags_raw = row.get('Жанр книги', '') 
        
        parts = [t.strip() for t in tags_raw.split('#') if t.strip()]
        unique_tags.update(parts)
        
        
        try:
            downloads = int(row['Кол-во выдач'])
        except ValueError:
            downloads = 0
            
        books_popularity.append({
            'title': row['Название'],
            'author': row['Автор'],
            'downloads': downloads
        })


print(f"Всего уникальных тегов: {len(unique_tags)}")
print("Список тегов (первые 20):", list(unique_tags)[:20])
print("-" * 30)


top_20 = sorted(books_popularity, key=lambda x: x['downloads'], reverse=True)[:20]

print("Топ-20 самых популярных книг:")
for i, book in enumerate(top_20, 1):
    print(f"{i}. {book['title']} ({book['author']}) - Выдач: {book['downloads']}")