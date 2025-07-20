// Get the element with id 'red_header'
const redHeader = document.getElementById('red_header');

// Add a click event listener to the element
redHeader.addEventListener('click', function() {
  // Change the text color of the header to red
  document.querySelector('header').style.color = '#FF0000';
});

