export const fetchTodos = async (setter) => {
  try {
    const response = await fetch('/api/v1/todos');
    if (response.ok) {
      console.log(`Server responded with code ${response.status}`)
      const data = await response.json();
      setter(data);
    } else {
      console.error(`Error fetching todos: ${response.status}`);
    }
  } catch (error) {
    console.error('Error fetching todos:', error);
  }
};
