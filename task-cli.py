import argparse

parser = argparse.ArgumentParser(description="Basic Examples of ArgParse.")
parser.add_argument('name', help='Your name')
parser.add_argument('-a', '--age', type=int, help='Your age', required=True)
parser.add_argument('--color', choices=['red', 'blue', 'green'], default='blue', help='Pick a color')
parser.add_argument('--verbose', action='store_true', help='Enable verbosity')

args = parser.parse_args()

print(f"Hello, {args.name}, You are {args.age} years old")

print(f"Chosen Color: {args.color}")
if args.verbose:
	print("Verbose mode is on")
