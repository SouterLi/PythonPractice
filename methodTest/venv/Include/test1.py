import re, os, sys

if __name__ == '__main__':
    str = ' "hasLarge" :0,            "hoverURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2267443830,2258699112&fm=26&gp=0.jpg",            "pageNum":0,            "objURL":"http://dingyue.nosdn.127.net/JDYElKiNInJePpucjcwK5i=bobYdI8r3zHrgkSMX9NbWg1537158310225compressflag.jpg",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F1y_z&e3B8mn_z&e3Bv54AzdH3FedAzdH3Fw6ptvsjAzdH3F1jpwtsAzdH3FDRTGPAmHacnaWRPC_z&e3Bip4s",            "fromURLHost":"dy.163.com","currentIndex":"",            "width":1080,            "height":720,            "type":"jpg",            "is_gif":0,            "strategyAssessment": "534530_0_0_0",'
    strr = '<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E5%8A%A8%E6%BC%AB&pn=180&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">10</span></a><a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E5%8A%A8%E6%BC%AB&pn=20&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0" class="n">下一页</a>'
    str2 = re.findall('"objURL":"(.*?)"', str)
    str3 = re.findall('<a href="(.*?)" class="n">下一页</a>', strr)[0]
    print(str3)
    print(str2)
    name = os.path.basename(str2[0])
    print(name)
    print(sys.path[0])