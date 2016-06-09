
from app.utils.meetup_utils import MeetupUtils
from app.constants import COLOMBIA_PLACES_FILTERS, LATAM_PLACES_FILTERS, KEYWORD_FILTERS, LOCATION_CODES
from app.utils.file_utils import save_group_list_in_file
from app.utils.list_utils import process_group_list, print_group_list
from settings import MEETUP_API_KEY


def process_python_group_by_location(location_code):
    """
    Get python groups fron the given location code and create a xt file with the results
    :param location_code: String, code of the location the search will be done. Ie "LATAM"
    """
    # get info from meetup api
    print("Getting info about Colombia Python meetups...")
    colombia_python_groups = get_location_based_python_groups(location_code)

    location_name = LOCATION_CODES[location_code]
    print(" =================== %s Python groups =================" % location_name)
    print_group_list(colombia_python_groups)

    file_name = location_name + ".txt"
    print("Creating %s file" % file_name)
    save_group_list_in_file(file_name, location_name, colombia_python_groups)


def get_location_based_python_groups(location_filter_code):
    """
    Select the filters to be added depending of the location filter code
    :param location_filter_code: String, code of the location the search will be done. Ie "LATAM"
    :return List: Groups that were found in the meetup api
    """
    if location_filter_code == "LATAM":
        return get_python_groups(LATAM_PLACES_FILTERS)
    elif location_filter_code == "CO":
        return get_python_groups(COLOMBIA_PLACES_FILTERS)


def get_python_groups(places_filters):
    """
    Get groups from the meetup api based on the given filters
    :param places_filters: List, dicts of country codes and cities to be filtered
    :return List: Groups that were found in the meetup api
    """
    # create meetup api instance with defined api key
    meetup_utils_instance = MeetupUtils(MEETUP_API_KEY)

    # get python groups from meetup dot com
    retrieved_python_groups = meetup_utils_instance.get_find_groups(places_filters, KEYWORD_FILTERS)

    # remove duplicates and sort list
    return process_group_list(retrieved_python_groups)
