import { useState, useEffect } from "react";
import "./App.css";
import { fetchTodos } from "./requests/getData.js";
import { createTodo, deleteTodo } from "./requests/handleTodo.js";
import { updateTodoStatus } from "./requests/updateTodo.js";

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");
  const [isCreating, setIsCreating] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  
  const [filteredTodos, setFilteredTodos] = useState([]);

  useEffect(() => {
    fetchTodos(setTodos);
  }, []);

  useEffect(() => {
    handleSearch();
  }, [searchTerm, todos]);

  const handleSearch = () => {
    const searchedTodos = todos.filter(todo => 
      todo[1].toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredTodos(searchedTodos);
  };

  const toggleCreateMode = () => setIsCreating((prev) => !prev);

  return (
    <div id="main">
      <div id="box">
        <button onClick={toggleCreateMode}>
          {isCreating ? "Close" : "New Item"}
        </button>
        <input 
          type="text" 
          placeholder="Search Todos"
          value={searchTerm} 
          onChange={(e) => setSearchTerm(e.target.value)} 
        />
        {!isCreating ? (
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>To-Do</th>
                <th>Created At</th>
                <th>Finished</th>
                <th>Edit</th>
              </tr>
            </thead>
            <tbody>
              {filteredTodos.map((todo) => (
                <tr key={todo[0]}>
                  <td>{todo[0]}</td>
                  <td>{todo[1]}</td>
                  <td>{new Date(todo[2]).toLocaleDateString()}</td>
                  <td>
                    <input
                      type="checkbox"
                      checked={todo[3]}
                      onChange={(e) => updateTodoStatus(e, todo[1], !todo[3], setTodos, setIsCreating)}
                    />
                  </td>
                  <td>
                    <button
                      onClick={(e) => deleteTodo(e, todo[1], setTodos)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <form onSubmit={(e) => createTodo(e, newTodo, setTodos, setIsCreating)}>
            <label>To-Do</label>
            <input
              type="text"
              placeholder="New Item"
              value={newTodo}
              onChange={(e) => setNewTodo(e.target.value)}
              required
            />
            <button type="submit">Create</button>
          </form>
        )}
      </div>
    </div>
  );
}

export default App;
