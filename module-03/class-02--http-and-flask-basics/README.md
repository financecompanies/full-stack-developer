# HTTP and Flask basics

## Introduction to HTTP

[![](https://img.youtube.com/vi/rtYY2NvDMWE/0.jpg)](https://youtu.be/rtYY2NvDMWE)

### Features:
* **Connectionless**: When a request is sent, the client opens the connection; once a response is received, the client closes the connection. The client and server only maintain a connection during the response and request. Future responses are made on a new connection.
* **Stateless**: There is no dependency between successive requests.
* **Not Sessionless**: Utilizing headers and cookies, sessions can be created to allow each HTTP request to share the same context.
* **Media Independent**: Any type of data can be sent over HTTP as long as both the client and server know how to handle the data format. In our case, we'll use JSON.

### Elements:
* **Universal Resource Identifiers (URIs)**: An example URI is `http://www.example.com/tasks/term=homework`. It has certain components:
    * **Scheme**: specifies the protocol used to access the resource, HTTP or HTTPS. In our example `http`.
    * **Host**: specifies the host that holds the resources. In our example `www.example.com`.
    * **Path**: specifies the specific resource being requested. In our example, `/tasks`.
    * **Query**: an optional component, the query string provides information the resource can use for some purpose such as a search parameter. In our example, `/term=homework`.

> ### Side Note: URI vs URL
> You may be unsure what the difference is between a URI (Universal Resource Identifier) and a URL (Universal Resource Locator). These terms tend to get confused a lot, and are even frequently used interchangeably—but there is a distinction.
>
> The term URI can refer to any identifier for a resource—for example, it could be either the name of a resource or the address of a resource (since both the name and address are identifiers of that resource). In contrast, URL only refers to the location of a resource—in other words, it only ever refers to an address.
>
> So, "URI" could refer to a name or an address, while "URL" only refers to an address. Thus, URLs are a specific type of URI that is used to locate a resource on the internet when a client makes a request to a server.
>
> And if you really want to dive into the topic, here are some further readings (with examples and Venn diagrams):
>
> StackExchange: What is the difference between a URI and a URL?
StackOverflow: What is the difference between a URI, a URL, and a URN?
RFC 3986, published by the Internet Engineering Taskforce (this one is rather hefty and more of an official reference than a reader-friendly explanation)

## HTTP Requests

### HTTP Requests
HTTP requests are sent from the client to the server to initiate some operation. In addition to the URL, HTTP requests have other elements to specify the requested resource.

#### Elements:
* **Method**: Defines the operation to be performed
* **Path**: The URL of the resource to be fetched, excluding the scheme and host
HTTP Version
* **Headers**: optional information, success as Accept-Language
* **Body**: optional information, usually for methods such as POST and PATCH, which contain the resource being sent to the server

#### Request Methods
Different request methods indicate different operations to be performed. It's essential to attend to this to correctly format your requests and properly structure an API.
* **GET**: ONLY retrieves information for the requested resource of the given URI
* **POST**: Send data to the server to create a new resource.
* **PUT**: Replaces all of the representation of the target resource with the request data
* **PATCH**: Partially modifies the representation of the target resource with the request data
* **DELETE**: Removes all of the representation of the resource specified by the URI
* **OPTIONS**: Sends the communication options for the requested resource

## HTTP Responses

### HTTP Responses
After the request has been received by the server and processed, the server returns an HTTP response message to the client. The response informs the client of the outcome of the requested operation.

#### Elements:
* **Status Code & Status Message**
* **HTTP Version**
* **Headers**: similar to the request headers, provides information about the response and resource representation. Some common headers include:
    * **Date**
    * **Content-Type**: the media type of the body of the request
* **Body**: optional data containing the requested resource

#### Status Codes:
As an API developer, it's important to send the correct status code. As a developer using an API, the status codes—particularly the error codes—are important for understanding what caused an error and how to proceed.

**Codes fall into five categories:**
* `1xx` Informational
* `2xx` Success
* `3xx` Redirection
* `4xx` Client Error
* `5xx` Server Error

**Common Codes:**
* `200`: OK
* `201`: Created
* `304`: Not Modified
* `400`: Bad Request
* `401`: Unauthorized
* `404`: Not Found
* `405`: Method Not Allowed
* `500`: Internal Server Error

#### Resources
* There are lots of resources out there that list status codes, including one of my favorites: [HTTP Dogs](https://httpstatusdogs.com/)


## Intro to Flask

### Introduction to Flask
[Flask](http://flask.pocoo.org/docs/1.0/) is the tool we'll use to create our api server.

It is a "micro" framework, which means that its core functionality is kept simple, but that there are numerous extensions to allow developers to add other functionality (such as authentication and database support).

[![](https://img.youtube.com/vi/W5LxATUf_KM/0.jpg)](https://youtu.be/W5LxATUf_KM)

### Creating a basic Flask application

[![](https://img.youtube.com/vi/tXBk8FBtwwM/0.jpg)](https://youtu.be/tXBk8FBtwwM)

### Basic App
1.  Import your dependencies
    * `from flask import Flask, jsonify`
2. Define the `create_app` function with parameter `test_config` initially set to `None`. Then within the function:
3. Define the application. Ensure you include the first parameter. `__name__` is the name of the current Python module.
    * `app = Flask(__name__)`
4. Return the app instance.
    * `return app`

Configured Application
The below information is for your reference and related information can be found in the Flask documentation. You are expected to use the basic application set up for this course. However, as you build larger applications that utilize multiple environments and configurations (production, development, testing, etc) this knowledge will be helpful for streamlining your development process.

1. Import additional dependencies. You'll need to import os in order to access the operating system and file structure `import os`

2. Set up your default configuration. When working in development your `SECRET_KEY` can be hardcoded as shown but for production should come from a secret environment variable. `DATABASE` is the path for the database file.

```python
app.config.from_mapping(
 SECRET_KEY='dev',
 DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
 )
 ```

 3. If a `config.py` file is included in the instance folder, use its values to override the default configuration, for instance the `SECRET_KEY`. You can also enable a testing configuration if it was passed into the `create_app` function.

 ```python
 if test_config is None:
 # load the instance config, if it exists, when not testing
 app.config.from_pyfile('config.py', silent=True)
else:
 # load the test config if passed in
 app.config.from_mapping(test_config)
 ```

 4. Make the instance path directory. The app will create the database file within that directory so it needs to exist.

 ```python
 try:
 os.makedirs(app.instance_path)
except OSError:
 pass
 ```

### First Endpoint with JSON

Before you return the app, use the @app.route decorator to create an endpoint to path / and define a function to handle that route.

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'

return app
```

Instead of returning text, use jsonify to send an object containing the message

```python
 return jsonify({'message':'Hello, World!'})
```

### Run your application

In the command line, you'll run three lines of code. The first two lines tell the terminal where to find your application and to run it in development mode, which allows you to keep it running while it hotloads any modifications. The third actually starts the application. If running your application on Windows

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

[![](https://img.youtube.com/vi/NAtUcUuduVs/0.jpg)](https://youtu.be/NAtUcUuduVs)

## Introduction to Curl and Chrome Dev Tools

### Chrome Dev Tools

[![](https://img.youtube.com/vi/5MHAJcYQHZo/0.jpg)](https://youtu.be/5MHAJcYQHZo)

### Curl

[![](https://img.youtube.com/vi/jWEFlKA0ib4/0.jpg)](https://youtu.be/jWEFlKA0ib4)

#### Curl Syntax

```bash
curl -X POST http://www.example.com/tasks/
```

The above is a sample curl request. Every request starts off with the command `curl` and needs to include a URL. Other parts you see added in are options that you can use to build your request. In the example the `-X` shortform option (also `--request`) specifies the request method.

[![](https://img.youtube.com/vi/VfdQXImHJlU/0.jpg)](https://youtu.be/VfdQXImHJlU)

#### Curl Options

You can find more options by entering `curl --help` in the terminal. Some frequently used options are:

* `-X` or `--request` COMMAND
* `-d` or `--data` DATA
* `-F` or `--form` CONTENT
* `-u` or `--user` USER[:PASSWORD]
* `-H` or `--header` LINE

#### Extra

Pretty printing

```
curl -s -D "/dev/stderr" https://pokeapi.co/api/v2/move/47 | jq
```

Or simply add to `~/.curlrc` file

```bash
 -w "\n"
 silent
 -D /dev/stderr
 ```