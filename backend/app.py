from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='todo_db',
                            user=os.getenv('USER_NAME'),
                            password=os.getenv('PASSWORD')
    )
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
        todo_id = data.get('id')
        is_finished = data.get('isFinished')  


        if todo_id is None or is_finished is None:
            return jsonify({'error': 'ID and isFinished status are required'}), 400

        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(
            'UPDATE todos SET isFinished = %s WHERE id = %s',
            (is_finished, todo_id)
        )
        
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Todo updated successfully'}), 200


@app.route('/api/v1/delete', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        data = request.json
        todo_id = data.get('id')
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(
            'DELETE FROM todos WHERE id = %s',
            (todo_id,)
        )
        
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Todo deleted successfully'}), 200
    
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

        
    
        
