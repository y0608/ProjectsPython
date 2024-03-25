from bs4 import BeautifulSoup as bs
import requests
import wikipedia

def get_links(search_link):
    # f = open("links.txt","w")
    res = requests.get(search_link)
    soup = bs(res.text, "html.parser")
    links = []

    blacklist = ['Template:','File:','Wikipedia:','Category:',
                'Help:','Special:','Portal:','Talk:',
                'Template talk:','.org/','https://','Main_Page',
                search_link.rsplit('wikipedia.org/wiki/', 1)[1]]

    for link in soup.find_all("a"):
        url = link.get("href", "")
        if "/wiki/" in url:
            if url not in links and not any(x in url for x in blacklist):
                links.append(url)
    result_links = []
    for url in links:
        result_links.append('https://en.wikipedia.org' + url)
        # f.write('https://en.wikipedia.org' + url + '\n')
    return result_links


# def read_links(file):
#     f = open("links.txt","r")
#     lines = f.readlines()
#     for line in lines:
#         print(line)

def get_extended_page(search_link):

    if 'wikipedia.org' not in search_link:
        print('wtf')
        return 0

    file = open(f"wikipedia_result_{search_link.rsplit('wikipedia.org/wiki/', 1)[1]}.txt","w")

    links = get_links(search_link)
    file.write(wikipedia.page(search_link).content)
    
    file.close()

link='https://en.wikipedia.org/wiki/SHA-2'
print(wikipedia.page(link).content)

# get_links("https://en.wikipedia.org/wiki/SHA-2")
# read_links('links.txt')
# get_extended_page(link)
