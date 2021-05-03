from bs4 import BeautifulSoup

with open("./website.html", encoding="utf-8") as file:
    contents = file.read()

# print(type(contents))

soup = BeautifulSoup(contents, "html.parser")

# print(type(soup))
# print(soup)
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


# # First anchor
# print(soup.a) 

# # First paragraph
# print(soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# print(type(all_anchor_tags))

all_paragraph_tags = soup.find_all(name="p")
# print(all_paragraph_tags)


# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(".heading")
# print(headings)