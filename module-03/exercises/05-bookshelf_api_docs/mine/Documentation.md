Bookshelf app
==================

Bookshelf is a web application for managing a list of books providing basic information about the them, including a rating for each book so you can manage your favorite books.

I have created this web application because I love to read books, from economics to technology, from children's to food. They're the basis for our life and self development.

We all should read a book everyday!

## Guidelines

The code it's not completed so your job is to finish all the TODO's available throughout the source code.

You'll expend most of your time and effort working with TODO's within the `/backend` project, but there's also TODO's for the `/frontend` project so we encourage you to take a look into them all.

## Code style

This project adheres to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide so you must to follow these guideline too.

## Getting

Before you get contributing started with this project you should know and be comfortable with the prerequisites of this project.

### Prerequisites and installation

#### Frontend

To run the project locally you must have the following prerequisites:
- NodeJS

To install NodeJS access the page https://nodejs.org/en/download/ and download the LTS version for your operation system.

**The frontend tested using:**
- NodeJS 13.0.0
- NPM 6.12.0

#### Backend

To run the project locally you must have the following prerequisites:
- Python 3
- PostgreSQL

To install Python 3 access the page https://www.python.org/downloads/ and download the most recent version for your operation system.

To install PostgreSQL access the page https://www.postgresql.org/download/ and download the most recent version for your operation system.

**The backend was written and tested using:**
- Python 3.8.2
- PostgreSQL 12.2

### Local development

#### Frontend

Open `frontend` folder:

```bash
$ cd frontend
```

Install project dependencies:

```bash
$ npm install
```

 Run the React application:

```bash
npm start
```

Wait until the script run the initialization, after your default browser should open and load the application using the address `http://localhost:3000`

#### Backend

Open `backend` folder:

```bash
$ cd ../backend
```

Create virtual enviroment:

```bash
python -m venv .env
```

Install project dependencies:

```bash
$ pip install -r requirements.txt
```

Create the database:

```bash
$ psql -U postgres < setup.sql
```

Create tables:

```bash
$ psql -U postgres < books.psql
```

Configure Flask application:

```bash
$ export FLASK_APP=flaskr
```

Configure Flask in debug mode:

```bash
$ export FLASK_ENV=development
```

Run Flask application:

```bash
$ flask run
```

Wait until application is started. Application is being served at address `http://localhost:5000`

### Testing

To run the tests execute the following command in your terminal:

```bash
$ python -m unittest
```

## API Reference

The Bookshelf API is organized around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer).


### Base URL

Currently Bookshelf API is not hosted as a base URL so can only run locally

```
http://127.0.0.1:5000/api
```

### Authentication

Currently Bookshelf API does not require any kind of authentication or API keys.

### Errors

Bookshelf uses conventional HTTP response codes to indicate the success of failure of an API request.

> Codes in the `2xx` range indicate success

> Codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted)

> Codes in the `5xx` range indicate an error with Bookshelf's servers (you'll rarely see one these)

#### Attributes

**success** `boolean`

`True` if was a successful request otherwise `False` when a failure occurred

<hr>

**error** `integer`

Error code which represents the error occurred

<hr>

**message** `string`

A human-readable message providing more detail about the error.

#### Example

```json
{
    "success": False,
    "code": 404,
    "message": "resource not found"
}
```

#### Possible errors

| error | message            |
|:------|:-------------------|
| 400   | bad request        |
| 404   | resource not found |
| 405   | method not allowed |
| 422   | unprocessable      |

### Library

#### Book

Book objects are the central resource, they form the bookshelf.

##### List all books

Returns a list of books. Results are paginated in groups of 8.

###### Parameters

`page` <small>optional</small>

Paginate the results starting from 1. The value must be a `integer`.

###### Returns

A `dictionary` with `books` property that contains of the maximum of 8 books. A `boolean` with `success` indicating if was a successful response and an `integer` with `total_books` counting the total of books regardless the pagination.

If there's no book because of the page submitted, this call returns a `404` [error](#Errors).

###### Request `GET` /books

```bash
curl http://127.0.0.1:5000/books
```

###### Response

