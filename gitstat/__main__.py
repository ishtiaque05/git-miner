from subprocess import check_output
import argparse

def cli():
  parser = argparse.ArgumentParser(description="This script returns top contributors sorted by number of commits")
  parser.add_argument('number', type=int, default=0, nargs='?', help="Return top n contributors")
  parser.add_argument('number', type=int, default=0, nargs='?', help="Return top n contributors")
  return parser.parse_args()

def main():
  args = cli()
  sort_by_commit = check_output("git shortlog -ns --no-merges".split())
  number = args.number

  if number:
    rank = sort_by_commit.decode("ascii").split('\n')[0:number]
  else:
    rank = sort_by_commit.decode("ascii").split('\n')

  for line in rank:
    print(line)

if __name__ == '__main__':
    main()
