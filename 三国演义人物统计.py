import jieba

txt = open("./附件/三国演义.txt", "r", encoding="utf-8").read()

execludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "军士", "左右", "军马",
             "引兵", "次日", "大喜", "主公", "天下", "东吴", "于是", "今日", "不敢", "魏兵", "陛下", "一人",
             "人马", "不知", "汉中", "只见", "众将", "后主", "蜀兵", "上马", "大叫", "太守", "此人", "夫人",
             "先主", "后人", "背后", "城中", "天子", "一面", "何不", "大军", "忽报", "先生", "百姓", "何故",
             "然后", "先锋", "不如", "赶来", "原来", "令人", "江东", "下马", "喊声", "正是", "徐州", "忽然",
             "因此", "成都", "不见", "未知", "大败", "大事", "之后", "一军", "引军", "起兵", "军中", "接应",
             "进兵", "大惊", "可以", "以为", "大怒", "不得", "心中", "下文", "一声", "追赶", "粮草", "曹兵",
             "一齐", "分解", "回报", "分付"} #排除非人名

words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长" or word == "关云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰" or word == "刘玄德":
        rword = "刘备"
    elif word == "孟德" or word == "丞相" or word == "曹孟德":
        rword = "曹操"
    elif word == "都督" or word == "公瑾":
        rword = "周瑜"
    else:
        rword = word
        counts[rword] = counts.get(rword, 0) + 1
for word in execludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))