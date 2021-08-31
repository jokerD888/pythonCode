# 爬取数据接口：
u = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryConfirmAdd,WomWorld,WomAboard'
# 将各个国家疫情信息，放入到列表中
import requests
import json

resp = requests.get(u)
r = resp.content.decode("utf-8")

# str  --> dict
dt = json.loads(r)
dl = dt['data']['WomAboard']  # list ,存储了每个国家的疫情数据信息
#print(dl)

result = []

for d in dl:
    r = {}
    r['国家'] = d['name']  # 人数
    r['确诊人数'] = d['confirm']  # 日期
    r['死亡人数'] = d['dead']

    result.append(r)

print(result)

# 得到新增人数最多的那一天是几号
# result  list排序
# result.sort(key=lambda x: x['add'], reverse=True)
# print(result);
