import re

def type1(dict_link):
    title_dict = dict()
    for name in dict_link.keys():
        title_dict[name] = list()
        
        if re.search(r'unit\d+', name):
            unit = re.findall(r'(unit\d+)', name)[0]
            title = name.split(' ')
            title = title[3:]
            title = ' '.join(title)
            title_dict[name].append(title)
            title_dict[name].append(unit)
        else:
            title = name.split('-')
            title_dict[name].append(title[0].strip())
            title_dict[name].append(title[2].strip())
    return title_dict


dict_link = dict();
dict_link['st101 unit15 08 q Summarize 3'] = 1
dict_link['Average Friends Solution - Intro to Statistics - Teaser - Udacity'] = 1
dict_link['Coconuts 4 - CS373 Unit 2 - Udacity'] = 1
title_dict = type1(dict_link)
print title_dict.values()
