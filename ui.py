class Menu_UI:
    @staticmethod
    def print_menu():
        while True:
            option = input(
                        "What would you like to do:\n"
                        "(1) List statistics\n"
                        "(2) Display 3 cities with longest names\n"
                        "(3) Display county's name with the largest number of communities\n"
                        "(4) Display locations, that belong to more than one category\n"
                        "(5) Advanced search\n"
                        "(0) Exit program\n")

            if option == '1':
                get_list_statistics()
            if option == '2':
                Province.get_3_longest_names_cities()
            if option == '3':
                get_county_with_max_communities()
            if option == '4':
                get_multicategories_countries()
            if option == '5':
                advanced_search()
            if option == '0':
                break