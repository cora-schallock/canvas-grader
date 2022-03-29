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


### Trouble Shooting:
If you encounter an error along the lines of this: https://community.canvaslms.com/t5/Canvas-Developers-Group/User-not-authorized-to-perform-that-action/td-p/181632

Make sure the assignment is published, as you are not able to upload these unless the assignment is publised.
