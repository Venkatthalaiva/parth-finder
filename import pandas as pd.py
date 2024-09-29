import pandas as pd

# Load the CSV file
df = pd.read_csv('path_to_your_file.csv')

# Check the structure of the CSV
print(df.head())

# Assuming the CSV contains two columns: 'District' and 'Neighbour', with state information, we can build the graph.
# You can now structure the data to build a graph.
