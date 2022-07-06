from clean_data import clean_data
import sys

def run(model, comment):
    comment=clean_data().clean(comment)
    resultat=model.predict([comment])
    resultat=resultat.tolist()[0]
    i= resultat.index(max(resultat))
    if i+1 ==9:
        return -1
    else:
        return i+1
if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])