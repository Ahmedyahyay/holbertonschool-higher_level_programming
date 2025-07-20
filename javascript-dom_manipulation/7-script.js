// Fetch data from the provided URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Get the 'results' array which contains movie details
    const movies = data.results;

    // Get the ul element with id 'list_movies'
    const listMovies = document.getElementById('list_movies');
    
    // Loop through each movie and create an li element for the title
    movies.forEach(movie => {
      const li = document.createElement('li'); // Create a new li element
      li.textContent = movie.title; // Set the text content to the movie title
      listMovies.appendChild(li); // Append the li to the ul
    });
  })
  .catch(error => {
    // Handle errors if any
    console.error('Error fetching data:', error);
  });

