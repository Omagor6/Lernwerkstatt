# Readme

This project provides a starting point for implementing the backend of the application. 

The endpoint `get /students/` is fully implemented as an example: All the information on students is read from the person table and returned if the endpoint is called. (Add example data for a student to test this!) 

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

   ![Database Setup Screenshot](.\resources\psql_tool.png)

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

_Hint: If the execution of PoserShell scripts is disabled on your system, you might get a PSSecurityException. You can run the following command to disable the security restrictions 
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

5. Start the application with uvicorn:
`uvicorn api:app --reload`

## Database Design

   ![ERD](.\resources\erd.png)
