import feedparser, time

URL = "https://ayaan-dev.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

markdown_text = """
## ✅ Latest Blog Post

매일 아침 10시경 최신 블로그 포스트로 업데이트 됩니다.</br>
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
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