```json
{
   "books":[
      {
         "author":"Stephen King",
         "id":1,
         "rating":5,
         "title":"The Outsider: A Novel"
      },
      {
         "author":"Lisa Halliday",
         "id":2,
         "rating":5,
         "title":"Asymmetry: A Novel"
      },
      {
         "author":"Kristin Hannah",
         "id":3,
         "rating":5,
         "title":"The Great Alone"
      },
      {
         "author":"Tara Westover",
         "id":4,
         "rating":5,
         "title":"Educated: A Memoir"
      },
      {
         "author":"Jojo Moyes",
         "id":5,
         "rating":5,
         "title":"Still Me: A Novel"
      },
      {
         "author":"Leila Slimani",
         "id":6,
         "rating":5,
         "title":"Lullaby"
      },
      {
         "author":"Amitava Kumar",
         "id":7,
         "rating":5,
         "title":"Immigrant, Montana"
      },
      {
         "author":"Madeline Miller",
         "id":8,
         "rating":5,
         "title":"CIRCE"
      }
   ],
   "success":true,
   "total_books":18
}
```

##### Create a book

Creates a new book using the submitted title, author and rating. All of them are mandatory.

###### Parameters

`title` <small>string</small>

The title or name of the book. The value must be a `string`.

<hr>

`author` <small>string</small>

The name of the author of the book. The value must be a `string`.

<hr>

`rating` <small>integer</small>

The current score of the book. The value must be a `integer` between 1 a 5.

###### Returns

A `dictionary` with `books` property that contains of the maximum of 8 books. A `integer` with `created` indicating the `ID` of the new created book, a `boolean` with `success` indicating if was a successful response and an `integer` with `total_books` counting the total of books regardless the pagination.

If something goes wrong given the parameters submitted, this call returns a `422` [error](#Errors).

###### Request `POST` /books

```bash
curl http://127.0.0.1:5000/books -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":5}'
```

###### Response

```json
{
   "books":[
      {
         "author":"Neil Gaiman",
         "id":24,
         "rating":5,
         "title":"Neverwhere"
      }
   ],
   "created":24,
   "success":true,
   "total_books":17
}
```

##### Update a book

Updates a rating of an existing book.

###### Parameters

`ID` <small>integer</small>

A `ID` of a existing book. The value must be a `integer`.

<hr>

`rating` <small>integer</small>

The updated score of the book. The value must be a `integer` between 1 a 5.

###### Returns

A `dictionary` with a `integer` with `updated` indicating the `ID` of the updated book and a `boolean` with `success` indicating if was a successful response.

If the book `ID` does not exist, this call returns a `404` [error](#Errors), or if something goes wrong given the parameters submitted, this call returns a `400` [error](#Errors).

###### Request `PATCH` /books

```bash
curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":1}'
```

###### Response

```json
{
   "updated":15,
   "success":true
}
```

##### Delete a book

Deletes an existing book given `ID` if it exists.

###### Parameters

`ID` <small>integer</small>

A `ID` of a existing book. The value must be a `integer`.

###### Returns

A `dictionary` with `books` property that contains of the maximum of 8 books. A `integer` with `deleted` indicating the `ID` of the deleted book, a `boolean` with `success` indicating if was a successful response and an `integer` with `total_books` counting the total of books regardless the pagination.

If the book `ID` does not exist, this call returns a `404` [error](#Errors), or if something goes wrong trying to delete the book, this call returns a `422` [error](#Errors).

###### Request `DELETE` /books

```bash
curl http://127.0.0.1:5000/books/16 -X DELETE
```

###### Response

```json
{
   "books":[
      {
         "author":"Gina Apostol",
         "id":9,
         "rating":5,
         "title":"Insurrecto: A Novel"
      },
      {
         "author":"Tayari Jones",
         "id":10,
         "rating":5,
         "title":"An American Marriage"
      },
      {
         "author":"Jordan B. Peterson",
         "id":11,
         "rating":5,
         "title":"12 Rules for Life: An Antidote to Chaos"
      },
      {
         "author":"Kiese Laymon",
         "id":12,
         "rating":1,
         "title":"Heavy: An American Memoir"
      },
      {
         "author":"Emily Giffin",
         "id":13,
         "rating":4,
         "title":"All We Ever Wanted"
      },
      {
         "author":"Jose Andres",
         "id":14,
         "rating":4,
         "title":"We Fed an Island"
      },
      {
         "author":"Rachel Kushner",
         "id":15,
         "rating":1,
         "title":"The Mars Room"
      }
   ],
   "deleted":16,
   "success":true,
   "total_books":15
}
```

## Authors
- Caryn McCarthy (@caryn_elisabeth)
- Filipe Bezerra de Sousa (filipebzerra@gmail.com)

## Acknowledgements
- My mentor Michael for his great support during all projects