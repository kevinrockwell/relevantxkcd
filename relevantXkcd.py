import webbrowser
from googlesearch import search

url = "https://xkcd.com/"
searchType = input("Do you want to search by NUMBER or by PHRASE?").lower()

if searchType == "number":
    comicNumber = input("What is the number of the comic you want to search?")
    try:
        int(comicNumber)
        url = (f'{url}{comicNumber}')
        webbrowser.open_new(url)
    except:
        print("An error occured. Perhaps you didn't enter an integer, or you don't have a recognized web browser, or dark magic interfered. The world may never know.")
        webbrowser.open_new("https://xkcd.com/2200/")
elif searchType == "phrase":
    referencePhrase = input("What is the relevant phrase?")
    results = input("How many xkcds would you like to search for?")
    query = ("site:xkcd.com " + str(referencePhrase))
    try:
        num = int(results)
        for i in search(query, tld="co.in", num=num, stop=num, pause=5):
            str(i)
            webbrowser.open_new(i)
    except:
        print("An error occured. Perhaps you didn't enter an integer for the number of searches, or you don't have google, or maybe its all my fault and I really am a disappointment like my parents said.")
        webbrowser.open_new("https://xkcd.com/2200/")
else:
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


