import requests
url = 'http://organicdrop.in:8050/droidbrain/send/email/json/'

data =[{"email":"markdsilva10@gmail.com",
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






    
