# Print out all colors from color-list1 not contained in color-list2. 

color_list1 = input("Enter colors for color-list1, separated by commas: ").split(',')
color_list2 = input("Enter colors for color-list2, separated by commas: ").split(',')
differing_colors = [color.strip() for color in color_list1 if color.strip() not in color_list2]
print("Colors in color-list1 not contained in color-list2:")
for color in differing_colors:
    print(color)
