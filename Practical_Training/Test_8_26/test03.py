info = [{'name': '杜静', 'sex': '女'}, {'name': '齐根芳', 'sex': '女'}, {'name': '郑忠营', 'sex': '男'},
        {'name': '孔小康', 'sex': '男'},
        {'name': '胡书畅', 'sex': '男'}, {'name': '刘新良', 'sex': '男'}, {'name': '潘恩奇', 'sex': '男'},
        {'name': '张展硕', 'sex': '男'},
        {'name': '高文达', 'sex': '男'}, {'name': '王康萍', 'sex': '女'}, {'name': '范乃晖', 'sex': '男'},
        {'name': '宋天宇', 'sex': '男'},
        {'name': '韩振威', 'sex': '男'}, {'name': '张儒超', 'sex': '男'}, {'name': '李蕊', 'sex': '女'},
        {'name': '张永丽', 'sex': '女'},
        {'name': '董梦雪', 'sex': '女'}, {'name': '孙晶晶', 'sex': '女'}, {'name': '刘淑明', 'sex': '女'},
        {'name': '崔梦琪', 'sex': '女'},
        {'name': '郑钰森', 'sex': '男'}, {'name': '崔孟男', 'sex': '男'}, {'name': '周航飞', 'sex': '男'},
        {'name': '刘雯婷', 'sex': '女'},
        {'name': '丁需峰', 'sex': '男'}, {'name': '陈思宇', 'sex': '男'}, {'name': '王振铎', 'sex': '男'},
        {'name': '李文桐', 'sex': '女'},
        {'name': '吉世 平', 'sex': '男'}, {'name': '牛肖凯', 'sex': '男'}, {'name': '魏西琳', 'sex': '女'},
        {'name': '张邵娴', 'sex': '女'},
        {'name': '陈艳', 'sex': '女'}, {'name': '李春晖', 'sex': '男'}, {'name': '张舟', 'sex': '男'}, {'name': '胡深', 'sex': '男'},
        {'name': '郝瑞祥', 'sex': '男'}, {'name': '蔡成帆', 'sex': '男'}, {'name': '刘伟平', 'sex': '男'},
        {'name': '左宇航', 'sex': '男'},
        {'name': '丁浩', 'sex': '男'}, {'name': '金湾湾', 'sex': '女'}, {'name': '秦嘉康', 'sex': ' 男'},
        {'name': '邢家浩', 'sex': '男'},
        {'name': '王自闯', 'sex': '男'}, {'name': '邸新伟', 'sex': '男'}, {'name': '曹元博', 'sex': '男'},
        {'name': '李晴', 'sex': '女'},
        {'name': '毛梦园', 'sex': '女'}, {'name': '李凯', 'sex': '男'}, {'name': '高迎春', 'sex': '男'},
        {'name': '杜家乐', 'sex': '男'},
        {'name': '刘兆京', 'sex': '男'}, {'name': '苏岩', 'sex': '男'}, {'name': '刘家龙', 'sex': '男'},
        {'name': '单祖皓', 'sex': '男'},
        {'name': '葛圣旗', 'sex': '男'}, {'name': '王璐浩', 'sex': '男'}, {'name': '李潇潇', 'sex': '女'},
        {'name': '边继辉', 'sex': '男'},
        {'name': '张莹莹', 'sex': '女'}, {'name': '陈震东', 'sex': '男'}, {'name': '朱攀攀', 'sex': '男'},
        {'name': '张宇', 'sex': '男'},
        {'name': ' 陈辛源', 'sex': '男'}, {'name': '卢良辉', 'sex': '男'}, {'name': '李文想', 'sex': '男'},
        {'name': '马甜甜', 'sex': ' 女'},
        {'name': '岳俊芳', 'sex': '女'}, {'name': '吉庆', 'sex': '男'}, {'name': '马春飞', 'sex': '男'},
        {'name': '乔楷罡', 'sex': '男'},
        {'name': '王志斌', 'sex': '男'}, {'name': '李录录', 'sex': '女'}, {'name': '侯晓盼', 'sex': '女'},
        {'name': '徐家洋', 'sex': '男'},
        {'name': '史雪程', 'sex': '女'}, {'name': '赵梦雨', 'sex': '男'}, {'name': '浮佳伟', 'sex': '男'},
        {'name': '马路坤', 'sex': '男'},
        {'name': '时浩田', 'sex': '男'}, {'name': '赵亚非', 'sex': '男'}, {'name': '邢琳琳', 'sex': '女'},
        {'name': '刘通', 'sex': '男'},
        {'name': '张志昌', 'sex': '男'}, {'name': '张聪聪', 'sex': '女'}, {'name': '窦明晨', 'sex': '男'},
        {'name': '葛艺茗', 'sex': '女'},
        {'name': '刘倩倩', 'sex': '女'}]

# maleNum = 0
# femaleNum = 0
# maleNames = []
# femaleNames = []
# for i in range(len(info)):
#     if info[i]["sex"].strip() == "男":
#         maleNum = maleNum + 1
#         maleNames.append(info[i]["name"])
#     elif info[i]["sex"].strip() == "女":
#         femaleNum = femaleNum + 1
#         femaleNames.append(info[i]["name"])
# people = {
#     "maleNum：": maleNum,
#     "femaleNum：": femaleNum,
#     "maleNames=": maleNames,
#     "femaleNames=": femaleNames
# };
# print(people)
# print("男生人数：",maleNum,"\n女生人数：",femaleNum,"\n男生姓名=",maleNames,"\n女生姓名=",femaleNames)

result = {}
# 从infos中过滤出所有男生的字典集合
ms = filter(lambda x: x['sex'].strip() == '男', info)
# 得到所有男生的姓名
msnames = [x['name'] for x in ms]
# 设置男生个数
result['MaleNum'] = len(msnames)
# 设置男生名字
result['MaleNames'] = msnames

ms = filter(lambda x: x['sex'].strip() == '女', info)
msnames = [x['name'] for x in ms]
result['FeMaleNum'] = len(msnames)
result['FeMaleNames'] = msnames

print(result)
