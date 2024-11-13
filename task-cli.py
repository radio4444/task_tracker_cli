import argparse
import json
import os
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
		'description': args.task_name
	}
	# Store all the tasks in the list
	tasks_list = [task]
	# Create a file
	fileName = 'all_tasks.json'
	if not os.path.exists(fileName):
		# Create a new JSON file and add the tasks_list in it
		with open(fileName, 'w') as file:
			json.dump(tasks_list, file, indent=4)
	else:
		# Read the file
		with open(fileName, 'r') as file:
			tasks_list_json = json.load(file)

		# Append the task in it.
		tasks_list_json.append(task)

		# Update the file using the new task list
		with open(fileName, 'w') as file:
			json.dump(tasks_list_json, file, indent=4)

	print(f"Output: Task added successfully: {tasks_list}")
