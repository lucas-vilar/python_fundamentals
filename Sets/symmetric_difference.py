# The symmetric difference returns elements which are either in set A or in set B but not in both

colors_A = {'Blue', 'Red', 'Green', 'Black'}
colors_B = {'Black', 'Pink', 'Orange', 'Blue', 'Red'}

symmetric_difference = colors_A.symmetric_difference(colors_B)
print(symmetric_difference)