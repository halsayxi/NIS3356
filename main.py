import sys
import os
from bs4 import BeautifulSoup
from typing import List, Dict

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from client import Client
from models.topic import Topic
from models.post import Post

def get_topic_posts(cli: Client, topic_id: int) -> List[Dict]:
    topic: Topic = cli.get_single_topic(topic_id)
    posts_data = []

    for post_id in topic.post_stream.stream:
        post_detail: Post = cli.retrieve_single_post(post_id)
        # parse HTML and extract text
        soup = BeautifulSoup(post_detail.cooked, 'lxml')
        text_content = soup.get_text(separator=" ")
        # replace line breaks
        text_content = text_content.replace('\n', ' ').replace('\r', ' ')
        posts_data.append({
            "floor_number": post_detail.post_number,
            "content": text_content
        })

    return posts_data


if __name__ == '__main__':
    with open('cookies.txt', 'r') as f:
        cookies = f.read()
    cli = Client(cookies=cookies)
    topic_id = int(input("Input topic ID: "))

    data = get_topic_posts(cli, topic_id)
    with open(f'topic_{topic_id}_posts.txt', 'w', encoding='utf-8', newline='') as file:
        for row in data:
            file.write(f"{row['floor_number']}\t{row['content']}\n")

    print(f"Data successfully saved to topic_{topic_id}_posts.txt.")
