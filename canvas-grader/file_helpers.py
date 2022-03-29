import os
import pandas as pd

from constants import PATH_TO_CANVAS_KEY_FILE

#functions for reading in CANVAS key:
def get_canvas_key():
    """gets canvas api key from text file specified in constants.py"""
    key = ""
    with open(PATH_TO_CANVAS_KEY_FILE) as f:
        key = str(f.read())
    return key

#functions for reading/writing/processing files:
def read_csv(path_to_csv):
    return pd.read_csv(path_to_csv)

def write_to_file(file_path,to_write):
    with open(file_path, "w") as outfile:
        outfile.write("\n".join(to_write))
        
def comment_file_path(output_comment_folder,sis_login,assignment_name):
    file_name = "{}_{}.txt".format(sis_login,assignment_name)
    return os.path.join(output_comment_folder,file_name)