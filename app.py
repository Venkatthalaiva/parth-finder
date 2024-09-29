from flask import Flask, request, jsonify, render_template
import pandas as pd
import networkx as nx

app = Flask(__name__)

# Load data
location_map = pd.read_csv(r"Gramhal_ Pan-India Mappings - Gramhal - Location Map2222.csv")
neighbour_map = pd.read_csv(r"District Neighbour Map44.csv")

# Create a graph from the neighbour map
graph = nx.Graph()
neighbour_columns = ['Neighbour_1', 'Neighbour _2', 'Neighbour_3', 'Neighbour_4', 'Neighbour_5', 'Neighbour_6', 'Neighbour _7']

# Adding edges to the graph
for index, row in neighbour_map.iterrows():
    main_district = row['Main_District_Name']  # Adjust this based on your actual column name
    for column in neighbour_columns:
        neighbour_district = row[column]
        if pd.notna(neighbour_district):  # Check if the neighbour district is not NaN
            graph.add_edge(main_district, neighbour_district)

# Define a function to get the shortest path
def find_shortest_path(start_district, end_district):
    try:
        shortest_path = nx.shortest_path(graph, source=start_district, target=end_district)
        return shortest_path
    except nx.NetworkXNoPath:
        return f"No path found between {start_district} and {end_district}"

# Default route to render the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find_path', methods=['GET'])
def find_path():
    start = request.args.get('start')
    end = request.args.get('end')
    path = find_shortest_path(start, end)
    return jsonify({'path': path})

if __name__ == '__main__':
    app.run(debug=True)

