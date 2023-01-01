class scraping:

    def __init__(self):
        self.website_url = ''

    #Get HTML page
    #HTMLページを取得
    def gethtml(self):
        import requests

        from requests.exceptions import Timeout
        try:
            page = requests.get(self.website_url, timeout=(3.0, 7.5))
        except Timeout:
            print("!!!TIME OUT!!!")
            pass
        
        return page

    #Get links(href and link) on the HTML page(-->gethtml())
    #取得したHTMLページ上のlink(href, link)を取得
    def links(self):
        from bs4 import BeautifulSoup
        page = self.gethtml()

        soup = BeautifulSoup(page.content, "html.parser")
        links = []

        for a in soup.find_all('a'):
            href = a.get("href")
            links.append(href)
        for link in soup.find_all('link'):
            href = link.get("href")
            links.append(href)

        return links


    #Get images on the HTML page(-->gethtml())
    #取得したHTMLページ上の画像を取得
    def imgs(self):
        from bs4 import BeautifulSoup
        import csv

        page = self.gethtml()
        soup = BeautifulSoup(page.content, "html.parser")
        imgs = []
        for img in soup.find_all('img'):
            src = img.get("src")
            imgs.append(src)

        return imgs

    #Get texts on the HTML page(-->gethtml())
    #取得したHTMLページ上のテキストを取得
    def texts(self):
        from bs4 import BeautifulSoup
        import csv
        import re

        page = self.gethtml()
        soup = BeautifulSoup(page.content, "html.parser")
        tag_texts = []
        texts = []

        tag_texts.extend(soup.find_all('p'))
        tag_texts.extend(soup.find_all("h1"))        
        tag_texts.extend(soup.find_all("h2"))
        tag_texts.extend(soup.find_all("title"))

        for text in tag_texts:
            texts.append(re.sub('<.+?>', "", str(text)))

        return texts


    #取得したlinkを開く
    def links_open(self):
        import webbrowser as web
        links = self.links()
        for link in links:
            web.open(link)

    #取得した画像を開く
    def imgs_open(self):
        import webbrowser as web
        imgs = self.imgs()
        for img in imgs:
            web.open(img)

    
    #Save the links to links.csv
    #取得したlinkをcsvに保存
    def links_csv(self):
        import csv
        links = self.links()

        with open('links.csv','w', newline="") as f:
           writer = csv.writer(f)
           for i in range(len(links)):
               writer.writerow([links[i]])
        
    #Save the images to imgs.csv
    #取得した画像をcsvに保存
    def imgs_csv(self):
        import csv
        imgs = self.imgs()

        with open('imgs.csv','w', newline="") as f:
            writer = csv.writer(f)
            for i in range(len(imgs)):
               writer.writerow([imgs[i]])

    #Save the texts to imgs.csv
    #取得したテキストをcsvに保存
    def texts_csv(self):
        import csv
        texts = self.texts()

        with open('texts.csv','w', encoding='utf-8', newline="") as f:
            writer = csv.writer(f)
            for i in range(len(texts)):
               writer.writerow([texts[i]])