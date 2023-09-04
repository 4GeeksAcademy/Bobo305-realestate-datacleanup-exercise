import pandas as pd
ds = pd.read_csv('assets/real_estate.csv', sep=';')

population_counts = ds['level5'].value_counts()


most_houses_population = population_counts.idxmax()
num_houses_most_population = population_counts.max()

#the results
print("Population with the Most Houses:", most_houses_population)
print("Number of Houses in the Most Populated Population:", num_houses_most_population)

