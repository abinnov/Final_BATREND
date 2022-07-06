import os, json
from datetime import date
import pandas as pd
import config 
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = "123456789",
    database = "Trends_analysis")
mycursor = db.cursor(buffered=True)

os.chdir("./")

    
# Returns the current local date
today = date.today()
for root,dirs, fichier in os.walk(".", topdown = False):
    print(root[2:])
    s=root[2:]
    req='select id_source from source where (id_type=4 and name="%s");' % s
    mycursor.execute(req)
    # print(mycursor)
    for x in mycursor:
        id_source=x[0]
    path_to_json = os.path.join(".",root)
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    comments=[]
    for file in json_files:
        date_post = file[:10]
        #print(date_post)
        with open(os.path.join(path_to_json,file), 'r') as f:
            data = json.load(f)
            for dictionary in data :
                print(dictionary)
                comments.append((dictionary['text'],today,date_post,id_source))


    print(comments)
    #df = pd.DataFrame(comments, columns=["comment","date_extraction","date_publication","id_source"])


    #df.to_csv(config.instagram_csv_file_path, mode='a', index=False)   
