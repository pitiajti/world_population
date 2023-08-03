import json

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


# Print the 2-1- population for each country.
for pop_dict in pop_data:
    if pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = pop_dict['Value']
            print(f"{country_name}: {population}")