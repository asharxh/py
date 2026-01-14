import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ur service")
firebase_admin.initialize_app(cred, {
    'databaseURL': "ur database"
})

ref = db.reference('Students')

data = {
    "22081A0520":
        {
            "name": "Ashar Arif",
            "major": "B.Tech CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-07-11 00:54:34"
        },
    "22081A0553":
        {
            "name": "Ashfaq Hussain",
            "major": "B.Tech CSE",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2024-07-11 00:54:34"
        },
    "22081A0594":
        {
            "name": "Mohammad Sahbaz Uddin",
            "major": "B.Tech CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-07-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)