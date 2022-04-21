# # Dictionaries
# # Key Value Pairs
# # {Key: Value}
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# print(programming_dictionary["Bug"])
#
# # Add new entry
#
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)
#
# empty_dictionary = {}
#
# # Wipe existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# # Edit item
# # programming_dictionary["Bug"] = "new value"
# # print(programming_dictionary)
#
# # Loop
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }
#
# # Nesting in Dictionary in Dictionary
#
# travel_log = {
#     "France": {"Cities_Visited":  ["Paris", "Lille", "Dijon"], "total_visits": 12}
# }
#
# # Nesting dictionary in list
#
# # [{
# #     Key: [List],
# #     Key2: {Dict},
# # },
# #     {
# #         Key: Value,
# #         Key2: Value,
# # }]
#
# travel_log = [
#     {
#         "Country": "United States",
#         "cities_visited": ["Austin", "New Haven", "New York City"],
#         "total_visits": 8
#     },
#     {
#         "Country": "France",
#         "Cities_Visited":  ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
# ]
#
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries


def add_new_country(country_visited, num_visits, cities_visited):
    new_country = {"country": country_visited, "visits": num_visits, "cities": cities_visited}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

