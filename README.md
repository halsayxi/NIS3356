# Shuiyuan Crawler

![python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)

## 开始
+ 创建 client
    + **手动复制 cookies（存入cookies.txt）**
        ```python
        cli = Client(cookies='COPY_YOUR_COOKIES_HERE')
        ```
    + ~~提供 jaccount 和密码，通过 selenium 自动获取 cookies（需额外安装库）~~
        ```python
        cli = Client(jaccount='YOUR_JACCOUNT', pwd='YOUR_PASSWORD')
        ```
    + ~~使用 User-Api-Key（详见 https://shuiyuan.sjtu.edu.cn/t/topic/123808 ，有频率限制）~~
        ```python
        cli = Client(user_api_key='YOUR_USER_API_KEY')
        ```
+ 调用接口
    + 此项目只需获取指定帖子各楼层内容，运行```main.py```即可得到相应topic的txt文件。


## 参考
https://github.com/Okabe-Rintarou-0/Shuiyuan-Client/tree/main
(若有其他扩展需求，也可参考此处)
 