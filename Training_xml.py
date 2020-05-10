import xml.etree.ElementTree as ET

tree = ET.parse(r"newsafr.xml")
root = tree.getroot()

titles = root.findall("channel/title")
descriptions = root.findall("channel/description")
categories = root.findall("channel/category")

items = tree.findall("channel/item")
titles2 = root.findall("channel/item/title")
descriptions2 = root.findall("channel/item/description")

new_list_of_words = []

# here I split the text in separated items

new_list_of_words.extend(descriptions[0].text.split(" "))
new_list_of_words.extend(categories[0].text.split(" "))
new_list_of_words.extend(titles[0].text.split(" "))

i = 0
while i < len(items):
    new_list_of_words.extend(titles2[i].text.split(" "))
    new_list_of_words.extend(descriptions2[i].text.split(" "))
    i = i + 1

# Here I count the number of identical items in the list. For this purpose I create a dictionary: key corresponds to a word, value corresponds to the number of times this word is repeated

dct = {}
for word in new_list_of_words:
    if len(word) > 6:
        lower_word = word.lower()
        if lower_word in dct.keys():
            dct[lower_word] = dct[lower_word] + 1
        else:
            dct[lower_word] = 1

# here I sort the list
list_d = list(dct.items())
list_d.sort(key=lambda i: i[1])

new_list = []
# here I append the 10 last elements of list_d to the new_list
i = 1
while i <= 10 and i <= len(list_d):
    new_list.append(list_d[-i])
    i = i + 1

print("Топ", len(new_list), "слов длиннее 6 символов:", "\n")
for i in new_list:
    print(i[0])



