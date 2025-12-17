import re

with open('task_add.txt', 'r', encoding='utf-8') as f:
    content = f.read()

patterns = {
    'Даты': [r'\s\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}', r'\s\d{4}[-/.]\d{1,2}[-/.]\d{1,2}'],
    'Email': [r'\s[\w.%+-]+@[\w.-]+\.[a-z]{2,}'],
    'URL': [r'\shttps?://[^\s]+', r'\shttp://[^\s]+\.[a-zA-Z]{2,}']
}

results = {}
for data_type, regex_list in patterns.items():
    results[data_type] = []
    for regex in regex_list:
        matches = re.findall(regex, content)
        results[data_type].extend(matches)

for data_type, matches in results.items():
    print(f"{data_type}:")
    for match in matches:
        print(f"  - {match.strip()}") 
    print()