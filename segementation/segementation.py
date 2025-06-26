import re

with open("tassini\Toponomastica Veneziana_with_pages_delim.txt", 'r', encoding='utf-8') as f:
    text = f.read()


page_pattern = r'====================.+?====================\n([\s\S]*?)(?=====================.+?====================)'
matches = re.findall(page_pattern, text)

print(matches[0])
