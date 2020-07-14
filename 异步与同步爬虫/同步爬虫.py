import time
import requests
from lxml import etree

'''使用 xpath 进行定位是有个小坑，在本代码的第 15 行定位电影的 href 时，直接从 network 获得的 xpath 为 //*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a/@href 
    而正确的定位应将 xpath 中的 tbody 删去，否则定位失败。
'''

headers = {
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
           }

def get_move_url():
    req_url = 'https://movie.douban.com/chart'
    r = requests.get(req_url,headers = headers)
    html = etree.HTML(r.text)
    moves_url = html.xpath('//*[@id="content"]/div/div[1]/div/div/table//tr/td[2]/div/a/@href')
    return moves_url

def get_move_contents(move_url):
    r = requests.get(move_url,headers = headers)
    html = etree.HTML(r.text)
    move = dict()
    move_name = html.xpath('//*[@id="content"]/h1/span[1]/text()')
    move_author = html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
    move['name'] = move_name
    move['author'] = move_author
    return move

if __name__ == '__main__':
    s_time = time.time()
    move_url_list = get_move_url()
    moves = dict()
    for url in move_url_list:
        moves = get_move_contents(url)
        print(moves)
    print('爬取成功，耗时%s s。'%(time.time() - s_time))
