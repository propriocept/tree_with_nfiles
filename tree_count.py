#%%
from pathlib import Path
import pandas as pd

#%%

root_dir = Path("/", "Users", "Anil", "Onedrive", "Documents", "Raw photos - Copy")

# %%
def dir_with_count(start_dir: Path):
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


# %%
def main():
    out = dir_with_count(root_dir)
    for idx in out: print((f""" {idx["dir"]} : {idx["n_files"]} """).strip())

if __name__ == "__main__":
    main()