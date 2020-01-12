import os
from flask import Flask, request, abort, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy #, or_
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8

# @TODO: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  # CORS Headers
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  # @TODO: Write a route that retrivies all books, paginated.
  #         You can use the constant above to paginate by eight books.
  #         If you decide to change the number of books per page,
  #         update the frontend to handle additional books in the styling and pagination
  #         Response body keys: 'success', 'books' and 'total_books'
  # TEST: When completed, the webpage will display books including title, author, and rating shown as stars
  @app.route('/books')
  def get_books():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF
    selection = Book.query.order_by(Book.id).all()
    formatted_books = [book.format() for book in selection]
    books = formatted_books[start:end]

    if books is None:
        return abort(404)

    return jsonify({
      'success': True,
      'books': books,
      'total_books': len(selection)
    })

  # @TODO: Write a route that will update a single book's rating.
  #         It should only be able to update the rating, not the entire representation
  #         and should follow API design principles regarding method and route.
  #         Response body keys: 'success'
  # TEST: When completed, you will be able to click on stars to update a book's rating and it will persist after refresh
  @app.route('/books/<int:book_id>', methods=['PATCH'])
  def update_rating(book_id):
    book_found = Book.query.filter_by(id=book_id).first()

    if book_found is None:
        return abort(404)

    try:
        if not 'rating' in request.get_json():
            abort(make_response(jsonify(message='You have to specify rating value in the range 1 to 5')))

        book_rating = request.get_json().get('rating', 1)
        book_found.rating = book_rating
        book_found.update()

        return jsonify({
          'success': True,
          'updated': book_found.id
        })
    except:
        abort(400)

  # @TODO: Write a route that will delete a single book.
  #        Response body keys: 'success', 'deleted'(id of deleted book), 'books' and 'total_books'
  #        Response body keys: 'success', 'books' and 'total_books'

  # TEST: When completed, you will be able to delete a single book by clicking on the trashcan.
  @app.route('/books/<int:book_id>', methods=['DELETE'])
  def delete_book(book_id):
    book_found = Book.query.filter_by(id=book_id).first()

    if book_found is None:
        return abort(404)

    book_found.delete()
    selection = Book.query.all()
    formatted_books = [book.format() for book in selection]

    return jsonify({
      'success': True,
      'deleted': book_id,
      'books': formatted_books,
      'total_books': len(formatted_books)
    })


  # @TODO: Write a route that create a new book.
  #        Response body keys: 'success', 'created'(id of created book), 'books' and 'total_books'
  # TEST: When completed, you will be able to a new book using the form. Try doing so from the last page of books.
  #       Your new book should show up immediately after you submit it at the end of the page.
  @app.route('/books', methods=['POST'])
  def create_book():
    book_json = request.get_json()
    title = book_json.get('title', None)
    author = book_json.get('author', None)
    rating = book_json.get('rating', 1)

    if not title or not author:
        return abort(make_response(jsonify(message='Title and author fields are required'), 400))

    try:
        new_book = Book(title=title, author=author, rating=rating)
        new_book.insert()

        selection = Book.query.all()
        formatted_books = [book.format() for book in selection]

        return jsonify({
          'success': True,
          'created': new_book.id,
          'books': formatted_books,
          'total_books': len(formatted_books)
        })
    except:
        abort(422)

  return app
