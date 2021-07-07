# Week 3: REST API

## Topics

- Frontend/backend
  - In modern web development, the frontend is it's own deployable application (Vue.js, Angular, React). The frontend is a "client-side" application, meaning all the code is executed within the user's browser. 
  - To get information like the user's information or content, the frontend will make a **request** to the backend. The frontend is unaware of how the information is retrieved or processed on the backend, nor should it be. This **decouples** the frontend from the backend and separates their concerns.
  - The thing that the frontend makes a request to is the "API". Specifically a "REST API" in this web development example. (You will hear "API" in a lot of contexts in software development. The Java programming language is actually an "API" to the Java Virtual Machine (JVM).)
- Client-side development
  - Everything that runs or is rendered in the browser: HTML, CSS, JavaScript. These can be simple, static, HTML documents... or they can be real applications built on Vue.js, React, Angular, or other frameworks. These frameworks are literally a _framework_ for using JavaScript to respond to user input and update the HTML document. These modern, advanced frameworks are used in a design pattern called "Model-View-Controller", where the **model** are the entities stored in a database (people, places, things), the **view** is an HTML document for rendering the data, (mapped to URL paths like /person, /place, /thing) and the **controller** is the JS running on the client, responding to user input and updating the view as necessary. 
    - Something like Django, a popular web framework in Python, uses a simpler approach called "Model-View-Template", where the HTML document is rendered server-side and sent to the client. Javascript is minimal, typically for aesthetics or enhancing the user experience. The **templates** are similar to **views** in MVC, but they are less flexible.
- HTTP = Hypertext Transfer Protocol
  - It's how browsers (clients) and websites (servers) exchange information. Browsing to a website is a "request". Using the "requests" module in Python is... well... sending a request!
  - There are destinct parts to an HTTP request: URL, query parameters, headers, and body

- REST APIs = "REpresentational State Transfer ... Application Programming Interface"
  - Somewhat-standard specification for describing the resources (people, posts, comments, photos) of an application, and how clients interact with them. Common naming convention is `api/resource/<resource-id>/`. This can be extended if there are sub-resources under the parent: `api/resource/<resource-id>/child/<child-id>`. A contextual example would be `api/user/101/posts/1`, which would hypothetically return user 101's first post.
  - How clients interact with the API's resources is described using [HTTP verbs](https://www.restapitutorial.com/lessons/httpmethods.html): GET, POST, PUT, DELETE. So...
    - `GET api/user/101/posts/1` would _get_ or _retrieve_ the user's first post
    - `DELETE api/user/101/posts/1` would _delete_ the post
    - `POST api/user/101/posts/2` would create the 2nd post, which would require that the client send the actual content for the post in the request body. 
 - JSON = JavaScript Object Notation
   - "It's just a Python dictionary"
   - https://www.json.org/json-en.html
  
## Learning materials

- Example APIs you can send requests to:
  - Star Wars API: https://swapi.dev/
    - Example: https://swapi.dev/api/people/1
  - National Highway Safeway Vehicle database: https://vpic.nhtsa.dot.gov/api/
    - Example: https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json
  - Here's a giant directory of other APIs. Use the toolbar on the left to find a category that's interesting to you. https://documenter.getpostman.com/view/8854915/Szf7znEe#62510224-e2fc-4a7a-af33-33b4a31b63b3
  - UCSB Academics: https://developer.ucsb.edu/apis/academics
- HTTP
  - https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html
  
## Exercises

- Install Postman and send requests to the the public APIs above. Just browse around and try to get a feel for the URL formay and JSON
- Follow this Flask tutorial: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
- Get a basic Flask app running locally with a single GET API that returns some JSON blob, it doesn't matter what the content is. Send a requst to it using Postman.
  - Hint: the URL in Postman will look like "127.0.0.1:5000/api/example-api/" or "localhost:5000/api/example-api/". The "example-api" will depend on what you actually name the route. The Port may also be different.
- Fork the Flask app on Azure Samples, run it locally. Following the other APIs as an example..
- implement 2 APIs to GET resource
- Implement a GET API ("/api/upperCaseService") that accepts a request body with this content:

  ```json
  {
    "words": ["james", "may", "jeremy", "clarkson", "richard", "hammond"]
  }
  ```

  And returns the **same** body object, but the words are Capitalized! 
  
  ```json
  {
    "words": ["James", "May", "Jeremy", "Clarkson", "Richard", "Hammond"]
  }
  ```
  
  Don't just return static content, your API should should read the request body, uppercase the words in the array, and return the object. You can test your API by sending a more complex request:
  
  ```json
  {
    "words": ["here", "are", "a", "lot", "of", "words", "that", "need", "to", "all", "be", "capitalized"]
  }
  ```
