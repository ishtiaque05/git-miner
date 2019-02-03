from subprocess import check_output
import os
import argparse

def cli():

  parser = argparse.ArgumentParser(description="Find the commit statistic in particular file")
  parser.add_argument(
    'filename',
     type=str,
     help="Input filename or directory to find the commit stats"
  )
  parser.add_argument(
    'keywords',
    type=str,
    default="",
    nargs='?',
    help="Search file or directory for particular substring"
  )

  return parser.parse_args()

def main():
  args = cli()

  if os.path.exists(args.filename):
    target_file_contributors(args.filename, args.keywords)
    get_specific_contributors(args.filename, args.keywords)
    no_directory_given(args.filename, args.keywords)
  else:
    print("File or directory not found!")

def target_file_contributors(filename, keywords):
  if filename and not keywords:
    star_performers(filename)

def no_directory_given(filename, keywords):
  if os.path.isfile(filename) and keywords:
    print("Please input directory instead instead of filename to search for particular keyword")

def get_specific_contributors(filename, keywords):
  if keywords and os.path.isdir(filename):
    files = sub_string_search(keywords, os.path.realpath(filename))
    print("Contributors of file containing keyword {} \n".format(keywords))
    output_all_contributors(files)

def output_all_contributors(files):
  if (len(files) > 1):
    for path in files:
      print("In file path: {}\n".format(path))
      star_performers(path)
      print("\n\n")
  else:
    star_performers(files[0])

def star_performers(filename):

  command = ["git", "log", "--follow", "--format=%cn", "--", filename]
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

  print("Total number of commits in {} : {}".format(filename, total_commits))
  print("--------------------------------------------------------------------------")

  for i, (key, value) in enumerate(desc_sorted_stats):
    print("Contributor number: {}".format(i+1))
    print("Name: {}".format(key))
    print("Number of Commits: {}".format(value))
    print("Percentage (Commit/Total Commit): {}".format((value/total_commits)*100))
    print("--------------------------------------------------------------------------")


def sub_string_search(keyword, filepath_to_search = os.path.realpath(__file__)):
  root_dir = filepath_to_search # path to the root directory to search
  found_files = []

  for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
    for filename in files:  # iterate over the files in the current dir
      file_path = os.path.join(root, filename)  # build the file path
      try:
        with open(file_path, "rb") as f:  # open the file for reading
          # read the file line by line
          for line in f:  # use: for i, line in enumerate(f) if you need line numbers
            try:
              line = line.decode("utf-8")  # try to decode the contents to utf-8
            except ValueError:  # decoding failed, skip the line
              continue
            if keyword in line:  # if the keyword exists on the current line...
              found_files.append(file_path)
              break  # no need to iterate over the rest of the file
      except (IOError, OSError):  # ignore read and permission errors
        pass

  return found_files


if __name__ == '__main__':
    main()
