import urllib2
from bs4 import BeautifulSoup
url = 'http://www.codechef.com/rankings/ACMKAN14'
page = urllib2.urlopen(url)
page = page.read()
soup = BeautifulSoup(page)
soup.prettify()
userranks = []
for anchor in soup.findAll('a', href=True):
    p = anchor['href']
    if "users/acm14kn" in p:
        userranks.append(p.split("/users/")[1])
         
i = 1
          
for arank in userranks:
            success = False
            while(not success):
                try:
                    teampage = urllib2.urlopen('http://www.codechef.com/teams/view/'+arank).read()
                    success = True
                except:
                    pass
            teamsoup = BeautifulSoup(teampage)
            tables = teamsoup.find_all("table", {"cellpadding":"0", "cellspacing":"0", "border":"0"})
            need = tables[1]
            res = need.find_all("td")
            needer = str(i) + " , " + res[3].get_text() + " , " + res[13].get_text()
            print(needer.encode('utf-8'))
            i = i+1
