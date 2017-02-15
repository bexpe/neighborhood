

class County:

    def __init__(self, province_name, urban_communities_amount, rural_communities_amount,
                 urban_rural_communities_amount, rural_areas_amount, cities_amount, county_cities_amount,
                 delegacies_amount):

        self.province_name = 'małopolskie'
        self.urban_communities_amount = urban_communities_amount # liczba gmin miejskich
        self.rural_communities_amonut = rural_communities_amount # liczba gmin wiejskich
        self.urban_rural_communities_amount = urban_rural_communities_amount # liczba gmin miejsko- wiejskich
        self.rural_areas_amount = rural_areas_amount # liczba obszarów wiejskich
        self.cities_amount = cities_amount # liczba miast
        self.county_cities_amount = county_cities_amount # liczba miast na prawach powiatu
        self.delegacies_amount = delegacies_amount # liczba delegatur