from app.python_groups import process_python_group_by_location


def process_python_groups():

    # process colombia info from meetup api
    process_python_group_by_location("CO")

    # process latam info from meetup api
    process_python_group_by_location("LATAM")


if __name__ == "__main__":
    process_python_groups()