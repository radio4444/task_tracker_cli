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
add_task_parser.add_argument('add_task_name', help="Name of the tasks")

# Create "list" task command
list_task_parser = subparsers.add_parser('list', help="Listing all tasks")
list_task_parser.add_argument('list_status', choices=['todo', 'in-progress', 'done'], nargs='?', help='Listing by status')

# Create "delete" task command
delete_task_parser = subparsers.add_parser('delete', help="Delete a task")
delete_task_parser.add_argument('delete_id', type=int, help='Delete a task by Id')

# Create "update" task command
update_task_parser = subparsers.add_parser('update', help="Update the task name")
update_task_parser.add_argument('update_id', type=int, help='Update task by id')
update_task_parser.add_argument('update_task_name', help='New task name')

# Create "mark-in-progress" task command
mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark as: in-progress')
mark_in_progress_parser.add_argument('mark_in_progress_id', type=int,
                                     help="Mark the in-progress by id")

# Create "mark-done" task command
mark_done_parser = subparsers.add_parser('mark-done', help='Mark as: done')
mark_done_parser.add_argument('mark_done_id', type=int, help='Mark done by id')

# Parse the argument
args = main_parsers.parse_args()

# Create a file
fileName = 'all_tasks.json'

# Check if the command is 'add'
if args.command == 'add':
	# Create a task:
	task = {
		'id': 1,
		'description': args.add_task_name,
		'status': 'todo',
		'createAt': datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
	}

	# Check if the file does not exist
	if not os.path.exists(fileName):
		# Create a new JSON file and add the tasks_list in it
		with open(fileName, 'w') as file:
			json.dump([task], file, indent=4)

	else:
		# Read the JSON file and convert to python object
		with open(fileName, 'r') as file:
			tasks_lists = json.load(file)

		# Update the task id
		task['id'] = tasks_lists[-1]['id'] + 1
		# Append the task in tasks_list
		tasks_lists.append(task)

		# Update the file using the new tasks_list
		with open(fileName, 'w') as file:
			json.dump(tasks_lists, file, indent=4)

# Check if the command is 'list'
if args.command == 'list':
	# Read the JSON file and converted to python list
	with open(fileName, 'r') as file:
		tasks_lists = json.load(file)
	print(f"{'Id':<5}{'Description':<20}{'Status':^10}{'Created At':>18}")
	# check if the list choice set to: to-do
	if args.list_status == 'todo':
		for task in tasks_lists:
			if args.list_status == task['status']:  # Only display to-do tasks
				print(f"{task['id']:<5}{task['description']:<20}{task['status']:^10}{task['createAt']:>30}")

	# Check if the list choice set to: in-progress
	if args.list_status == 'in-progress':
		for task in tasks_lists:
			if args.list_status == task['status']: # Only display tasks that are in-progress
				print(f"{task['id']:<5}{task['description']:<20}{task['status']:^10}{task['createAt']:>30}")

	# Check if the list choice set to: done
	if args.list_status == 'done':
		for task in tasks_lists:
			if args.list_status == task['status']:
				print(f"{task['id']:<5}{task['description']:<20}{task['status']:^10}{task['createAt']:>30}")
	else:
		for task in tasks_lists:  # Display all the tasks
			print(f"{task['id']:<5}{task['description']:<20}{task['status']:^10}{task['createAt']:>30}")

# Check if the command is 'delete'
if args.command == 'delete':
	# Read the JSON file
	with open(fileName, 'r') as file:
		tasks_lists = json.load(file)
	# Traverse the tasks_list
	for task in tasks_lists:
		# check if the delete id match with task id
		if args.delete_id == task['id']:
			tasks_lists.remove(task)  # remove the task from the list
	# Update the JSON file using the tasks_lists
	with open(fileName, 'w') as file:
		json.dump(tasks_lists, file, indent=4)

# Check if the command is 'update'
if args.command == 'update':
	# Read the JSON file
	with open(fileName, 'r') as file:
		tasks_lists = json.load(file)  # Store converted python list in tasks_lists
	# Traverse the tasks_lists
	for task in tasks_lists:
		# Check if the update id match with task id in task list
		if args.update_id == task['id']:
			task['description'] = args.update_task_name  # Update the task name

	# Update the JSON file using this new tasks_lists
	with open(fileName, 'w') as file:
		json.dump(tasks_lists, file, indent=4)

# Check if the command is 'mark-in-progress'
if args.command == 'mark-in-progress':
	# Read the JSON file and convert it to python list
	with open(fileName, 'r') as file:
		tasks_lists = json.load(file)
	# Traverse the list
	for task in tasks_lists:
		# Check if the mark_in_progress_id match with the task id
		if args.mark_in_progress_id == task['id']:
			task['status'] = 'in-progress'  # update the task's statue: in-progress
	# Update the JSON file using the new tasks_lists
	with open(fileName, 'w') as file:
		json.dump(tasks_lists, file, indent=4)

# Check if the command is 'mark-done'
if args.command == 'mark-done':
	# Read the JSON file and convert it to Python List
	with open(fileName, 'r') as file:
		tasks_lists = json.load(file)
	# Traverse the tasks_lists
	for task in tasks_lists:
		# check if the mark_done_id match with the tasks
		if args.mark_done_id == task['id']:
			task['status'] = 'done'  # Update the status to done
	# Update the JSON file using the new tasks_lists
	with open(fileName, 'w') as file:
		json.dump(tasks_lists, file, indent=4)
