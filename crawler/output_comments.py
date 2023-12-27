import sys
import os
from bs4 import BeautifulSoup
from typing import List
import tkinter as tk

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from crawler.client import Client
from crawler.models.topic import Topic
from crawler.models.post import Post

def get_topic_posts(cli: Client, topic_id: int) -> List[str]:
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("读取进度")
    label = tk.Label(window, text="已读取的评论数: 0")
    label.pack()

    topic: Topic = cli.get_single_topic(topic_id)
    posts_contents = [topic.title]

    for i, post_id in enumerate(topic.post_stream.stream):
        post_detail: Post = cli.retrieve_single_post(post_id)
        # parse HTML and extract text
        soup = BeautifulSoup(post_detail.cooked, 'lxml')
        text_content = soup.get_text(separator=" ")
        # replace line breaks
        text_content = text_content.replace('\n', ' ').replace('\r', ' ')
        posts_contents.append(text_content)

        # update the label with the number of posts read
        label.config(text=f"已读取的评论数: {i+1}")
        # update the Tkinter window to reflect the changes
        window.update()

    # Close the window after reading all posts
    window.destroy()

    return posts_contents

def output_comments(topic_id):
    with open('crawler/cookies.txt', 'r') as f:
        cookies = f.read()
    cli = Client(cookies=cookies)
    data = get_topic_posts(cli, topic_id)
    return data
