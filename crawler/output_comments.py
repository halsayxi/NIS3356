import sys
import os
from bs4 import BeautifulSoup
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from crawler.client import Client
from crawler.models.topic import Topic
from crawler.models.post import Post

def get_topic_posts(cli: Client, topic_id: int) -> List[str]:
    topic: Topic = cli.get_single_topic(topic_id)
    posts_contents = []

    for post_id in topic.post_stream.stream:
        post_detail: Post = cli.retrieve_single_post(post_id)
        # parse HTML and extract text
        soup = BeautifulSoup(post_detail.cooked, 'lxml')
        text_content = soup.get_text(separator=" ")
        # replace line breaks
        text_content = text_content.replace('\n', ' ').replace('\r', ' ')
        posts_contents.append(text_content)

    return posts_contents


def output_comments(topic_id):
    with open('crawler/cookies.txt', 'r') as f:
        cookies = f.read()
    cli = Client(cookies=cookies)
    data = get_topic_posts(cli, topic_id)
    return data
