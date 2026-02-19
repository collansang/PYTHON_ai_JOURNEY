def prompt(text):#standardizes input format to avoid inputing .strip everywhere
    return input(text + "\n>").strip()


def  prompt_float(text, min_val= None, max_val=None):
    while True:
        try:
            value = float(prompt(text))
            if min_val is not None and value < min_val:
                raise ValueError
            if max_val is not None and value> max_val:
                raise ValueError
            return value
        except ValueError:
            print("Invalid number Try again")
            
def prompt_list(text, separator=","):
    raw = prompt(text)
    return [item.strip() for item in raw.split(separator) if item.strip()]#split,clean, remove empty values