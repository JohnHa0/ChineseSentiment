from bixin import predict

import pandas as pd
# path =r"C:\Users\junya\OneDrive\文档\Pycharm\ChineseSentiment\ChineseSentiment\testData\贸易指标-待评价数据.xlsx"
path = "./testData/贸易指标-待评价数据.xlsx"
# # scale_n = 5 # language scale
# terms = ["非常负面", "负面", "中性", "正面", "非常正面"]
data_input = pd.read_excel(path)
df = data_input.copy()
df['Sentimental']=df['原始语句'].apply(predict)
# # data_input['sentiment']=data_input.apply(lambda row: predict(row['原始语句/定量数值']),axis=1)
# #
def map_to_terms(value):
    terms = ["差", "中", "好"]
    n = 3
    # 计算每个子区间的大小
    interval_size = 2 / n
    # 计算value相对于中心0的偏移量并加上1（使其成为正值），然后除以区间大小
    index = int((value + 1) / interval_size)
    # 为了防止边界值导致的索引越界，确保索引最大为n-1
    index = min(index, n - 1)
    return terms[index]
df['评语'] = df['Sentimental'].apply(lambda value: map_to_terms(value))
df.to_excel('./testData/output_贸易指标-待评价数据.xlsx')

import seaborn as sns
import matplotlib.pyplot as plt

df['评语'] = df['评语'].astype('category')
sns.barplot(x=df['评语'].value_counts())
plt.xlabel('评语集')
plt.ylabel('频率')
plt.show()

sns.histplot(data=df, x='Sentimental', kde=True)
plt.xlabel('情感分析')
plt.ylabel('频率')
plt.show()
print("OK")