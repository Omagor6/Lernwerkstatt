# Readme

This project provides a starting point for implementing the backend of the application. 

There are several endpoints that are fully implemented:

- `get /students/`: All the information on students is read from the person table and returned if the endpoint is called. (Add example data for a student in the DB to test this!) 

- The endpoint `post /goals/{student_id}`: Is used to create a a new goal. 

- The endpoint `get /goals/{student_id}`: The created goals of a student can be retrieved again.

Currently not all implemented endpoints access the database yet. Mock data is returned for the endpoints accessed by the frontend. This functionality needs to be extended. 

## Setup

### Database

#### Prerequisites

- PostgreSQL is installed on your machine  
  _(This project uses PostgreSQL 16)_
- pgAdmin 4 is installed  
  _(Required to follow the steps below)_

#### Setup Instructions

1. Open **pgAdmin 4**
2. Under the user **postgres**, open the **PSQL Tool**

   ![Database Setup Screenshot](.\psql_tool.png)

3. Execute the script “app\db\create_db_with_role.sql" on the user postgres. This will create the database "lernwe_local".


   `\i 'Path to your repo \\Lernwerkstatt\\db\\create_db_with_role.sql'`

   _Hint: If you are not working on windows you might need change the \\ to //._


4. Connect to the newly created database "lernwe_local" and execute the script “app\db\create_tables.sql".


   `\c lernwe_local`

   `\i 'Path to your repo \\Lernwerkstatt\\db\\create_tables.sql'`


5. Refresh the database in pgAdmin 4 and check that the database has been successfully created. You should now be able to view the different tables.

   _Hint: You might want to install a tool like DBeaver to visualize the tables with the data._

## Backend (Python)

#### Prerequisites
- Python is installed on your machine. For this project python 3.12.0 was used.

#### Setup Instructions

1. Open A terminal in the cloned git repository. 

2. Create a virtual environment executing the following command:

`python -m venv venv`

This will create a folder "venv" in your repository. 

3. Activate your virtual environment. 
**Windows**: Execute the following command:

`.\venv\Scripts\activate`

_Hint: If the execution of PowerShell scripts is disabled on your system, you might get a PSSecurityException. You can run the following command to disable the security restrictions 
for the current session. 

`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

**MacOS:** Try executing the following_command:
`source venv/bin/activate`
If the command fails with a permission denied error, you have to type in:
`nano ~/.zshrc`
Inside this document, you have to add the following line:
`export VIRTUAL_ENV_DISABLE_PROMPT=`
Now the command should work:
`source venv/bin/activate`

4. Install the required packages using _pip install ..._.
  - uvicorn
  - psycopg2
  - fastapi

5. Start the application with uvicorn, make sure that you are in the backend-folder:
`uvicorn api:app --reload`

## Database Design

   ![ERD](.\erd.png)

   **person**

   This table contains all the information of a person. Persons can have different roles: `student`, `mentor` and `coach`. A student has an `apprenticeship`, mentor and coach do not.
   The password of a person will be stored here to. It needs to be hashed - plaintext is not secure.

   **subject**

  In a semester a student can have different subjects they take. The semester is identified by the first day of the semester. The grades are stored as JSON. That way it is possible to store the grades and the weight a specific grade has, since not every exam counts equally.

  **goal**

  Students have goals with a description and a grading (typically 1-4, meaning may vary depending on type). There are different types of goals. Currently only individual goals are implemented. Depending on the type of goal different mentors can view the goals (e.g. noly coach can access). 

  **absence**

  A mentor (e.g. BB) can register an absence of a student. The absence_time specifies half-day a student was absent: 
  - date + 08:00:00 if the student was absent in the morning
  - date + 12:00:00 if the student was absent in the afternoon

  **has_contact**

  This table specifies which contacts a student has in the contact book. A student can have any number of contacts.

  **student_mentor**

  This table specifies which mentor (coach or BB) is "responsible" for a student during a specific period. 

  ## Architecture

  This backend uses a layered architecture: 

  **Controller**

  FastApi - a python web-framework - is used to implement the endpoints. 

  **Service**

  For more complex requests, that require data from multiple layers and tables, a service layer is used to make the code more readable and well structured. 

  **Repository and DB access manager**

  The repositories access or persist the the data in the database. For this the db_access_manager is used to provide easy and generic access to the database: There is a function for executing a query that updates existing data or creates a new entry - optionally parameters can be set in the query. The second function is used to fetch data. In this case the data is returned as a dict. In addition the DB access manager ensures consistent error handling.


  ## Authorization and Access Management

  These are functiontalities have not been implemented yet. With FastApi this can be added.