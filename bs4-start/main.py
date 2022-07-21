#import smtplib
from bs4 import BeautifulSoup
import requests











# response = requests.get("https://news.ycombinator.com/news")

# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, 'html.parser')
# articles = soup.find_all(name='a', class_='titlelink')
# article_text = []
# article_link = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     link = article_tag.get('href')
#     article_text.append(text)
#     article_link.append(link)
#
# article_upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name='span', class_='score')]
#
# #
# max_upvotes = max(article_upvotes)
# max_index = article_upvotes.index(max_upvotes)
#
# # print(article_link[max_index])
# # print(article_text[max_index])
# # print(article_upvotes[max_index])
#
# with smtplib.SMTP('smtp.gmail.com') as server:
#     server.starttls()
#     server.login('gen2proff@gmail.com', 'gen2;soul')
#     server.sendmail(
#         'gen2proff@gmail.com',
#         'tobiadebiyi17@gmail.com',
#         msg=f"Subject:Hacker news!\n\n{article_text[max_index]}\n\n{article_link[max_index]}"
#     )


























# #import lxml
# with open('website.html', encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.name)  #this print out the string and the content
# # print(soup.title.string)    #this print the content of the string
# # print(soup.title)   #this print the tag
#
# # print(soup) #print the html in the console
# # print(soup.prettify()) #indent the html in the console
# #
# # all_anchor_tags = soup.find_all(name='a')
# # all_list_tags = soup.find_all(name='li')
# # print(all_anchor_tags)
# # print(all_list_tags)
#
# #getting the link text
# #
# # for tag in all_anchor_tags:
# #     print(tag.getText()) #link text
# #     print(tag.get('href')) #href link
#
# heading = soup.find(name='h1', id='name')
# print(heading)


# section_heading = soup.find(name='h3',class_='heading') # put class_
# print(section_heading.getText())
#
# #if you want to selfect a tag in another t
#
# company_url = soup.select_one(selector='p a')
# print(company_url.get('href'))

