import requests
# allows us to use the html and grab different data to scrape it
from bs4 import BeautifulSoup
# for a cleaner printed data
import pprint

res = requests.get('https://news.ycombinator.com/news') # url that we want to grab the data from
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser') # ac e un html si vreau sa il parsez / exsta mai multe parsari lxml/html
soup2 = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')

links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) #sort the dict by votes

def create_custom_hn(links, subtext):

    hn = [] #empty list
    for idx, item in enumerate(links): # enum links for using both lists links&subtext
        title = links[idx].getText()   # title is equal with name of each site
        href= links[idx].get('href', None) # grab the links too
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points',' ')) # grab the votes
            # were problems because sometimes the links doesn't have votes
            if points > 99 :
                hn.append({'title':title, 'link':href, 'votes':points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))



