from facebook_scraper import get_posts
import csv
import sys
import config
import datetime

def run(id_source, page):
    for p in get_posts(page, pages=1000, cookies='from_browser', options={"comments": True, "posts_per_page": 200}):
        date=p['time']
        if(date<config.DATE_MIN):
            break
        if(date>=config.DATE_MIN):
            for x in p['comments_full']:
                if x['comment_time']== None:
                    comment_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                else:
                    comment_time=x['comment_time']
                comment=x['comment_text']
                with open(config.CSV_FILE_PATH, 'a', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow([comment_time, comment, id_source])
                print(comment_time, comment, id_source)
if __name__ == "__main__":
    run(int(sys.argv[1]), sys.argv[2])
'''python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '1' 'LeNouvelObservateurPolitique' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '2' 'lemonde.fr.politique' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '3' 'RassemblementNational' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '4' 'cpolitique' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '5' 'lefigaro' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '6' 'causeur' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '7' 'LutteOuvriere1' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '8' 'anticapitaliste.presse' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '9' 'poutou.philippe' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '10' 'nathaliearthaud' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '11' 'Particommuniste' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '12' 'FabienRoussel2022' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '13' 'lafranceinsoumise' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '14' 'JLMelenchon' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '15' 'FranceInsoumiseLeforest' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '16' 'partisocialiste' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '17' 'HidalgoAnne' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '18' 'eelv.fr' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '19' 'yjadot' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '20' 'EnMarche' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '21' 'EmmanuelMacron' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '22' 'mouvementdemocrate' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '23' 'bayrou' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '24' 'HorizonsLeParti' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '25' 'edouardphilippelh' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '26' 'les.Republicains.FR' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '27' 'vpecresse' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '28' 'chjacob77' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '29' 'profile.php?id=100044532395333' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '30' 'jeanchristophe.lagarde.3' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '31' 'reconquete2022' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '32' 'ZemmourEric' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '33' 'MMLPen.officiel' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '34' 'JordanBardella' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '35' 'dlf.officiel' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '36' 'nicolasdupontaignan' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '37' 'udi' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '38' 'MvtLesPatriotes' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '39' 'franceinter' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/facebook.py' '40' 'lepoint.fr' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '41' 'UCeWMp4Frgyv275gSnWNYoZQ' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '42' 'UCIMGfEAERXjmWwQeg15BFsg' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '43' 'UCi1h68Fys0apnhLaJ-ijQOw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '44' 'UCCDz_XYeKWd0OIyjp95dqyQ' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '45' 'UCO6K_kkdP-lnSCiO3tPx7WA' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '46' 'UCUzk9hBisz4aSMVTl37pWgw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '47' 'UCZsh-MrJftAOP_-ZgRgLScw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '48' 'UCSwPcnzaMTuDcTgjRiJvZnw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '49' 'UCKHKSD-yanY2ZwwU_4Tgf0w' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '50' 'UCk-_PEY3iC6DIGJKuoEe9bw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '51' 'UCo7xGEOV-RfxOAxRfhlR3Ww' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '52' 'UCB8Q3N-nvX1YlMUL7Zl_16w' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '53' 'UCJw8np695wqWOaKVhFjkRyg' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '54' 'UCFqGa9uitcB-fWyNZK2xImw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '55' 'UCfHWZNJQ7wZpG_cL9ukYX1Q' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '56' 'UC3Ma4tRFxx85oZI_XKVTPwg' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '57' 'UCXAKlEXGwoavQuOMaNBeaXw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '58' 'UCcsw3rWMB_E73VEm_hoS36w' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '59' 'UCfA5DnCDX3Ixy5QOAMGtBlA' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '60' 'UC3U0VIDgANFaXeOAtt1m5Mw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '61' 'UCjTbZBXEw-gplUAnMXLYHpg' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '62' 'UCJldRgT_D7Am-ErRHQZ90uw' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '63' 'UCwupzUX-SYyt3y4yx8cYdpg' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '64' 'UCQd5LYcykaFeZtjDaP3bNSA' 
python3 '/home/maram/PFE/Analyse des tendances/web scraping/youtube.py' '65' 'UClaa_CwoQEmSo9Mb_M1f91g'

'''
