# Task Tracker CLI

Task Tracker CLI is a command-line tool for managing tasks efficiently. It provides functionalities for adding, updating, listing, deleting, and marking tasks as in-progress or done. All tasks are saved in a JSON file for persistence.

This project was developed as part of the [Task Tracker project](https://roadmap.sh/projects/task-tracker) on the Roadmap.sh platform.

## Features

### Task Operations:
- **Add Task**: Create a new task with a description and an auto-generated unique ID.
- **List Tasks**: View all tasks or filter tasks by status (`todo`, `in-progress`, `done`) with neatly formatted output.
- **Update Task**: Update the description of an existing task using its ID.
- **Delete Task**: Remove a task from the list using its ID.
- **Mark In-Progress**: Change the status of a task to `in-progress`.
- **Mark Done**: Change the status of a task to `done`.

### Robust Error Handling:
- Handles cases where the task file is missing or empty, ensuring the application runs smoothly.
- Provides clear and actionable error messages for invalid operations.

### Persistence:
- Tasks are saved in a JSON file (`all_tasks.json`) for reuse across sessions.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd task-tracker-cli
   ```
2. Ensure Python 3.7+ is installed on your system.

3. Install necessary dependencies (if applicable).

---

## Usage

### Commands Overview:

| Command               | Description                                        |
|-----------------------|----------------------------------------------------|
| `add`                | Add a new task with a description.                 |
| `list`               | List tasks by status or view all tasks.            |
| `delete`             | Delete a task by its unique ID.                    |
| `update`             | Update the description of a specific task.         |
| `mark-in-progress`   | Mark a task as in-progress by its ID.              |
| `mark-done`          | Mark a task as done by its ID.                     |

### Command Syntax and Examples:

#### Add a Task:
```bash
python task_tracker.py add "Buy groceries"
```

#### List All Tasks:
```bash
python task_tracker.py list
```

#### List Tasks by Status:
```bash
python task_tracker.py list todo
```

#### Update a Task:
```bash
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

#### Delete a Task:
```bash
python task_tracker.py delete 1
```

#### Mark a Task as In-Progress:
```bash
python task_tracker.py mark-in-progress 1
```

#### Mark a Task as Done:
```bash
python task_tracker.py mark-done 1
```

---

## JSON File Format

All tasks are stored in a file named `all_tasks.json`. Below is an example structure:

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createAt": "2024-11-22 02:15:45 PM"
    },
    {
        "id": 2,
        "description": "Complete Python project",
        "status": "in-progress",
        "createAt": "2024-11-22 03:00:10 PM"
    }
]
```

---

## Development

Feel free to contribute to this project. Follow the steps below to get started:

1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes with descriptive messages:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your branch and create a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.