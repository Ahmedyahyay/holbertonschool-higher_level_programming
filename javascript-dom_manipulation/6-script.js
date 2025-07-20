// Fetch data from the provided URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Get the character name from the data
    const characterName = data.name;
    
    // Display the character name in the HTML element with id 'character'
    document.getElementById('character').textContent = characterName;
  })
  .catch(error => {
    // Handle errors if any
    console.error('Error fetching data:', error);
  });

