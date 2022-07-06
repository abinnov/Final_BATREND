import datetime

HOST='localhost'
USER='root'
PASSWORD=''
DATABASE='trend'
SCRIPT_FILE_PATH="/home/maram/PFE/Analyse des tendances/web scraping/script.sh"
FB_FILE_PATH="/home/maram/PFE/Analyse des tendances/web scraping/facebook.py"
YT_FILE_PATH="/home/maram/PFE/Analyse des tendances/web scraping/youtube.py"
CSV_FILE_PATH="/home/maram/PFE/Analyse des tendances/web scraping/"+datetime.date.today().strftime("%Y-%m-%d")+".csv"

DATE_MIN = datetime.datetime(2022, 4, 18)

DEVELOPER_KEY = "AIzaSyDRMyTjsP3BOeyDrf1qfO4yBn7B-GZRLxs"
API_VERSION="v3"