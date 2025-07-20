// Get the element with id 'update_header'
const updateHeader = document.getElementById('update_header');

// Add a click event listener to the element
updateHeader.addEventListener('click', function() {
  // Update the text content of the header element
  document.querySelector('header').textContent = 'New Header!!!';
});

