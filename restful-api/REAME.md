# restful-api/README.md

## 0. Basics of HTTP/HTTPS

### Background

HTTP (Hypertext Transfer Protocol) is the core protocol used for data communication on the web. HTTPS is the secure version, adding SSL/TLS encryption to protect against eavesdropping and tampering.

### Objective

* Understand the differences between HTTP and HTTPS
* Learn the structure of HTTP requests/responses
* Recognize common HTTP methods and status codes

### Resources

* [MDN: HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
* [HTTP vs HTTPS](https://www.cloudflare.com/learning/ssl/why-https-is-important/)
* [List of HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Summary

* **HTTP vs HTTPS**: HTTPS adds encryption (SSL/TLS), securing the data in transit.
* **Structure**: HTTP requests include method, path, headers, and optionally a body. Responses include status code, headers, and a body.
* **Methods**:

  * GET: Retrieve data (e.g., webpage or API data)
  * POST: Submit data to the server
  * PUT: Update an existing resource
  * DELETE: Remove a resource
* **Status Codes**:

  * 200 OK: Successful request
  * 201 Created: Resource created
  * 400 Bad Request: Invalid client request
  * 404 Not Found: Resource not found
  * 500 Internal Server Error: Server-side problem

---

## 1. Using `curl` to Consume APIs

### Objective

* Use curl to fetch data, inspect headers, and send POST requests

### Examples

```bash
curl --version
curl http://example.com
curl https://jsonplaceholder.typicode.com/posts
curl -I https://jsonplaceholder.typicode.com/posts
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### Output

* JSON response of posts
* Headers-only response with `-I`
* POST simulation returns a new JSON object (id: 101)

---

## 2. Python and `requests`

### Objective

* Use Python `requests` to fetch and process data

### Functions

#### fetch\_and\_print\_posts()

* Fetches posts and prints titles
* Displays status code

#### fetch\_and\_save\_posts()

* Saves post data to `posts.csv` using `csv.DictWriter`

### Example Code

```python
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts
fetch_and_print_posts()
fetch_and_save_posts()
```

### Output

* Printed status: `Status Code: 200`
* Post titles printed
* CSV file with `id`, `title`, `body` columns

---

## 3. API with Python's `http.server`

### Objective

* Build a simple API with basic routing and JSON responses

### Endpoints

* `/`: "Hello, this is a simple API!"
* `/data`: returns JSON `{"name": "John", "age": 30, "city": "New York"}`
* `/status`: returns "OK"
* Undefined paths return 404 with "Endpoint not found"

---

## 4. Flask API

### Objective

* Build a Flask API with endpoints and POST functionality

### Endpoints

* `/`: Welcome message
* `/status`: returns "OK"
* `/data`: list of usernames
* `/users/<username>`: returns user details or error
* `/add_user`: accepts POST with JSON, adds user to dictionary

### Notes

* Uses `jsonify`, `request` from Flask
* Proper error handling for missing username

### Sample Output

```json
{
  "message": "User added",
  "user": {
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
  }
}
```

---

## 5. API Authentication & Security

### Objective

* Implement Basic Auth and JWT-based authentication

### Tools

* Flask-HTTPAuth for Basic Auth
* Flask-JWT-Extended for Token Auth

### Steps

* Use `werkzeug.security` for password hashing
* Protect routes with `@auth.login_required`
* Set JWT secret key
* Create `/login` to return token
* Use `@jwt_required()` for protected routes
* Implement role-based access

---

## Repository Structure

```
holbertonschool-higher_level_programming/
└── restful-api/
    ├── task_02_requests.py
    ├── task_03_http_server.py
    ├── task_04_flask.py
    └── README.md

