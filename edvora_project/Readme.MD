INTRODUCTION

- This project is a feed system using FastAPI and Socket.IO to manage a session
- It display all the names of users active in the session.
- It requires a user to pass query_string 'username' and 'password' to access the session.
- The password is 'admin'
- The user can logout by passing query_string 'username' to /logout end-point.

eg: - API END POINT(GET)
     - http://3.7.213.105:7863/login?username=Rahul&password=admin ,
     - http://3.7.213.105:7863/logout?username=Rohan
 
APP STRUCTURE
 
  main.py
 
  socket_server.py
			
  README.md
  
  requirements.txt
  
  
GETTING STARTED

- Change to the project directory: cd .\edvora_project
- If you want to use virtualenv: virtualenv venv
                                 venv\scripts\activate
- Install dependencies with pip: pip install -r requirements.txt

- Then, run the application:
		- python socket_server.py
		- python main.py
		
To test the  application, access this url in postman:

	http://localhost:7863
	

