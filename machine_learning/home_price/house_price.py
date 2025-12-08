import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

sns.set(style = "whitegrid")


train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

print (f"学習データの大きさ: {tarain_df.shape}")
print (f"テストデータの大きさ: {test_df.shape}")


# 今回使うデータの列名リスト
features = [
    'OverallQual',  # 家の全体的な品質
    'GrLivArea',    # リビングの広さ
    'GarageCars',   # ガレージに入る車の数
    'TotalBsmtSF',  # 地下室の広さ
    'FullBath',     # お風呂の数
    'YearBuilt',    # 築年数
    'TotRmsAbvGrd'  # 地上にある部屋の総数(追加)
]

X = train_df[features]
y = train_df['SalePrice']

test_X = test_df[features]