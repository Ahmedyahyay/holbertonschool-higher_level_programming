// Get the element with id 'red_header'
const redHeader = document.getElementById('red_header');

// Add a click event listener to the element
redHeader.addEventListener('click', function() {
  // Add the 'red' class to the header
  document.querySelector('header').classList.add('red');
});

