import { fetchTodos } from "./getData";

export const createTodo = async (e, todoItem, setter, setIsCreating) => {
  e.preventDefault();
  try {
    const response = await fetch(`/api/v1/create`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ todo: todoItem }),
    });
    if (response.ok) {
      console.log(`Server responded with code ${response.status}`)
      await fetchTodos(setter);
      setIsCreating(false);
    } else {
      console.error(`Error creating todo: ${response.status}`);
    }
  } catch (error) {
    console.error('Error creating todo:', error);
  }
};


export const deleteTodo = async (e, todoItem, setter) => {
  e.preventDefault();
  try {
    const response = await fetch(`/api/v1/delete`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ todo: todoItem }),
    });
    if (response.ok) {
      console.log(`Server responded with code ${response.status}`)
      fetchTodos(setter);
    } else {
      console.error(`Error deleting todo: ${response.status}`);
    }
  } catch (error) {
    console.error('Error deleting todo:', error);
  }
};
