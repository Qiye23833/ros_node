import threading
import requests

class Download():# 下载类
    def download(self,url,callback_word_count):# 下载文件 并调用回调函数
        print(f"线程{threading.get_ident()} 开始下载 {url}")# 打印线程id
        response = requests.get(url)# 下载文件
        response.encoding ='utf-8'# 设置编码
        callback_word_count(url,response.text)# 调用回调函数

    def start_download(self,url,callback_word_count):# 启动线程
        thread = threading.Thread(target=self.download,args=(url,callback_word_count))# 创建线程
        thread.start()# 启动线程

def word_count(url,text):# 回调函数
    print(f"{url} 的文本长度为 {len(text)}")# 打印文本长度

def main():
    download = Download()# 创建下载对象
    download.start_download('http://0.0.0.0:8000/novel1.txt',word_count)# 启动线程
    download.start_download('http://0.0.0.0:8000/novel2.txt',word_count)# 启动线程
    download.start_download('http://0.0.0.0:8000/novel3.txt',word_count)# 启动线程
