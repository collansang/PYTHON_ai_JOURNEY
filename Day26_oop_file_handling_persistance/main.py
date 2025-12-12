from pathlib import Path #think of it as a navigation system to guide to a specific path


LOG_DATA  = Path("my_fol/log.txt")#means log.txt is a file inside data folder

def ensure_parent(path : Path)-> None:
    path.parent.mkdir(parents = True, exist_ok = True)
            # path.parent means:
                # If the file is “data/log.txt”
                # The parent is the folder “data”
            # .mkdir(..., exist_ok=True) means:
                # “Hey computer, please make this folder if it does not already exist.”
                # “If it DOES exist, don’t get angry — it’s okay.”
        
def append_line(path : Path, line: str)->None:
    ensure_parent(path)#makes sure that the folder exist
    try:
        with path.open("a", encoding = "utf-8")as f:
            f.write(line.rstrip('\n')+'\n')
    except (PermissionError, OSError) as e:
        raise RuntimeError(f"Cannot write to path {path} : {e}") from e
    
        # “Open the notebook”
        # "a" means APPEND, not erase
            # (like turning to the LAST page and writing there)
        # encoding="utf-8" means:
            # Write letters in the normal way, so everyone understands
        # with means:
            # When I’m done writing, close the notebook automatically.
            
        #  rstrip("\n") removes extra newlines
            # so you don’t accidentally create blank spaces
        # Then we add ONE newline
            # so every line is neatly separated.           

def read_lines(path: Path)->list[str]:
    if not path.exists():#If notebok not created, return empty list
        return []
    try:
        with path.open("r", encoding = "utf-8")as f:
            return[line.rstrip("\n") for line in f]#kills new line format
    except (PermissionError,OSError) as e:
        raise RuntimeError(f"Cannot read from {path}  {e}") from e
    
def stream_line(path : Path):
    #streaming= holding one line in memory at a time. unlike reading holds the entire data which is unfavourable when dealing with big data
    try:
        with path.open("r", encoded = "utf-8")as f:
            for line in f:#iterate over each line
                yield line.rstrip("\n")#yield gives you one line then pauses then continues next time you ask(line generator)
    except (PermissionError, OSError) as e:
        raise RuntimeError(f"Cannot read from {path} : {e}") from e
    
if __name__ == "__main__":
    append_line(LOG_DATA, "FIRST LOGO ETRY")
    append_line(LOG_DATA, "SECOND LOG ENTRY")
    for i in read_lines(LOG_DATA):
        print("LINE :", i)