from datetime import datetime
from itertools import dropwhile, takewhile
from instaloader import Instaloader, Profile
import mysql.connector
import os 
username="mariem_consulting"
password='MC-mdp2020'
L= Instaloader(download_comments=True,sleep=True, quiet=False, user_agent=None, dirname_pattern=None, filename_pattern=None, download_pictures=False, download_videos=False, download_video_thumbnails=False, compress_json=False)
L.login(username,password)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = "123456789",
    database = "Trends_analysis"
)
mycursor = db.cursor()
instagram=[]
mycursor.execute('select name from source where id_type=4;')
for x in mycursor:
    instagram.append(x[0])


search_user = "marine_lepen"

for search_user in instagram:
    posts=Profile.from_username(L.context,search_user).get_posts()

    SINCE = datetime(2022,4,18)
    UNTIL = datetime(2022,5,20)

    for post in takewhile(lambda p:p.date > SINCE,dropwhile(lambda p:p.date > UNTIL ,posts)):
        L.download_post(post,search_user)
        print(L.download_post(post,search_user))
