# USE YOUTUBEDL

import webbrowser as wb
from youtubesearchpython import Search
import pprint

song = input("Enter the name of the song: ")
url = "+".join(song.split())
url = "https://www.youtube.com/results\?search_query=" + url
# wb.open(url)
allSearch = Search(url, limit=1)

# pprint.pprint(allSearch.result())
print(allSearch["result"])
if "url" in allSearch:
    print(True)
