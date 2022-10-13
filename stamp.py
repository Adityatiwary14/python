"""rupal has a huge collection of countries stamps. she decided to count the total number of distinct country stamps in her collection she asked for your help you pick the stamps one by one from a stack of country stamps find the total number of distinct country stamps using suitable data type"""
countries = []
while True:
    i=0
    country = str(input("enter country name -"))
    countries.insert(i,country)
    if country == "":
        break
    else:
        total_countries = len(set(countries))
    i=i+1
print("\ntotal umbers of countries are = ",total_countries)


"""
output

enter country name -india
enter country name -pakistan
enter country name -sri lanka
enter country name -

total umbers of countries are =  3
"""