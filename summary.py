import json
import requests

API_KEY = "rvmb5iLe0pPoQSej2aboyIZP"
SECRET_KEY = "fhxE7ufNdszDCZpUVhay57dqOtVyeuKQ"

def main(data):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_bot_8k?access_token=" + get_access_token()
    content = "\n".join("标题." + data[0] if i == 0 else f"{i}.{comment}" for i, comment in enumerate(data))
    print(content)
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "这是一篇讨论，第一层楼是主楼，其余是针对主楼的评论，请总结一下这些评论主要讲了什么，如果存在不同观点请分析" + content
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)["result"]  # 只返回result字段的值

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
