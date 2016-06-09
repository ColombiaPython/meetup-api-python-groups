
def process_group_list(python_groups):
    """
    Process group list so the duplicated groups are removed and the list is sorted from most to less members
    :param python_groups: List, python groups returned from meetup api
    :return: List, list of python groups
    """

    # remove duplicated groups
    list_of_unique_dicts = [dict(y) for y in set(tuple(x.items()) for x in python_groups)]

    # sort by members from less to most members
    list_of_unique_dicts.sort(key=lambda x: x["members"])

    # sort by members from most to less members
    list_of_unique_dicts.reverse()

    return list_of_unique_dicts


def print_group_list(python_groups):
    """
    Print group list to be completely readable
    :param python_groups: List, python groups returned from meetup api
    """
    for python_group in python_groups:
        print('{:10s} {:20s} {:5s} {:10s}'.format(python_group['country_name'],
                                                  python_group['city'],
                                                  str(python_group['members']),
                                                  python_group['name']))
