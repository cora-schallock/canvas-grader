from canvas_grader.constants import STUDENT_KEY, ID_KEY, SIS_USER_ID_KEY, SIS_LOGIN_ID_KEY, SECTION_KEY
from canvas_grader.file_helpers import write_to_file, check_if_folder_exists_and_create, comment_file_path
from canvas_grader.process_gradebook import standardize

#comment:
def constuct_comment(student,sis_login_id,section,assignment_name,row,header_dict,score_key="total"):
    the_comment = []
    
    the_comment = [assignment_name]
    the_comment.append("\tSection:{}".format(section))
    the_comment.append("\t\t-Submitted By: {} ({})".format(student,sis_login_id))
    the_comment.append("")
    
    for col_name in header_dict:
        the_comment.append('{}: {}'.format(header_dict[col_name],standardize(row[col_name])))
        
    the_comment.append("Total Score: {}".format(standardize(row[score_key])))
            
    return the_comment

def create_comment_files(data_frame,output_comment_folder,header_dict={},score_key="total",assignment_name="assignment"):
    check_if_folder_exists_and_create(output_comment_folder)
    
    for index, row in data_frame.iterrows():
        student="*missing name*" #incase error and missing name
        
        try:
            student = row[STUDENT_KEY]
            sis_login_id = row[SIS_LOGIN_ID_KEY]
            section = row[SECTION_KEY]
        
            the_comment = constuct_comment(student,sis_login_id,section,assignment_name,row,header_dict,score_key="total")
        
            comment_path = comment_file_path(output_comment_folder,sis_login_id,assignment_name)
            write_to_file(comment_path,the_comment)
        except Exception as e:
            print("Error while creating comment for student={}, {}".format(student,e))
            
            
#seating:
def constuct_seat_comment(student,sis_login_id,section,assignment_name,row,header_dict,room_string=""):
    the_comment = []
    
    the_comment = [assignment_name]
    the_comment.append("\tSection:{}".format(section))
    the_comment.append("\t\t-Student: {} ({})".format(student,sis_login_id))
    the_comment.append("")
    
    for col_name in header_dict:
        the_comment.append('{}: {}'.format(header_dict[col_name],standardize(row[col_name])))
        
    the_comment.append("Information: {}".format(room_string))
            
    return the_comment

def create_seat_comment_files(data_frame,output_comment_folder,header_dict={},room_string="",assignment_name="assignment"):
    check_if_folder_exists_and_create(output_comment_folder)
    
    for index, row in data_frame.iterrows():
        student="*missing name*" #incase error and missing name
        
        try:
            student = row[STUDENT_KEY]
            sis_login_id = row[SIS_LOGIN_ID_KEY]
            section = row[SECTION_KEY]
        
            the_comment = constuct_seat_comment(student,sis_login_id,section,assignment_name,row,header_dict,room_string)
        
            comment_path = comment_file_path(output_comment_folder,sis_login_id,assignment_name)
            write_to_file(comment_path,the_comment)
        except Exception as e:
            print("Error while creating comment for student={}, {}".format(student,e))