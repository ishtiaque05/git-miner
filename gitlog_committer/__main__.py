from subprocess import check_output
import argparse

def cli():
  parser = argparse.ArgumentParser(description="Find the commit statistic in particular file")
  parser.add_argument(
    'filename',
     type=str,
     help="Input filename or directory to find the commit stats"
  )
  return parser.parse_args()

def main():
  args = cli()

  command = ["git", "log", "--follow", "--format=%cn", "--", args.filename]
  commit_history = check_output(command)

  committer_arr = commit_history.decode('ascii').split('\n')
  committer_arr = list(filter(None, committer_arr))

  stats = {}
  total_commits = len(committer_arr)
  for line in committer_arr:
    if line in stats:
      stats[line] += 1
    else:
      stats[line] = 1

  desc_sorted_stats = sorted(stats.items(), key=lambda kv: kv[1], reverse=True)

  print("Total number of commits in {} : {}".format(args.filename, total_commits))
  print("--------------------------------------------------------------------------")

  for i, (key, value) in enumerate(desc_sorted_stats):
    print("Contributor number: {}".format(i+1))
    print("Name: {}".format(key))
    print("Number of Commits: {}".format(value))
    print("Percentage (Commit/Total Commit): {}".format((value/total_commits)*100))
    print("--------------------------------------------------------------------------")

if __name__ == '__main__':
    main()
