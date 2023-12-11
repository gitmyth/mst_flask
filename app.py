from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# Sample data - list of books
books = [
    {'id': 1, 'title': 'Flask 101', 'author': 'John Doe'},
    {'id': 2, 'title': 'Python Web Development', 'author': 'Jane Smith'}
]

@app.route('/books', methods=['GET'])
def get_books():
    return render_template('book_list.html', books=books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return render_template('book_detail.html', book=book)
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def create_book():
    new_book = {'id': len(books) + 1, 'title': request.form['title'], 'author': request.form['author']}
    books.append(new_book)
    return redirect(url_for('get_books'))

@app.route('/books/new', methods=['GET'])
def add_book_form():
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)

