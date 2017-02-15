import csv

class Province:

    FILE = 'data/malopolska.csv'
    def __init__(self, province_name, county_amount, urban_communities_amount, rural_communities_amount,
                 urban_rural_communities_amount, rural_areas_amount, cities_amount, county_cities_amount, delegacies_amount):

        self.province_name = 'małopolskie'
        self.county_amount = [] # liczba powiatów
        self.urban_communities_amount = [] # liczba gmin miejskich
        self.rural_communities_amonut = [] # liczba gmin wiejskich
        self.urban_rural_communities_amount = [] # liczba gmin miejsko- wiejskich
        self.rural_areas_amount = [] # liczba obszarów wiejskich
        self.cities_amount = [] # liczba miast
        self.county_cities_amount = [] # liczba miast na prawach powiatu
        self.delegacies_amount = [] # liczba delegatur











    @staticmethod
    def get_province_objects():
        """
        :return: list of provinces as a list of objects without any additional action
        """
        return all_objects_list

    @classmethod
    def get_3_longest_names_cities(cls):
        sorted_by_len = []
        for object in all_objects_list:
            sorted_by_len.append(object)
            sorted_by_len.sort(key=lambda t: len(t[4]), reverse=True)
        longest_city_names = sorted_by_len[:3]
        for line in longest_city_names:
            print(line[4])
        print('\n')

    @classmethod
    def get_county_with_max_communities(cls):
        """
        Znajduje powiat z najwieksza iloscia gmin ogolem
        :return:
        """
        for city in cls.all_objects_list:
            print(city)

    def get_multicategories_countries(self):
        pass

    def advanced_search(self):
        pass

    @staticmethod
    def read_from_csv():
        """
        Returns list of all provinces and counties and communities in a csv file

        :return: list
        """
        all_objects_list = []
        FILE = 'data/malopolska.csv'
        with open(FILE) as csv_file:
            readCSV = csv.reader(csv_file, delimiter='\t')
            for row in readCSV:
   #            new_object = ''.join(row)
                all_objects_list.append(row)
            print(all_objects_list)
            return all_objects_list

    @classmethod
    def table(cls):
        for object in cls.all_objects_list:
            print(object)



################################################################################

Province.read_from_csv()

# # Province.get_3_longest_names_cities()
# province1 = Province('nazwa1', 'typ', '12', '122', '73', '4')
# province2 = Province('nazwa2', 'typ', '12', '122', '73', '4')
# province3 = Province('nazwa3', 'typ', '12', '122', '73', '4')
# province4 = Province('nazwa4', 'typ', '12', '122', '73', '4')
# province5 = Province('nazwa5', 'typ', '12', '122', '73', '4')
# Province.get_county_with_max_communities()
# Province.table()
