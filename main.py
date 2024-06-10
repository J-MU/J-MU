import feedparser, time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



URL = "https://ayaan-dev.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

markdown_text = """
## ✅ Latest Blog Post

매일 10시경 최신 블로그 포스트로 업데이트 됩니다.</br>
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{idx+1}. {time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"


new_text_content = ''
with open("README.md",'r',encoding='utf-8') as f:
    lines = f.readlines()
    key=0
    for i, line in enumerate(lines):
        if(line.strip()=="<!-- Start blog -->"):
            key=1
            new_string = "<!-- Start blog -->"
        elif(key==1):
            new_string = markdown_text
            key+=1
        elif(key>1):
            if(line.strip()!="<!-- End blog -->"):
                continue;
            else:
                new_string="<!-- End blog -->"
                key=0
        else:
            new_string = line.strip()

        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'

with open("README.md",'w',encoding='utf-8') as f:
    f.write(new_text_content)

# 여기서부터는 백준 크롤링
url = Request('https://www.acmicpc.net/status?user_id=alsdnrdl01&result_id=4', headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
    "refere": "https://example.com",
    "cookie": """your cookie value ( you can get that from your web page) """,
})

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

markdown_text = """
## ✅ Latest Solved Baekjoon

매일 10시경 최신 기록으로 업데이트 됩니다.</br>
"""  # list of blog posts will be appended here
base_url="https://www.acmicpc.net/"

for idx,child in enumerate(soup.tbody.children):
    if(idx>=MAX_POST):
        break
    problem_link=base_url+child.select("td")[2].a["href"]
    problem_no=child.select("td")[2].a.string #문제 번호 크롤링
    problem_name=child.select("td")[2].a["title"] #문제 이름 크롤링
    solved_time=child.select("td")[8].a["title"][0:10]
    markdown_text+=f"[{problem_no}. {problem_name}-{solved_time}]({problem_link}) <br/>\n"

new_text_content=''
with open("README.md",'r',encoding='utf-8') as f:
    lines = f.readlines()
    key=0
    for i, line in enumerate(lines):
        if(line.strip()=="<!-- Start BaekJoon -->"):
            key=1
            new_string = "<!-- Start BaekJoon -->"
        elif(key==1):
            new_string = markdown_text
            key+=1
        elif(key>1):
            if(line.strip()!="<!-- End BaekJoon -->"):
                continue;
            else:
                new_string="<!-- End BaekJoon -->"
                key=0
        else:
            new_string = line.strip()

        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'

with open("README.md",'w',encoding='utf-8') as f:
    f.write(new_text_content)
