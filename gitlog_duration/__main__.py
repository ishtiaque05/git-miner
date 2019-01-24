from subprocess import check_output
import argparse

def cli():
  parser = argparse.ArgumentParser(description="This script print the time spent in a feature")
  parser.add_argument(
    'author',
     type=str,
     default='current_author',
     nargs='?',
     help="Name of the author to find time spent by him in a feature"
  )
  return parser.parse_args()

def main():
  args = cli()
  print(args.author)

if __name__ == '__main__':
    main()
