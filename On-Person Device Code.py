from firebase import Firebase
import sys
import requests
config = {
    "apiKey": "AIzaSyBkQ5z8Rs5IRP4lHoiWyXV9XVQHjAh-sEI",
    "authDomain": "a-eye-for-the-blind.firebaseapp.com",
    "storageBucket": "a-eye-for-the-blind.appspot.com",
    "databaseURL": "https://a-eye-for-the-blind-default-rtdb.firebaseio.com/",
}
uid = "EUzyQOAmWJY7F3IuZrajTUOp1aE3" #unique user ID, must set before running
email = 'saranggoel06@gmail.com'
password = 'breadcake73'
firebase = Firebase(config)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

if uid == "" or email == "" or password == "":
    print("Please set user UID, email, or password in the lines above!")
    sys.exit()

user = auth.sign_in_with_email_and_password(email, password)
user = auth.refresh(user['refreshToken'])
data = {"3": "Joe Tilsed"}
db.child(f"users/{uid}").child("images").update(data)
storage.child("images/example.jpg").put("D:/A-Eye For The Blind/2dtodepth/outfile/test_image.jpg", user['idToken'])
storage.child("images/example.jpg").download("D:/A-Eye For The Blind/2dtodepth/outfile/downloaded.jpg", user['idToken'])


