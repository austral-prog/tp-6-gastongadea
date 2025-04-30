def remove_elements(list_to_remove_elements):
    return list_to_remove_elements[1:4] + list_to_remove_elements[6:]


def add_elements(list_to_add_elements):
    #list_to_add_elements=['Pink']+list_to_add_elements+['Yellow']
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements


def is_empty(list_to_check):
    return list_to_check == []


def check_lists(list_to_compare1, list_to_compare2):
    return list_to_compare1[2:3]==list_to_compare2[2:3]


def list_of_lists(list_of_lists_to_modify):
    l2=[]
    l2.append(list_of_lists_to_modify[0][:3])
    l2.append(list_of_lists_to_modify[1][1:4])
    l2.append(list_of_lists_to_modify[2][-2:])
    return l2
