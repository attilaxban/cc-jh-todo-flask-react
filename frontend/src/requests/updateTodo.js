import { fetchTodos } from "./getData";

export const updateTodoStatus = async (e, todoItem, newState, setter) => {
  e.preventDefault();
  try {
    const response = await fetch(`/api/v1/update`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ isFinished: newState, todo: todoItem }),
    });
    if (response.ok) {
      console.log(`Server responded with code ${response.status}`)
      fetchTodos(setter);
    } else {
      console.error(`Error updating todo status: ${response.status}`);
    }
  } catch (error) {
    console.error('Error updating todo status:', error);
  }
};
