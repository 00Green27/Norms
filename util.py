__author__ = 'ehd'

def get_id_by_name(list, name):
    id = -1
    for element in list:
        if element[1] == name:
            id = element[0]

    return id
