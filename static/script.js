document.getElementById('path-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get input values
    const start = document.getElementById('start').value;
    const end = document.getElementById('end').value;

    // Make a GET request to the Flask endpoint
    fetch(`/find_path?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            // Display the result in the result div
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `<h3>Shortest Path: </h3><p>${data.path.join(' ➔ ')}</p>`;
        })
        .catch(error => {
            console.error('Error fetching the path:', error);
        });
});
