import snscrape.modules.twitter as tScraper
import pandas as pd
import csv

def run():
    twitter=["Rassemblement_National","RNational_off","mouvementDémocrate","URMoDem","LaRépubliqueEnMarche","Republiqueenmarche"]
    for t in twitter:
        scraper = tScraper.TwitterHashtagScraper(t)
        print(scraper.get_items())
        for i , tweet in enumerate(scraper.get_items()):
            print(tweet.content)

    #df = pd.DataFrame(tweets, columns=["content","date"])
    #df.to_csv(config.path_to_data, mode='a', index=False)
run()