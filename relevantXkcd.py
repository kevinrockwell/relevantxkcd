import webbrowser

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
