"""
Name: Python Data Analysis
Purpose: Writing data to CSV

Algorithm:
"""

import matplotlib.pyplot as plt

"""Creating function that will take one list input - 
Check for maximum three countries and write to Emissions_subset.csv file"""


def extract_data(country):
    # Validating input up to three countries - If there are more then three countries then return false
    for length in range(len(country)):

        if length > 3:
            print("ERR: Sorry, at most 3 countries can be entered.", end="\n\n")

        if country[length].title() not in li_keys:
            print(f"ERR: Sorry “{country[length]}” is not a valid country", end="\n\n")
            return False
    else:
        extraction_subset = [li_keys[0] + ",", ",".join(li_val[0]) + "\n"]
        for num in range(len(country)):
            extraction_subset.append(country[num].title() + ",")
            extraction_subset.append(extraction_dict[country[num]] + "\n")
    with open("Emissions_subset.csv", 'w') as write_new_csv:
        write_new_csv.write("".join(extraction_subset))
    return write_new_csv


print("A Simple Data Analysis", end="\n")
filename = 'Emissions.csv'
extraction_dict = {}
try:
    with open(filename, 'r') as file:
        for data in file.read().split('\n'):
            extraction_dict.update({data.split(',')[0]: data.split(',')[1:]})

    li_keys = []
    li_val = []
    index = 0
    for x, y in extraction_dict.items():
        print(x, end='-')
        print(y)
        li_keys.append(x)
        li_val.append(y)
    input_year = input("Select a year to find statistics: ")
    li = list(map(int, extraction_dict.get('CO2 per capita')))
    for yr in li:
        if int(yr) == int(input_year):
            index = li.index(yr)

    list_emissions = []
    for i in range(1, len(li_val)):
        for j in li_val[i]:
            if li_val[i].index(j) == index:
                list_emissions.append(j)
    list_emissions = [float(list_emissions[i]) for i in range(len(list_emissions))]

    avg = (sum(list_emissions) / len(list_emissions))
    min_val = min(list_emissions)
    max_val = max(list_emissions)
    index_max = list_emissions.index(max_val)
    index_min = list_emissions.index(min_val)
    country_max_emissions = li_keys[index_max + 1]
    country_min_emissions = li_keys[index_min + 1]
    print(f"In {input_year}, countries with minimum and maximum CO2 emission levels were: [{country_min_emissions}]"
          f" and [{country_max_emissions}] respectively.")
    print(f'Average CO2 emissions in {input_year} were {"%.6f" % round(avg, 6)}')
    print()

    while True:
        visualize_country_name = input("Select the country to visualize: ").lower().title()
        if visualize_country_name in li_keys:
            y_label = "Emissions in " + visualize_country_name
            li1 = list(map(float, extraction_dict.get(visualize_country_name)))
            plt.plot(li, li1)
            plt.xlabel('Year')
            plt.ylabel(y_label)
            plt.show()
            break
        else:
            print("Please enter a Valid country. ")
            continue

    while True:
        try:
            countries_to_compare_list = input("Write two comma separated countries for which you want to visualize "
                                              "data: ").lower().title().split(",")
        except ValueError:
            print("Please write upto two comma separated countries")
        first_country_list = list(map(float, extraction_dict.get(countries_to_compare_list[0])))
        second_country_list = list(map(float, extraction_dict.get(countries_to_compare_list[1])))
    plt.plot(li, first_country_list, label=extraction_dict.get(countries_to_compare_list[0]))
    plt.plot(li, second_country_list, label=extraction_dict.get(countries_to_compare_list[1]))
    plt.xlabel('Year')
    plt.ylabel('Emissions')
    plt.show()

    """Take input up to three comma-separated countries and creating list of countries 
    (Passing value to our next step function)"""
    while True:
        input_string = input("Write up to three comma-separated countries for which you want to extract data: ")
        input_country_list = input_string.split(",")
        # Calling the Function to validate input
        if not extract_data(input_country_list):
            continue
        else:
            break

except FileNotFoundError:
    print("File 'Emissions.csv' is not found")
