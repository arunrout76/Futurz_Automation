from pages.admin_page import sessions_cover

sessions_covers = ["1-VisualAnalogies-Workout2,1-VisualAnalogies-Workout3,1-VisualAnalogies-Workout4"]

search_terms = ['1-VisualAnalogies-Workout1', 'Workout2', 'Workout3']
my_list = ['1-VisualAnalogies-Workout1', '1-VisualAnalogies-Workout2', '1-VisualAnalogies-Workout3', '1-VisualAnalogies-Workout4',
           '1-VisualAnalogies-Workout5', '1-VisualAnalogies-Workout10']

for term in search_terms:
    matching_elements = [item for item in my_list if term == item]

    if matching_elements:
        print(f"Clicking on the element for '{term}': {matching_elements}")
        # Add your click action here
    else:
        print(f"No matching element found for '{term}'")



# print(type(sessions_covers))
# print(sessions_covers)
# print(len(sessions_covers))
# print(sessions_covers[0])
# converting = sessions_covers[0]
# list_session = converting.split(",")
# print(f"this is List: {list_session}")


# result_list = [int(item) for item in sessions_covers[0].split(',')]
#
# print(result_list)
# for a in sessions_covers:
#     print(a)
