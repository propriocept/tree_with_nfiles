from pathlib import Path
import argparse

def dir_with_count(start_dir: str):
    # Initialise variables. directories is a list of all found directories.
    # n_files is the number of files in the current directory.
    directories = list()
    n_files = 0
    # Convert starting directory (start_dir) to pathlib.Path format to allow
    # easy access of file list and if a file is a directory.
    start_dir = Path(start_dir)
    objects = start_dir.glob("*")
    
    for o in objects:
        if o.is_dir():
            # Recurse until we get to the end, and then report back all
            # sub-directories and the number of files
            child_counts = dir_with_count(o)
            directories.extend(child_counts)
        else:
            # It is a file, increment the counter
            n_files += 1

    if n_files > 0:
        # If we had any files, add the number of files along with the 
        # directory name to the list.
        directories.extend([{"dir" : start_dir, "n_files" : n_files}])
    return(directories)

if __name__ == "__main__":
    # Get command line arguments
    parser = argparse.ArgumentParser(
        description='Print tree of subdirectories with number of files'
    )
    parser.add_argument('dir', metavar='dir', type=str, nargs='?', default=".",
                    help='Starting directory')
    args = parser.parse_args()
    # Get the tree list with number of files in each sub-directory.
    out = dir_with_count(args.dir)
    # Print out everything
    for idx in out: print((f""" {idx["dir"]} : {idx["n_files"]} """).strip())
