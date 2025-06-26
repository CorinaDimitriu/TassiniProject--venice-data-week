import re

with open("tassini_clean\\tassini_pages_without_index.txt", 'r', encoding='utf-8') as f:
    text = f.read()


""" #Segement per page
page_pattern = r'[=]+?.+?[=]+?\n([\s\S]*?)(?=[=]+?.+?[=]+?)'
matches = re.findall(page_pattern, text)

print(matches[0]) """

#For each page, segement per index (there will be still within certain indexes two or more places).
#Each entity is linked with page number(s)

entity_pattern_1 = r'[A-Z]\s+?indice\s+?\n([\s\S]+?)(?=[A-Z]\s+?indice)'
matches = re.findall(entity_pattern_1, text)

#print(matches[1])


#Separate inside the matches if there are two of them
all_entities = []

for match in matches:
    entity_pattern_2 = r'(.+\(.+\)[\s\S]+?\.[\s]*\n)([\s\S]+?)(?=.+\(.+\)[\s\S]+?\.[\s]*\n|\Z)'
    place_matches = re.findall(entity_pattern_2, match)

    for place_match in place_matches:
        with open("out/text_with_places.txt", "a", encoding='utf-8') as text_file:
            text_file.write("%" + place_match[0].strip() + "%\n")
            text_file.write(place_match[1].strip() + "\n&\n")

