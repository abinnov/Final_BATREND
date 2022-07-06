import mysql.connector
import pandas as pd
import os
import config
import csv
import utilis

def run():
    with open(config.CSV_FILE_PATH, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'comment', 'id_source'])

    info=pd.read_sql_query("select * from source", utilis.connexion())

    fb_page = dict(zip(info[ info['id_site'] == 1 ]['id_source'], info[ info['id_site'] == 1 ]['source_name']))
    yt_chaine = dict(zip(info[ info['id_site'] == 2 ]['id_source'], info[ info['id_site'] == 2 ]['source_name']))
    print(yt_chaine)
    if os.path.exists(config.SCRIPT_FILE_PATH):
        os.remove(config.SCRIPT_FILE_PATH)
    fichier = open(config.SCRIPT_FILE_PATH, "a")
    fichier.write("#!/bin/bash \n")

    for page in fb_page.items():
        fichier.write("python3 '"+config.FB_FILE_PATH+"' '"+str(page[0])+"' '"+page[1]+"' \n")

    for chaine in yt_chaine.items():
        fichier.write("python3 '"+config.YT_FILE_PATH+"' '"+str(chaine[0])+"' '"+chaine[1]+"' \n")

    os.system("chmod u+x '"+config.SCRIPT_FILE_PATH+"'")
    fichier.close()

if __name__ == "__main__":
    #run()
    all=pd.read_csv("/home/maram/PFE/Analyse des tendances/web scraping/2022-04-30.csv")
    print(all)

