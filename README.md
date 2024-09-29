Shortest Path Finder Between Districts in India
Project Overview
The aim of this project is to build a web application that allows users to enter the names of two districts in India and find the shortest path between them. The project leverages geographical data about neighboring districts and state boundaries to compute the shortest path using graph traversal algorithms. The final output is a web page displaying the districts to be crossed and the states they belong to.
Table of Contents
Introduction
Objective
Data Description
Methodology
Data Ingestion
Shortest Path Calculation
Web Application Development
Results
Conclusion
Future Enhancements
References

1. Introduction
This project provides an interactive web-based solution for determining the shortest path between any two districts in India. The application utilizes a graph structure, where nodes represent districts and edges represent neighboring districts. By implementing algorithms like Breadth-First Search (BFS), the application calculates the shortest path in terms of districts traversed.
2. Objective
The main objective of this project is to:
Create a comprehensive dataset of neighboring districts in India.
Develop a method to find the shortest path between any two districts.
Build a web-based user interface for users to input the start and end districts and visualize the shortest path.
3. Data Description
The project uses two primary datasets:
District Neighbour Map: This dataset contains district names along with their neighboring districts. It is used to build the adjacency list for graph traversal.
District-State Mapping: This dataset includes the mapping of each district to its corresponding state, helping in the display of states along the path.
4. Methodology
4.1 Data Ingestion
The data is ingested from CSV files using the pandas library.
Neighboring districts for each district are extracted to form a graph-like structure using dictionaries or adjacency lists.
4.2 Shortest Path Calculation
A graph traversal algorithm like Breadth-First Search (BFS) is implemented to find the shortest path.
The BFS algorithm ensures that the shortest path, in terms of the number of districts crossed, is obtained.
The path is then translated into district and state names for easy interpretation.
4.3 Web Application Development
Backend:
Implemented using Flask, a lightweight web framework in Python.
The server handles the logic of ingesting data, computing the shortest path, and serving the results to the frontend.
Frontend:
Designed using Bootstrap to provide a responsive user interface.
A form is presented to the user to input the source and destination districts.
The results are displayed dynamically on the page.
Directory Structure:
sql
Copy code
my_flask_app/
│
├── app.py                   <-- Main Flask application file
├── templates/               <-- Folder containing HTML templates
│   └── index.html           <-- HTML template for the home page
└── static/                  <-- Folder containing static files
    ├── css/
    │   └── style.css        <-- Custom CSS styles
    ├── js/
    │   └── script.js        <-- JavaScript files
    └── images/
        └── logo.png         <-- Images for the web application

Code Sample: app.py
python
Copy code
from flask import Flask, render_template, request, jsonify
import pandas as pd
from collections import deque

app = Flask(__name__)

# Load data and create adjacency list
def load_data():
    df = pd.read_csv('District Neighbour Map33.csv')
    graph = {}
    for _, row in df.iterrows():
        district = row['District_name']
        neighbors = [row[f'Neighbour_{i}'] for i in range(1, 8) if pd.notna(row[f'Neighbour_{i}'])]
        graph[district] = neighbors
    return graph

# Find the shortest path using BFS
def bfs_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return None
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        for neighbor in graph[node]:
            if neighbor in path:
                continue
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    return None

# Flask route to render the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the form submission and return results
@app.route('/find_path', methods=['POST'])
def find_path():
    start = request.form['start_district']
    end = request.form['end_district']
    graph = load_data()
    path = bfs_shortest_path(graph, start, end)
    if path:
        return jsonify({'path': path})
    else:
        return jsonify({'path': 'No path found'})

if __name__ == '__main__':
    app.run(debug=True)

5. Results
The web application successfully computes and displays the shortest path between any two districts.
The application shows the names of all districts and states crossed on the shortest path, providing valuable insights for logistical planning and transportation.
6. Conclusion
This project demonstrates the use of graph traversal algorithms in solving real-world geographical problems. By combining district data with a web-based interface, it provides an easy-to-use tool for finding paths between districts in India.
7. Future Enhancements
Implementing more advanced algorithms like Dijkstra’s for weighted paths.
Adding a visual map representation of the districts and paths.
Enhancing the user interface with more interactivity and custom styling.
8. References
Flask Documentation: https://flask.palletsprojects.com/
Bootstrap Framework: https://getbootstrap.com/
