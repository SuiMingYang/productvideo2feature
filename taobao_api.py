import requests as reqs
import base64
import logging
import re
import json

# 调用淘宝识图请求接口，获取商品源和标签
def taobao_pic_recognize(pic_dir,pic_name,cookie):
    # with open(pic_dir+'/'+pic_name, "rb") as f:
    #     # b64encode：编码，b64decode: 解码
    #     base64_data = base64.b64encode(f.read())

    imagefile={ "file": (pic_name, open(pic_dir+'/'+pic_name, "rb"), "image/%s" % pic_name.split('.')[1])}
    header={
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': cookie,
    'origin': 'https://s.taobao.com',
    'referer': 'https://s.taobao.com/search?q=&imgfile=&js=1&stats_click=search_radio_all%253A1&initiative_id=staobaoz_20191105&ie=utf8&tfsid=O1CN01g6xEgi1TxE8ft6Nmb_!!0-imgsearch.jpg&app=imgsearch',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'}

    res_pic=reqs.post('https://s.taobao.com/image',files=imagefile,headers=header, verify=False)

    print(res_pic.json()['name'])

    res_alias=reqs.get("""https://s.taobao.com/search?q=&imgfile=&js=1&stats_click=search_radio_all&initiative_id=staobaoz_20191105&ie=utf8&tfsid=%s&app=imgsearch""" % res_pic.json()['name'],{},headers=header,verify=False)
    #reg=r'<script>+[\W]+g_page_config = ([\w\W]+"map":{}};);+[\W]+<\/script>'
    reg_alias=r'<script>+[\W]+g_page_config = ([\w\W]+"map":{}})+'

    m=re.search(reg_alias,res_alias.text,re.M|re.I)
    data=json.loads(m.group(1))

    # 外观相似宝贝
    item = data['mods']['itemlist']['data']['collections'][0]#['auctions'][0]

    # 您可能会喜欢
    # item = data['mods']['itemlist']['data']['collections'][1]

    for i,detail in enumerate(item['auctions']):
        if i==3:
            break
        else:
            print('商品：',detail['title'],detail['pic_url'],detail['detail_url'])
            res_detail=reqs.get("https:"+detail['detail_url'],{},headers=header,verify=False)

            reg_detail=r'"attributes-list"+([\w\W]+)</ul>+'

            m=re.search(reg_detail,res_detail.text,re.M|re.I)
            detail=m.group(1).replace('\t','').replace('"','').replace('\'','').replace(' ','').replace('&nbsp;','').replace('\r','').replace('\n','').replace('<li','')
            field_list=detail.split('</li>')

            for field in field_list[0:-1]:
                try:
                    f_obj=field.split('>')[-1].split(':')
                    f_key=f_obj[0]
                    f_value=f_obj[1]
                    print('属性：',f_key,f_value)
                except Exception as e:
                    print(e)
                    pass
            

