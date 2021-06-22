from notion.client import *
from notion.block import *

BASE_DIR = os.path.dirname(__file__)
with open(os.path.join(BASE_DIR, 'MY_TOKEN.txt'), 'r') as f:
    MY_TOKEN = f.read()
PAGE_URL = 'https://www.notion.so/Experiment-fcb88e28c7694a31a0e4897c59fc34e5'

client = NotionClient(token_v2 = MY_TOKEN)
page = client.get_block(PAGE_URL)

new_child1 = page.children.add_new(TodoBlock, title='블록 자동생성')