import requests, urllib.request, re, os

# 实现多页下载


# 获取所有url
def get_all_url(html_text, page):
    down_url = re.findall('"objURL":"(.*?)"', html_text)
    now_page = 1
    while now_page < page:
        next_page_url = 'https://image.baidu.com' + re.findall('<a href="(.*?)" class="n">下一页</a>', html_text)[0]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        html = requests.get(next_page_url, headers=headers)
        next_page_pic_url = re.findall('"objURL":"(.*?)"', html.text)
        print('第{}页有{}张图片'.format(now_page+1, next_page_pic_url.__len__()))
        down_url.extend(next_page_pic_url)
        now_page = now_page + 1
        html_text = html.text
    return down_url


# 下载图片
def download_pic(down_url):
    print('共有{}张图片'.format(down_url.__len__()))
    download_path = 'D:\\pictures\\test0409-2'
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    for i, url in enumerate(down_url):
        try:
            pic_name = os.path.basename(url)
            urllib.request.urlretrieve(url, filename=os.path.join(download_path,os.path.basename(url)))
            print('成功下载第{}张图片'.format(i+1))
        except:
            print('下载第{}张图片失败,url为{}'.format(i+1, url))
            continue
    print('下载结束')


if __name__ == '__main__':
    # 等待用户输入，及提示
    print('*' * 10 + '百度图片下载助手' + '*' * 10)
    theme = input('请输入主题：')
    page = input('请输入页数：')
    # 拼接url
    picUrl = 'https://image.baidu.com/search/flip?tn=baiduimage&word=' + theme
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    html = requests.get(picUrl, headers=headers)
    # print('html:'+html.text)
    all_pic_url = get_all_url(html.text, int(page))
    download_pic(all_pic_url)
