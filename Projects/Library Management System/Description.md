# Library Management System

This project demonstrates a simple **Library Management System** implemented in Python. The library has functionality to:

- Add books
- List all books
- Get the total number of books

The program does not persist data, meaning the list of books will reset when the program is restarted.

---

## Features

1. **Add Books**: Add new books to the library collection.
2. **Print All Books**: Display all books currently in the library.
3. **Get Number of Books**: View the total number of books in the library.
4. **Volatile Storage**: Books are stored only in memory and do not persist between program runs.

---

## How to Run

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed (version 3.7 or higher recommended).
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the script:
   ```bash
   python library.py
   ```
5. Follow the prompts to add, view, or interact with the library.

---

## Example Usage

```bash
> python library.py
Book "The Great Gatsby" added to the library.
Book "To Kill a Mockingbird" added to the library.
Book "1984" added to the library.
Books in the library:
1. The Great Gatsby
2. To Kill a Mockingbird
3. 1984
Number of books in the library: 3

Exiting the program. Restart the program to see the state reset.
```

---

## Limitations

- **No Persistence**: The library does not save books after the program ends.
- **Manual Execution**: The program needs to be restarted to reset the library state.

---