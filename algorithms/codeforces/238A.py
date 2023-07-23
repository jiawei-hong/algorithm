valera_origin_has_horseshoes = 4 
horseshoe_colors = input().split(' ')
unique_colors = set(horseshoe_colors)

print(valera_origin_has_horseshoes - len(unique_colors))