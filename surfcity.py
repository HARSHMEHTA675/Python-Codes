import requests
from bs4 import BeautifulSoup

base_url = "https://www.surfcity.com/search?find_desc=Restaurants&find_loc="
loc = "Newport+Beach,+CA"
page = 10



url = base_url + loc + "&start=" + str(page)


surfcity_r = requests.get(url)
surfcity_soup = BeautifulSoup(surfcity_r.text, "html.parser")


businesses = surfcity_soup.findAll("div", {"class": "biz-listing-large"})

for biz in businesses:
    #print(biz)
    title = biz.findAll("a", {"class": "biz-name"})[0].text
    print(title)
    address = biz.findAll("address")[0] 
    print(address)
    print("\n")
    phone = biz.findAll("span", {"class": "biz-phone"})[0].text
    print(phone)



file_path = "surfcity-{loc}.txt".format(loc=loc)

with open(file_path, "a") as textfile:
    businesses = surfcity_soup.findAll("div", {"class": "biz-listing-large"})
    for biz in businesses:
      
        title = biz.findAll("a", {"class": "biz-name"})[0].text
        print(title)
        address = biz.findAll("address")[0] 
        print(address)
        print("\n")
        phone = biz.findAll("span", {"class": "biz-phone"})[0].text
        print(phone)
        page_line = "{title}\n{address}\n{phone}\n\n".format(
                title=title,
                address=address,
                phone = phone
            )
        textfile.write(page_line)

print(surfcity_soup.findAll("li", {"class": "regular-search-result"}))


print(surfcity_soup.findAll("a", {"class": "biz-name"}))

for name in surfcity_soup.findAll("a", {"class": "biz-name"}):
    print(name.text)

print(surfcity_r.status_code)




print(surfcity_soup.prettify())
print(surfcity_soup.findAll("a", {}))

for link in surfcity_soup.findAll("a"):
    print(link)
