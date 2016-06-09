import os


def save_group_list_in_file(file_name, location, meetup_groups):
    """
    Create file with the results
    :param file_name: String, name of the file to be cerated. Ie "colombia.txt"
    :param location: String, name of the location the search was done. Ie. "Colombia"
    :param meetup_groups: List of groups that were retrieved from the meetup api
    """
    with open("result" + os.sep + file_name, 'w') as f:
        f.write(" =================== %s Python groups ================= \n" % location)
        for group in meetup_groups:
            f.write('{:10s} {:20s} {:5s} {:10s} \n'.format(group['country_name'],
                                                           group['city'],
                                                           str(group['members']),
                                                           group['name']))
