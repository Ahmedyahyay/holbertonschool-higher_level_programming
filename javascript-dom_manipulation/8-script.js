// Fetch data from the provided URL
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Get the translation of 'hello' from the response
    const helloTranslation = data.hello;
    
    // Display the translation in the HTML element with id 'hello'
    document.getElementById('hello').textContent = helloTranslation;
  })
  .catch(error => {
    // Handle errors if any
    console.error('Error fetching data:', error);
  });

