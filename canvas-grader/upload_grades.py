from canvasapi import Canvas

from constants import CANVAS_URL, COURSE_CODE, PATH_TO_CANVAS_KEY_FILE, ID_KEY, STUDENT_KEY, ID_KEY, SIS_USER_ID_KEY, SIS_LOGIN_ID_KEY, SECTION_KEY
from process_gradebook import standardize

def get_scores_for_students(data_frame,output_comment_folder,score_key="Score",assignment_name="assignment",upload_comments=True):
    id_to_score_dict = dict()
    id_to_comment_path_dict = dict()
    
    for index, row in df_grades.iterrows():
        student="*missing name*" #incase error and missing name
        
        try:
            student = row[STUDENT_KEY]
            the_id = row[ID_KEY]
            sis_login_id = row[SIS_LOGIN_ID_KEY]
            score = row[SCORE_KEY]
            
            if upload_comments:
                id_to_comment_path_dict[the_id] = comment_file_path(output_comment_folder,sis_login_id,assignment_name)
                
            id_to_score_dict[the_id] = standardize(score)
            
        except Exception as e:
            print("Error while getting score/comment for student={}, {}".format(student,e))
            
    return id_to_score_dict, id_to_comment_path_dict

def upload_scores(id_to_score_dict, id_to_comment_path_dict,upload_comments=True, print_upload_id=True):
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_CODE)
    
    for the_id in id_to_score_dict:
        try:
            if print_upload_id:
                print(the_id)
                
            submission.edit(submission={'posted_grade': id_to_score_dict[the_id]})
            
            if upload_comments:
                submission.upload_comment(file=id_to_comment_path_dict[the_id])
                
        except Exception as e:
            print("error for {}".format(user_id))
            print(e)

            