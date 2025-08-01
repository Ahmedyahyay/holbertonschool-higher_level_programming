// Get the element with id 'add_item'
const addItem = document.getElementById('add_item');

// Add a click event listener to the element
addItem.addEventListener('click', function() {
  // Create a new li element
  const newItem = document.createElement('li');
  
  // Set the text content of the new li element
  newItem.textContent = 'Item';
  
  // Get the ul element with class 'my_list'
  const myList = document.querySelector('.my_list');
  
  // Append the new li element to the ul
  myList.appendChild(newItem);
});

