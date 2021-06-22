from notion.client import *
from notion.block import *

MY_TOKEN = ''
PAGE_URL = 'https://www.notion.so/Experiment-fcb88e28c7694a31a0e4897c59fc34e5'

client = NotionClient(token_v2 = MY_TOKEN)
page = client.get_block(PAGE_URL)

newchild1 = page.children.add_new(TodoBlock, title='블록 자동생성')