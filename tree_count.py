from pathlib import Path
import argparse

def dir_with_count(start_dir: str):
    start_dir = Path(start_dir)
    dir_count = list()
    objects = start_dir.glob("*")
    n_files = 0
    for o in objects:
        if o.is_dir():
            # Recurse until we get to the end and report back
            child_counts = dir_with_count(o)
            dir_count.extend(child_counts)
        else:
            n_files += 1
    if n_files > 0:
        dir_count.extend([{"dir" : start_dir, "n_files" : n_files}])
    return(dir_count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Print tree of subdirectories with number of files'
    )
    parser.add_argument('dir', metavar='dir', type=str, nargs='?', default=".",
                    help='Starting directory')
    args = parser.parse_args()
    out = dir_with_count(args.dir)
    for idx in out: print((f""" {idx["dir"]} : {idx["n_files"]} """).strip())
    