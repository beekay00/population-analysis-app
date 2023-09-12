def find_country_with_max_population(countries, populations):
    max_population = max(populations)
    max_population_index = populations.index(max_population)
    country_with_max_population = countries[max_population_index]
    return country_with_max_population