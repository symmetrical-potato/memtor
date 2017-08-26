import json

from stats.stats import get_all_stats

with open('pn60.json') as file:
    data = json.load(file)

stat = get_all_stats(data[1:])

with open('pn6_stat.json', 'w', encoding='utf=8') as file:
    json.dump(stat, file, ensure_ascii=False)
