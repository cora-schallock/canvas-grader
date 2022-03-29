from canvasapi import Canvas

from canvas_grader.constants import CANVAS_URL, COURSE_CODE, PATH_TO_CANVAS_KEY_FILE, ID_KEY, STUDENT_KEY, ID_KEY, SIS_USER_ID_KEY, SIS_LOGIN_ID_KEY, SECTION_KEY
from canvas_grader.process_gradebook import standardize
from canvas_grader.file_helpers import get_canvas_key, comment_file_path

def get_scores_for_students(data_frame,output_comment_folder,score_key="total",assignment_name="assignment",upload_comments=True):
    id_to_score_dict = dict()
    id_to_comment_path_dict = dict()
    
    for index, row in data_frame.iterrows():
        student="*missing name*" #incase error and missing name
        
        try:
            student = row[STUDENT_KEY]
            the_id = row[ID_KEY]
            sis_login_id = row[SIS_LOGIN_ID_KEY]
            score = row[score_key]
            
            if upload_comments:
                id_to_comment_path_dict[the_id] = comment_file_path(output_comment_folder,sis_login_id,assignment_name)
                
            id_to_score_dict[the_id] = standardize(score)
            
        except Exception as e:
            print("Error while getting score/comment for student={}, {}".format(student,e))
            
    return id_to_score_dict, id_to_comment_path_dict

def upload_scores(id_to_score_dict, id_to_comment_path_dict, assignmment_number, upload_comments=True, print_upload_id=True):
    CANVAS_TOKEN = get_canvas_key()
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_CODE)
    assignment = course.get_assignment(assignmment_number)
    submissions = assignment.get_submissions()
    
    for submission in submissions:
        user_id = "*missing id*" #for exception
        try:
            user_id = submission.user_id
        
            if user_id in id_to_score_dict:
                submission.edit(submission={'posted_grade': id_to_score_dict[user_id]})
            else:
                #print("{} not found".format(user_id))
                pass
            
            if upload_comments and user_id in id_to_score_dict:
                submission.upload_comment(file=id_to_comment_path_dict[user_id])
            else:
                #print("{} not found".format(user_id))
                pass
        except Exception as e:
            print("error for {}".format(user_id))
            print(e)
                
        

            