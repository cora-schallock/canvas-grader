# canvas-grader
Automatically upload information to canvas gradebook

Required Libraries: canvasapi, pandas

## Part 1 - Setup:
Before you can begin using the Canvas API, you'll need to setup the permissions.

### Step #1:
Go to canvas, click "Account" and then click "Settings"


![alt text](https://github.com/cora-schallock/canvas-grader/blob/main/documentation/setup_1_canvas.png?raw=true)


### Step #2:
Scroll down to the "Approved Integrations" section and click the button that says "New Access Token"

![alt text](https://github.com/cora-schallock/canvas-grader/blob/main/documentation/setup_2_new_access_token.PNG?raw=true)

### Step #3:
Enter a name and an expiration date

![alt text](https://github.com/cora-schallock/canvas-grader/blob/main/documentation/setup_3_create_key.PNG?raw=true)

### Step #4:
A new page will pop up with your token.

**Important:** Copy this token (before closing this pop up) and paste it into a text file.

![alt text](https://github.com/cora-schallock/canvas-grader/blob/main/documentation/setup_4_copy_key.png?raw=true)

**Important:** This is an API key, do not share this with anyone. The key above in the documentation is a "dummy key"


## Part 2 - Getting Class Roster
Once you have setup your Canvas API key, you will need to download a copy of your canvas course roster.

### Step 1:
On the course page, click "Gradebook"

### Step 2:
Click "Actions" and then in the drop down menu select "Export"
This may take a few moments but it will download a CSV file of the Course's Roster.

### Step 3:
Open this csv file, and delete evything **except** the following columns:
Student	ID	SIS User ID	SIS Login ID	Section

### Step 4: 
Delete the row that says "Points Possible"

### Step 5:
If you see any additional blank rows or rows that contain a fictious student (for example "Test Student") remove those rows as well

### Step 6:
Save this csv file as you will need this to create additional assignments.

## Part 3 - Creating a gradebook
Now that you have saved the class roster as a csv, you can a gradebook for an assignment.

A gradebook is a csv file that contains the score/ rubric information for a particular assignment. 

**Important** The gradebook must begin with class roster (i.e. it needs the following columns Student	ID	SIS User ID	SIS Login ID	Section on the far left of the sheet).


You can add additional columns that contain notes from the grader or scores.
Every column should have a one row header. (Note: you can edit it using an excel sheet but when you are ready to upload grades, you must download it to a .csv file). 


The only other reuirment is that you have a cummulative score column. Remember what this column is titled, as you will need it later on when you speciy the `score_key` variable (see example notebook).

## Part 3 - Uploading grades from comments
The code peforms the following when you upload grades:
* Reads the gradebook, and creates a unique comment file for each student
* Reads the gradebook, and get the score of the assignment
* Uploads both the score and comment for each student

For this section, I will be following the example notebook, so please refer to the example.ipynb file for more information.

## Step 1:
**Important** You must update these variables in canvas-grader/constants.py before uploading grades: `CANVAS_URL`, `COURSE_CODE`, and `PATH_TO_CANVAS_KEY_FILE`
* `CANVAS_URL` is your school's canvas URL (i.e. the site you go to for your canvas homepage. Hint: For most school's it will end in the domain of your school). If you need help find these, refer to the Canvas Documentation (note: I believe in the [documentation](https://community.canvaslms.com/t5/Canvas-Question-Forum/Where-do-I-get-the-api-url/m-p/141868/highlight/true#M57059) this is called: yourschool.instructure.com).
* `COURSE_CODE` is your courses canvas code. This can be found by going to your course's canvas home page and looking at the number after courses. (For example if your courses url is "https://canvas.eee.uci.edu/courses/44461/" then the `COURSE_CODE` is 44461). **Important**: This must be passed to the Canvas object as an integer.
* `PATH_TO_CANVAS_KEY_FILE` is the path to the txt file where you saved your canvas api key from [Part 1](`PATH_TO_CANVAS_KEY_FILE`)

## Step 2:
Once you have gradebook ready to be uploaded as a csv file, save it somewhere on your computer where you can easily find it. The path to this file is the `csv_path` in the notebook.

## Step 3:
Define your `comment_output_path` variable. This is the the path to the folder where each student's comments will be saved. By default, the txt file that will be created for each student will be saved in with the file name {sis_login}_{assignment_name}.txt (no curly brackets), see comment_file_path funtion in canvas-grader/file_helpers.py.


## Step 4:
Now you need to read in your gradebook csv file. You can do this by using the lines:
```
df_grades = read_csv(csv_path)
headers = get_headers(df_grades)
```





### Trouble Shooting:
If you encounter an error along the lines of this: https://community.canvaslms.com/t5/Canvas-Developers-Group/User-not-authorized-to-perform-that-action/td-p/181632

Make sure the assignment is published, as you are not able to upload these unless the assignment is publised.
