# html_doc = """
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, "html.parser")
# try:
#     print(soup.a.text)
# except KeyError as e:
#     print("KeyError:", e)
# except Exception as e:
#     ex_type, ex_value, ex_traceback = sys.exc_info()
#     print("Exception:", ex_traceback.tb_frame.f_code.co_filename)
#     print("Exception:", e)


# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import urllib.request


# def names(element):
#     if element.parent.name in ["script", "head", "title", "meta", "[document]"]:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True


# def text(body):
#     soup = BeautifulSoup(body, "html.parser")
#     texts = soup.findAll(text=True)
#     visible_texts = filter(names, texts)
#     return "".join(t.strip() for t in visible_texts)


# html = urllib.request.urlopen("https://en.wikipedia.org/wiki/Scrappage_program").read()
# print(text(html))

# links = []
# query = "hospital"
# try:
#     page = get_page(query)
#     # print(page)
#     soup = get_soup(page)
#     # print(soup.prettify())
#     links = get_links(page)
# except AttributeError as e:
#     print("AttributeError:", e)
# except Exception as e:
#     print("Error:", e)
# print(links)