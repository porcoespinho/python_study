
'''
# using index to match values / not convenient nor intuitive
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
ind_ger = countries.index('germany')
print(ind_ger)
print(capitals[ind_ger])

# using dictionaries to locate values
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

print(europe['norway'])
# using the keys method to get all the keys
print(europe.keys())

# adding values to a dictionary. Add the key Latvia to Europe
europe["latvia"] = "riga"
print("latvia" in europe)

# deleting values from a dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}
europe["latvia"] = 'riga'
print("latvia" in europe)

del(europe["latvia"])
print("latvia" in europe)
'''
# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}
print(europe['norway']['capital'])
