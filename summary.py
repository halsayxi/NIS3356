import json
import requests

API_KEY = "rvmb5iLe0pPoQSej2aboyIZP"
SECRET_KEY = "fhxE7ufNdszDCZpUVhay57dqOtVyeuKQ"

import csv

def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        result = ""
        for index, row in enumerate(reader):
            floor_number = row[0]
            content = row[1]
            result += f"{floor_number}.{content}\n"
    print(result)
    return result

def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_bot_8k?access_token=" + get_access_token()
    content = read_csv_file('../../../OneDrive/Desktop/topic_230779_posts.csv')
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "这是一篇讨论，第一层楼是主楼，其余是针对主楼的评论，请总结一下这些评论" + content
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()