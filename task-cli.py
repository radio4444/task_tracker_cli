import argparse

# Create main parser
parser = argparse.ArgumentParser(description="Basic Examples of ArgParse.")

# Create subparser object
subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

# Create the "greet" command
greet_parser = subparsers.add_parser('greet', help='Display name and age')
greet_parser.add_argument('name', help='Your name')
greet_parser.add_argument('-a', '--age', type=int, help='Your age', required=True)

# Create the "choice" command
choice_parser = subparsers.add_parser('choice', help='Display color option and verbose')
choice_parser.add_argument('--color', choices=['red', 'blue', 'green'], default='blue', help='Pick a color')
choice_parser.add_argument('--verbose', action='store_true', help='Enable verbosity')

# Parse the arguments
args = parser.parse_args()

if args.command == 'greet':
	print(f"Hello, {args.name}, You are {args.age} years old")

if args.command == 'choice':
	print(f"Chosen Color: {args.color}")
	if args.verbose:
		print("Verbose mode is on")

