import meetup.api


class MeetupUtils:

    def __init__(self, api_key):
        self.__client__ = meetup.api.Client(api_key)

    def get_find_groups(self, places_filters, keyword_filters):
        found_places = []
        for place in places_filters:
            find_group_filter = {'country': place['country'], 'location': place['location'], 'text': 'python',
                                 "distance": 100}
            python_groups = self.__client__.GetFindGroups(find_group_filter)
            for python_group in python_groups:
                for keyword_filter in keyword_filters:
                    # if the keyword is in the group name, the group is added to the list to be returned
                    if keyword_filter in python_group.name:
                        found_places.append({
                            'country_code': python_group.country,
                            'country_name': python_group.localized_country_name,
                            'city': python_group.city,
                            'members': python_group.members,
                            'name': python_group.name,
                        })
        return found_places
