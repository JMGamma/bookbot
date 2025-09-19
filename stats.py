def word_count(text):
    count = len(text.split())
    return count

def character_count(text):
    text = text.lower()
    character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',',','.',"'","?",'!','æ','â','ê','ë','ô']
    dict = {}
    for c in character:
        count = text.count(c)
        dict[c] = count
    return dict

def sort_on(items):
    return items['num']

def dict_sort(dict):
    dicts = []
    for character in dict:
        temp = {}
        temp['name'] = character
        temp['num'] = dict[character]
        dicts.append(temp)
    dicts.sort(reverse=True, key=sort_on)
    return dicts