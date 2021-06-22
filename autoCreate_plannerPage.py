import os
from notion.client import *
from notion.block import *
import datetime as dt

BASE_DIR = os.path.dirname(__file__)
with open(os.path.join(BASE_DIR, 'MY_TOKEN.txt'), 'r') as f:
    MY_TOKEN = f.read()
PAGE_URL = 'https://www.notion.so/Experiment-fcb88e28c7694a31a0e4897c59fc34e5'

client = NotionClient(token_v2 = MY_TOKEN)
page = client.get_block(PAGE_URL)

pTime = dt.datetime.now()
page.children.add_new(PageBlock, title = pTime.strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))

for child in page.children:
    child_page = client.get_block(child.id)
    little_child = child_page.children.add_new(TodoBlock, title = pTime.strftime('%H시 %M분 %S초'))