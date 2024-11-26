from bs4 import BeautifulSoup
with open("website.html") as file:
    content=file.read()
    soup=BeautifulSoup(content,"html.parser")
    # print(soup)
    # print(soup.title)
    # print(soup.title.text)
    # print(soup.prettify())
#     print(soup.a)
#     all_anchor_tags=soup.find_all(name="a")
#     print(all_anchor_tags)
#     for tag in all_anchor_tags:
#         print(tag.get("href"))
# heading =soup.find(name="h1",id="name").getText
# print(heading)
all_link_elements=soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper a")
all_links=[link["href"] for link in all_link_elements]
for link in all_links:
    print(link)