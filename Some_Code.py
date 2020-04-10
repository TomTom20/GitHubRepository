"""Some Code."""


def Some():
    """Some."""
    some = ["S", "o", "m", "e"]
    Some = ""
    for SOME in some:
        Some += SOME
    return Some


def Code():
    """Code."""
    code = 1
    CODE = -code
    if code * CODE == -code:
        Code = "Code"
    return Code


def Some_Code(Some, Code):
    """Some Code."""
    print(f"{Some}" + " " + f"{Code}")


Some_Code(Some(), Code())
