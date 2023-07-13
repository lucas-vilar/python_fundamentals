# Creating a new set
best_teams = {'Real Madrid', 'Barcelona', 'Manchester United', 'Manchester City', 'Flamengo'}

best_players = set(['Messi', 'Neymar', 'Cristiano Ronaldo'])
print(best_teams, best_players)

# Creating a FronzenSet
colors = ['red', 'blue', 'green', 'black', 'white', 'red']
frozenset_colors = frozenset(colors)
print("\n",frozenset_colors)

# Add a new item
best_teams.add('Liverpool')
print("\n",best_teams)

# Removing an item
best_players.remove('Neymar')
print("\n",best_players)

# Find elements in a set
print('\n','Messi' in best_players)

all_players = ['Messi', 'Neymar', 'Cristiano Ronaldo', 'Ronaldo', 'Zico', 'Salah', 'Roberto', 'Mike', 'Gerrard']

the_best = [player for player in all_players if player in best_players]

print('\n',the_best)