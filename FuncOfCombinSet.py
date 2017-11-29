def GetAliasesSetNew(all_router_list):
    per_set_count = 0
    while True:
        set_count = len(all_router_list)
        if set_count==per_set_count:
            break
        per_set_count = set_count
        remove_values = []
        remove_count = 0
        for i,item in enumerate(all_router_list):
            temp_set = item.copy()
            for index in range(i+1,set_count):
                if len(item&all_router_list[index])>0:
                    temp_set |= all_router_list[index]
                    if all_router_list[index] in remove_values:
                        pass
                    else:
                        remove_values.append(all_router_list[index])
            if len(remove_values)>remove_count:
                if item in remove_values:
                    pass
                else:
                    remove_values.append(item)
                remove_count = len(remove_values)
                all_router_list.append(temp_set)
        for item in remove_values:
            all_router_list.remove(item)