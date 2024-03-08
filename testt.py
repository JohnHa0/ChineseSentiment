from bixin import predict
import pandas as pd
# text = "幸福每时每刻都会像路边的乞丐一样出现在你面前。要是你觉得你所梦想的幸福不是这样的，因而断言你的幸福已死亡，你只接受符合你的原则和心愿的幸福，那么你就会落得不幸。"
# # 出自安德烈·纪德《人间食粮》
# predict(text)
# # sentiment score: 0.42
# predict("6、鼓励中国的“一带一路”倡议与澜湄合作活动和项目及包括《东盟互联互通总体规划》在内的湄公河国家相关发展规划之间的对接。")
# predict("重申澜湄合作自2016年启动以来在各领域取得的显著发展，以及在落实《东盟互联互通总体规划2025》、“一带一路”倡议和其他湄公河次区域合作愿景，推动繁荣和可持续发展、促进南南合作以及落实联合国2030年可持续发展议程等方面所发挥的重要作用。")
path ="待处理数据样例.xlsx"
# scale_n = 5 # language scale
terms = ["非常负面", "负面", "中性", "正面", "非常正面"]
data_input=pd.read_excel(path,sheet_name="数据")
df = data_input[0:100]
df['Sentimental']=df['原始语句/定量数值'].apply(predict)
# data_input['sentiment']=data_input.apply(lambda row: predict(row['原始语句/定量数值']),axis=1)

def map_to_terms(value, terms):
    n = len(terms)
    # 计算每个子区间的大小
    interval_size = 2 / n
    # 计算value相对于中心0的偏移量并加上1（使其成为正值），然后除以区间大小
    index = int((value + 1) / interval_size)
    # 为了防止边界值导致的索引越界，确保索引最大为n-1
    index = min(index, n - 1)
    return terms[index]
df['Scale'] = df['Sentimental'].apply(lambda value: map_to_terms(value, terms))



