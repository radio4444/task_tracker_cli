import argparse
import json
import os
from datetime import datetime
# Create a main parser
main_parsers = argparse.ArgumentParser(description="Task Tracker using CLI")

# Create a subparser
subparsers = main_parsers.add_subparsers(dest="command")

# Create "add" task command
add_task_parser = subparsers.add_parser('add', help="Add a task")
add_task_parser.add_argument('task_name', help="Name of the tasks")

# Parse the argument
args = main_parsers.parse_args()

if args.command == 'add':
	# Create a task:
	task = {
		'description': args.task_name,
		'status': 'todo',
		'createAt': datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
	}
	# Create a file
	fileName = 'all_tasks.json'
	# Check if the file does not exist
	if not os.path.exists(fileName):
		# Create a new JSON file and add the tasks_list in it
		with open(fileName, 'w') as file:
			json.dump([task], file, indent=4)

		print(f"Output: Task added successfully: {task}")
	else:
		# Read the JSON file and convert to python object
		with open(fileName, 'r') as file:
			tasks_list = json.load(file)

		# Append the task in tasks_list
		tasks_list.append(task)

		# Update the file using the new tasks_list
		with open(fileName, 'w') as file:
			json.dump(tasks_list, file, indent=4)

		print(f"Output: Task added successfully: {tasks_list}")
