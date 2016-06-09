COLOMBIA_PLACES_FILTERS = [
    # Colombia
    {'country': 'CO', 'location': 'Bogota'},
    {'country': 'CO', 'location': 'Medellin'},
    # TODO: solve issue, meetup is not returning results for cali even though it actually exist a django group
    {'country': 'CO', 'location': 'Cali'},
    {'country': 'CO', 'location': 'Barranquilla'},
    {'country': 'CO', 'location': 'Santa marta'},
    {'country': 'CO', 'location': 'Pasto'},
]

LATAM_PLACES_FILTERS = [

    # Argentina
    {'country': 'AR', 'location': 'Buenos Aires'},
    {'country': 'AR', 'location': 'Cordoba'},
    # TODO: solve issue, when this filter is enabled, US groups are being returned. Only AR groups should ve returned
    #{'country': 'AR', 'location': 'La Plata'},

    # Bolivia
    {'country': 'BO', 'location': 'Santa Cruz de la Sierra'},
    {'country': 'BO', 'location': 'El Alto'},
    {'country': 'BO', 'location': 'La Paz'},
    {'country': 'BO', 'location': 'Cochabamba'},
    #
    # Brazil
    {'country': 'BR', 'location': 'sao paulo'},
    {'country': 'BR', 'location': 'brasilia'},

    # Chile
    {'country': 'CL', 'location': 'Santiago'},

    #
    # # # Costa Rica
    # TODO: solve issue, when this filter is enabled, US groups are being returned. Only AR groups should ve returned
    # {'country': 'CR', 'location': 'San Jose'},
    #
    # # # Cuba
    # TODO: solve issue, when this filter is enabled, US groups are being returned. Only AR groups should ve returned
    # {'country': 'CU', 'location': 'Habana'},

    # Ecuador
    {'country': 'EC', 'location': 'quito'},

    # Guatemala
    {'country': 'GT', 'location': 'Guatemala'},

    # Honduras
    {'country': 'HN', 'location': 'Tegucigalpa'},

    # Mexico
    {'country': 'MX', 'location': 'ciudad de mexico'},
    {'country': 'MX', 'location': 'Ecatepec'},
    {'country': 'MX', 'location': 'Guadalajara'},
    {'country': 'MX', 'location': 'Puebla'},
    {'country': 'MX', 'location': 'Monterrey'},

    # Paraguay
    {'country': 'PY', 'location': 'asuncion'},

    # Peru
    {'country': 'PE', 'location': 'Lima'},

    # Uruguay
    {'country': 'UY', 'location': 'Montevideo'},

    # El Salvador
    {'country': 'SV', 'location': 'San Salvador'},

]

# add colombia filters to latam filters
LATAM_PLACES_FILTERS.extend(COLOMBIA_PLACES_FILTERS)

KEYWORD_FILTERS = [
    # general keywords
    "Django", "Python", "PyData", "PyLadies", "Py",
    # special group names
    "Grupy-SP",
]

LOCATION_CODES = {
    "CO": "Colombia",
    "LATAM": "LATAM"
}
