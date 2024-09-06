from flask import Flask,jsonify,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
]

class Book(Resource):
    def get(self,book_id):
        for book in books:
            if book['id']==book_id:
                return jsonify(book)
        return 'failed getting book details'
    
    def put(self,book_id):
        for book in books:
            if book['id']==book_id:
                data=request.get_json()
                book.update(data)
                return jsonify(books)
        return 'error updating data'
    
    def delete(self,book_id):
        for book in books:
            if book['id']==book_id:
                books.remove(book)
                return "deleting book success"
        return "failed deleting book"
    



class Booklist(Resource):
    def get(self):
        return jsonify(books)
    
    def post(self):
        try:
            newdata=request.get_json()
            books.append(newdata)
            return jsonify(books)
        except:
            return "error posting data"
    
    
api.add_resource(Book,'/book/<int:book_id>')
api.add_resource(Booklist,'/book')
if __name__=='__main__':
    app.run(debug=True)
