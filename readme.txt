To start this program, run
    python main.py

To add a profile, make a POST request to:
    http://127.0.0.1:5000/users
The fields of a profile are passed as URL parameters. 
To insert the following user...
  {
    "education": 0, 
    "experience": 10, 
    "name": "Alan Ritter", 
    "position": "Dog", 
    "score": 10, 
    "skills": [
      "Computer Science", 
      "Woof"
    ], 
    "summary": "Woof!", 
    "title": "Doggy",
    "username": "0"
  }
]

...send a POST request to 
http://127.0.0.1:5000/users/add?username=0&name=Alan%20Ritter&position=Dog&education=0&summary=Woof!&title=Doggy&experience=10&skills=Computer%20Science,Woof

To search a profile, make a GET request to:
    http://127.0.0.1:5000/users/search
name, position, title, summary, and skills are searchable by passing any number of those fields as URL parameters