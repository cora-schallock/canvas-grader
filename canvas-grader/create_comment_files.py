from constants import STUDENT_KEY, ID_KEY, SIS_USER_ID_KEY, SIS_LOGIN_ID_KEY, SECTION_KEY
from file_helpers import write_to_file
from process_gradebook import standardize

def constuct_comment(student,sis_login_id,section,assignment_name,row,header_dict):
    the_comment = []
    
    the_comment = [assignment_name]
    the_comment.append("\Section:{}".format(section))
    the_comment.append("\t-Submitted By: {} ({})".format(student,sis_login_id))
    the_comment.append("")
    
    for col_name in header_dict:
        the_comment.append('{}: {}'.format(header_dict[col_name],standardize(row[col_name])))
            
    return the_comment

def create_comment_files(data_frame,output_comment_folder,header_dict={},assignment_name="assignment"):
    for index, row in df_grades.iterrows():
        student="*missing name*" #incase error and missing name
        
        try:
            student = row[STUDENT_KEY]
            sis_login_id = row[SIS_LOGIN_ID_KEY]
            section = row[SECTION_KEY]
        
            the_comment = constuct_comment(student,sis_login_id,section,assignment_name,row,header_dict)
        
            comment_path = comment_file_path(output_comment_folder,sis_login_id,assignment_name)
            write_to_file(comment_path,the_comment)
        except Exception as e:
            print("Error while creating comment for student={}, {}".format(student,e))