# Helper functions

def read_coordinates(file_path):
    """
    Function reads input from txt file and returns as an array of floats.
    """
    with open(file_path) as f:
        line = f.readline()
        arr = line.replace("[", "").replace("]", "").replace(" ", "").split(",")
    return [ float(x) for x in arr ]
