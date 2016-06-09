import unittest
from app.python_groups import process_python_group_by_location, get_python_groups


class TestPythonGroups(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.__colombia_code__ = "CO"  # Colombia
        self.__latam_country_codes__ = [
            "AR",  # Argentina
            "BO",  # Bolivia
            "BR",  # Brazil
            "CL",  # Chile
            "EC",  # Ecuador
            "GT",  # Guatemala
            "HN",  # Honduras
            "MX",  # Mexico
            "PY",  # Paraguay
            "PE",  # Peru
            "UY",  # Uruguay
            "SV"   # El Salvador
        ]
        self.__latam_country_codes__.append(self.__colombia_code__)

    def test_get_all_python_groups(self):

        # process colombia info from meetup api
        process_python_group_by_location("CO")

        # process latam info from meetup api
        process_python_group_by_location("LATAM")

    def test_get_location_based_python_groups(self):

        # test retrieved group from colombia
        colombian_groups = get_python_groups("CO")
        for colombian_group in colombian_groups:
            self.assertEqual(colombian_group['country_code'], self.__colombia_code__)

        # test retrieved group from colombia
        latam_groups = get_python_groups("LATAM")
        for latam_group in latam_groups:
            self.assertTrue(latam_group['country_code'] in self.__latam_country_codes__)





if __name__ == '__main__':
    unittest.main()
