def type2(dict_link, i):
    title_dict = dict()
    for name in dict_link.keys():
        title_dict[name] = list()
        title_dict[name].append(name)
        title_dict[name].append(str('unit ' + str(i)))
    return title_dict
                                
                        
                                    
        
        
