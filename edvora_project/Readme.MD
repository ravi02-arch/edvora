INTRODUCTION

- This project is a feed system using FastAPI and Socket.IO to manage a session
 
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
	
API END POINT(POST)
	- /login
	- /logout
