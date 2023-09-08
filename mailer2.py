import requests

def mail():
    url = 'http://organicdrop.in:8050/droidbrain/send/email/json/'

    data =[{
    "email":"markdsilva10@student.sfit.ac.in",
    "name":"FallDetection",
    "auth_email":"markdsilva10@gmail.com", 
    "subject":"Fall detected",
    "message":"A fall has been detected on the feed from camera 1"
    }, {"email":"markdsilva10@gmail.com",
"name":"lol",
"auth_email":"markdsilva10@gmail.com",
"subject":"PATIENT UPDATE",
"message":"PLEASE CHECK YOU PATIENTT STATUS"}, {"email":"pmchaudhari106@gmail.com",
"name":"lol",
"auth_email":"pmchaudhari106@gmail.com",
"subject":"PATIENT UPDATE",
"message":"PLEASE CHECK YOU PATIENTT STATUS"}]

    for obj in data:
        x = requests.post(url, data = obj)






    
