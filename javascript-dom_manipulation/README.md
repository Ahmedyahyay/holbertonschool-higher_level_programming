ChatGPT said:
JavaScript DOM Manipulation Tasks
This repository contains a series of JavaScript tasks designed to practice DOM manipulation and API interactions. The tasks focus on selecting HTML elements, modifying their content, adding or removing classes, handling events, and using APIs.

Table of Contents
Color Me

Click and Turn Red

Add .red Class

Toggle Classes

List of Elements

Change the Text

Star Wars Character

Star Wars Movies

Say Hello!

1. Color Me
Task: Write a JavaScript script that updates the text color of the header element to red (#FF0000).

Instructions:

You must use document.querySelector to select the HTML tag.

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
2. Click and Turn Red
Task: Write a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the element with id="red_header".

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
3. Add .red Class
Task: Write a JavaScript script that adds the class .red to the header element when the user clicks on the element with id="red_header".

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
4. Toggle Classes
Task: Write a JavaScript script that toggles the class of the header element when the user clicks on the tag id="toggle_header". The class must be either .red or .green but never both or empty at the same time.

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
5. List of Elements
Task: Write a JavaScript script that adds a <li> element with the text "Item" to a list when the user clicks on the element with id="add_item".

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
6. Change the Text
Task: Write a JavaScript script that updates the text of the header element to "New Header!!!" when the user clicks on the element with id="update_header".

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
7. Star Wars Character
Task: Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json. Display the name in the HTML element with id="character".

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
8. Star Wars Movies
Task: Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json.

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies"></ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
9. Say Hello!
Task: Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id="hello".

Test:

html
Copy code
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
