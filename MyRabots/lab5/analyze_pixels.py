import re
from collections import Counter

with open('task2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

pattern = r'\b\d+(\.\d+)?px\b'
matches = re.findall(pattern, html_content, re.IGNORECASE)
counter = Counter(matches)

html_report = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Анализ пиксельных значений в task2.html</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }
        .stats {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .stat-card {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border-left: 4px solid #667eea;
        }
        .stat-number {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }
        .stat-label {
            color: #666;
            font-size: 0.9em;
        }
        .values-table {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background: #667eea;
            color: white;
            padding: 12px;
            text-align: left;
        }
        td {
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        tr:nth-child(even) {
            background: #f9f9f9;
        }
        .value-cell {
            font-family: monospace;
            font-weight: bold;
            color: #e74c3c;
        }
        .count-cell {
            text-align: center;
            background: #f0f7ff;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 Анализ пиксельных значений в task2.html</h1>
        <p>Отчёт, сгенерированный с помощью регулярных выражений в Python</p>
    </div>
    
    <div class="stats">
        <h2>📊 Общая статистика</h2>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">""" + str(len(matches)) + """</div>
                <div class="stat-label">Всего значений</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">""" + str(len(counter)) + """</div>
                <div class="stat-label">Уникальных значений</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">""" + str(counter.most_common(1)[0][1] if counter else 0) + """</div>
                <div class="stat-label">Макс. частота</div>
            </div>
        </div>
    </div>
    
    <div class="values-table">
        <h2>📋 Все уникальные пиксельные значения</h2>
        <table>
            <tr>
                <th>Значение</th>
                <th>Количество</th>
                <th>Примеры использования</th>
            </tr>
"""

sorted_values = sorted(counter.items(), 
                      key=lambda x: float(re.search(r'\d+(\.\d+)?', x[0]).group()) 
                      if re.search(r'\d+(\.\d+)?', x[0]) else 0)

for value, count in sorted_values:

    examples = []
    for match in re.finditer(re.escape(value), html_content):
        start = max(0, match.start() - 30)
        end = min(len(html_content), match.end() + 30)
        context = html_content[start:end].replace('\n', ' ').replace('  ', ' ')
        if len(context) > 60:
            context = context[:60] + "..."
        examples.append(context)
        if len(examples) >= 2:
            break
    
    examples_html = "<br>".join([f"<code>{ex}</code>" for ex in examples[:2]])
    
    html_report += f"""
            <tr>
                <td class="value-cell">{value}</td>
                <td class="count-cell"><span style="background: #e74c3c; color: white; padding: 3px 8px; border-radius: 12px;">{count}</span></td>
                <td>{examples_html}</td>
            </tr>
"""

html_report += """
        </table>
    </div>
    
    <div class="footer">
        <p>Сгенерировано с помощью Python и регулярных выражений</p>
        <p>Шаблон регулярного выражения: <code>\\b\\d+(\\.\\d+)?px\\b</code></p>
    </div>
</body>
</html>
"""

with open('pixel_analysis_report.html', 'w', encoding='utf-8') as f:
    f.write(html_report)

print("✅ HTML-отчёт сохранён в файл: pixel_analysis_report.html")
print(f"📊 Найдено {len(matches)} значений в пикселях")
print(f"🔢 Уникальных значений: {len(counter)}")

import webbrowser
webbrowser.open('pixel_analysis_report.html')