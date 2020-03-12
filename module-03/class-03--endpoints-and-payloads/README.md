# Endpoints and payloads

## Overview

[![](https://img.youtube.com/vi/yw8dQyi_Mxk/0.jpg)](https://youtu.be/yw8dQyi_Mxk)

In the last lesson, you gained an understanding of HTTP and the ability to set up a basic Flask app. In this lesson, you'll learn about how to extend the Flask microframework so that we can:
* Organize API Endpoints
* Handle Cross-Origin Resource Sharing (CORS)
* Parse the request path and body
* Use POST, PATCH, and DELETE requests in Flask
* Handle errors

To accomplish this, we'll need to use a new library, called *Flask-CORS*

## Organizing API Endpoints

[![](https://img.youtube.com/vi/jvlXKosZylQ/0.jpg)](https://youtu.be/jvlXKosZylQ)

When organizing API endpoints, they should be based on the resources instead of on actions. The request methods will determine what action should be taken at a given URL endpoint. Your entire API's scheme should be consistent, clear and concise. Below are the principles and examples from the video, for your reference:

### Principles
* **Should be intuitive**
* **Organize by resource**
    * Use nouns in the path, not verbs
    * The method used will determine the operation taken
    * GOOD:
        * https://example.com/posts
    * BAD:
        * https://example.com/get_posts
    * Keep a consistent scheme
        * Plural nouns for collections
        * Use parameters to specify a specific item
        * GOOD:
            * https://example.com/entrees
            * https://example.com/entrees/5
        * BAD:
            * https://example.com/entree
            * https://example.com/entree_five
    * Don’t make them too complex or lengthy
        * No longer than collection/item/collection
        * GOOD:
            * https://example.com/entrees/5/reviews
        * BAD:
            * https://example.com/entrees/5/customers/4/reviews

### Methods & Endpoints Review

The request method used will determine the operation performed for the given resource URI. Though your API documentation should explain exactly what operation is performed and data returned via the response, it should be intuitive for anyone using your API, such as in the example below

[![](https://img.youtube.com/vi/KVQI49a9Ao4/0.jpg)](https://youtu.be/KVQI49a9Ao4)

## CORS

### CORS
If you've had a little experience as a web developer, you may have seen an error in the browser:

`No 'Access-Control-Allow-Origin' header is present on the requested resource`

This error is all about **Cross-Origin Resource Sharing or CORS**. Let's see what that's all about.

[![](https://img.youtube.com/vi/ehkKIqZftrc/0.jpg)](https://youtu.be/ehkKIqZftrc)

The **same-origin policy** is a concept of web security that allows scripts in Webpage 1 to access data from Webpage 2 only if they share the same domain. This means that the above error will be raised in the following cases:

* Different domains
* Different subdomains (`example.com` and `api.example.com`)
* Different ports (`example.com` and `example.com:1234`)
* Different protocols (`http://example.com` and `https://example.com`)

This is not, however, to say that it is really an error. *It is behaving exactly as it should*. This policy is there to protect you and your users. For instance, attackers may embed malicious scripts in advertisements. This policy prevents those scripts from successfully making requests to your bank's website as you access the website hosting the advertisement.

If you're sending any requests beyond very simple GET or POST requests, then before your actual request is sent, the browser sends a preflight OPTIONS request to the server. If CORS is not enabled, then the browser will not respond properly and the actual request will not be sent.

### CORS headers

[![](https://img.youtube.com/vi/WLi2n2XEUZs/0.jpg)](https://youtu.be/WLi2n2XEUZs)

In order for the requests to be processed properly, CORS utilizes headers to specify what the server will allow:

* Access-Control-Allow-Origin
    * What client domains can access its resources. For any domain use *
* Access-Control-Allow-Credentials
    * Only if using cookies for authentication - in which case its value must be true
* Access-Control-Allow-Methods
    * List of HTTP request types allowed
* Access-Control-Allow-Headers
    * List of http request header values the server will allow, particularly useful if you use any custom headers

## Flask-CORS

Welcome to your first Flask extension! [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) is the extension for handling CORS and its installation and usage are very simple.

```python
from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/messages')
    @cross.origin()
    def get_messages():
        return 'GETTING MESSAGES'

    return app
```

[![](https://img.youtube.com/vi/-nO0JJeIXhA/0.jpg)](https://youtu.be/-nO0JJeIXhA)

### Installation
In order to install Flask-CORS simply run

`pip3 install -U flask-cors`

### Initialization
Once Flask-CORS is installed, you simply import the CORS function and call it with your app instance as a parameter. This will intialize Flask-CORS with all default options.

```python
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app)
```

### Resource-Specific Usage
There are multiple options you can use to specify your Flask-CORS behavior. One typical one is resources, which contains a dictionary whose keys are regular expressions and values are dictionary or kwargs

```python
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
```

### Route-Specific Usage
If you need to enable CORS on a given route, like those non-simple requests, you can use `@cross_origin()` to enable it.

```python
@app.route("/hello")
@cross_origin()
def get_greeting():
    return jsonify({'message':'Hello, World!'})
```