import re

with open('task1-en.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print("=" * 60)
print("ВАРИАНТ 10")
print("=" * 60)

print("\n1. СЛОВА, ПОСЛЕ КОТОРЫХ СТОИТ ТОЧКА:")
print("-" * 40)

pattern_words_with_dot = r'\b[A-Za-z][A-Za-z]*\b(?=\.(?!\d))'
words_with_dot = re.findall(pattern_words_with_dot, text)

for i in range(0, len(words_with_dot), 10):
    print(', '.join(words_with_dot[i:i+10]))

print(f"\nВсего найдено: {len(words_with_dot)} слов")

print("\n\n2. ДРОБНЫЕ ЧИСЛА:")
print("-" * 40)

pattern_fractions = r'(?<!\w)(\d+[./=]\d+)(?!\w)'
fractions = re.findall(pattern_fractions, text)

pattern_decimals = r'(?<!\w)\d+\.\d+(?!\w)'
decimals = re.findall(pattern_decimals, text)

all_fractions = list(set(fractions + decimals))
all_fractions.sort(key=lambda x: float(x.replace('/', '.').replace('=', '.')))

for i in range(0, len(all_fractions), 8):
    print(', '.join(all_fractions[i:i+8]))

print(f"\nВсего найдено: {len(all_fractions)} дробных чисел")

print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ:")
print("=" * 60)

print("\nПримеры слов с точкой в контексте:")
pattern_context_words = r'(\b[A-Za-z]+\b\.)'
matches = re.finditer(pattern_context_words, text)
for i, match in enumerate(matches):
    if i >= 10:  
        break
    start = max(0, match.start() - 20)
    end = min(len(text), match.end() + 20)
    context = text[start:end].replace('\n', ' ')
    print(f"  ...{context}...")

print("\nПримеры дробных чисел в контексте:")
pattern_context_fractions = r'(\d+[./=]\d+|\d+\.\d+)'
matches = re.finditer(pattern_context_fractions, text)
for i, match in enumerate(matches):
    if i >= 10:  
        break
    start = max(0, match.start() - 30)
    end = min(len(text), match.end() + 30)
    context = text[start:end].replace('\n', ' ')
    print(f"  ...{context}...")

print("\n" + "=" * 60)
print("СТАТИСТИКА:")
print("=" * 60)

from collections import Counter
words_counter = Counter(words_with_dot)
print(f"\nСамые частые слова с точкой:")
for word, count in words_counter.most_common(10):
    print(f"  {word}. - {count} раз")

print(f"\nТипы дробных чисел:")
slash_fractions = [f for f in all_fractions if '/' in f]
equal_fractions = [f for f in all_fractions if '=' in f]
dot_fractions = [f for f in all_fractions if '.' in f and '/' not in f and '=' not in f]

print(f"  Через слэш (/): {len(slash_fractions)}")
print(f"  Через равно (=): {len(equal_fractions)}")
print(f"  Через точку (.): {len(dot_fractions)}")