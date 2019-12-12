import requests
from bs4 import BeautifulSoup

def courses_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://ocw.mit.edu/courses/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('h4', {'class': 'course_title'}):
            link_title = link.find('a', {'rel': 'coursePreview'})
            href = 'https://ocw.mit.edu' + link_title.get('href')
            title = link_title.string
            print(title)
            print(href.split('/')[4])
            print('External Website logo: https://scontent.fcpt3-1.fna.fbcdn.net/v/t31.0-8/10505138_10152190076601857_3373879292029985409_o.png?_nc_cat=107&_nc_ohc=Zra5A8DAAHgAQnslCxM1jIYUWdc9c8F42YVgFCFoh-kHaQCV50CAen1TA&_nc_ht=scontent.fcpt3-1.fna&oh=e8fae2fc323cf025b62a968bc13469f7&oe=5E7B6266')
            get_single_course_data(href)
            print(href)
        page += 1

def get_single_course_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    # for item_description in soup.findAll('p'):
    for item_description in soup.findAll('div', {'id': 'description'}):
        description = item_description.findAll('p')
        print(description[0].string)
    for logo_url in soup.findAll('img', {'itemprop': 'image'}):
        print('Course logo URL: https://ocw.mit.edu' + logo_url.get('src'))

#         need to print each p and add them together to get a full description.
#         get tag from url (has category)


courses_spider(1)
