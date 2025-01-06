# Task Tracker and Reminder System


This repository contains a **Task Tracker and Reminder System** implemented in Python. The system allows users to manage their daily tasks efficiently using a simple menu-driven interface. Users can add tasks, view them, mark tasks as completed, and delete tasks seamlessly.

---

## Key Features

1. **Add Task**
   - Users can add new tasks with a description.
   - Each task is stored with a status (default: `Pending`).

2. **View Tasks**
   - Displays all tasks in a structured format along with their current status.
   - Tasks are numbered for easy reference.

3. **Mark Task as Completed**
   - Allows users to update the status of a task to `Completed`.
   - Users select the task by its corresponding number.

4. **Delete Task**
   - Enables users to delete a task from the list by selecting its number.

5. **Interactive Menu-Driven Interface**
   - User-friendly menu for navigating and performing all task-related operations.

6. **Error Handling**
   - Handles invalid inputs and ensures robust functionality.

---

## Technologies Used

- **Programming Language:** Python
- **Concepts:**
  - Functions and modular programming
  - Lists and dictionaries for task management
  - Loops for iterating through tasks
  - `match-case` for clean control flow

---

## Code Highlights

### **Key Functions**
1. **`add_task(task_list)`**
   - Adds a new task to the list.
   - Sets the default status to `Pending`.

2. **`view_tasks(task_list)`**
   - Displays all tasks along with their current status.

3. **`mark_as_completed(task_list)`**
   - Updates the status of a selected task to `Completed`.

4. **`delete_task(task_list)`**
   - Deletes a selected task from the list.

5. **`mainMenu()`**
   - Provides an interactive menu for users to choose from various options.

---

## How to Run the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-tracker-reminder-system.git
