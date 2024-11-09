from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DB_URL'))
    return conn

@app.route('/api/v1/todos')
def get_todo_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todos;')
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(todos) 

@app.route('/api/v1/create', methods=['POST'])
def create():
    if request.method == 'POST':
        data = request.json  
        todo = data.get('todo')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO todos (todo) VALUES (%s)',
            (todo,)
        )
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Todo added successfully'}), 201
    

@app.route('/api/v1/update', methods=['PATCH'])
def update():
    if request.method == 'PATCH':
        data = request.json
        todo = data.get('todo')
        is_finished = data.get('isFinished')  

        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(
            'UPDATE todos SET isFinished = %s WHERE todo = %s',
            (is_finished, todo)
        )
        
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Todo updated successfully'}), 200


@app.route('/api/v1/delete', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        data = request.json
        todo = data.get('todo')
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(
            'DELETE FROM todos WHERE todo = %s',
            (todo,)
        )
        
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Todo deleted successfully'}), 200
    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

        
    
        
