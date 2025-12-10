import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1. データを読み込む
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# ==========================================
# 2. 特徴量の選択（数値 + ★文字データ★）
# ==========================================
# 数値データ（いつもの精鋭たち）
numeric_features = [
    'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 
    'FullBath', 'YearBuilt', 'TotRmsAbvGrd'
]

# ★追加★ 文字データ（場所とキッチン）
categorical_features = [
    'Neighborhood', # 場所（高級住宅街か？下町か？）
    'KitchenQual'   # キッチンのランク (Ex, Gd, TA, Fa)
]

# 全部まとめたリスト
features = numeric_features + categorical_features

# ==========================================
# 3. データの合体とワンホットエンコーディング
# ==========================================
# 文字データを数字にする時、学習データとテストデータで「列の数」がズレないように、
# 一度ガッチャンコしてまとめて処理するのがコツです！

# 学習データとテストデータを縦に繋げる
all_data = pd.concat([train_df[features], test_df[features]])

# 魔法のコマンド: pd.get_dummies()
# これが「Neighborhood」を「Neighborhood_CollgCr」「Neighborhood_Veenker」...
# という大量の「0/1スイッチ」の列に変換してくれます
all_data = pd.get_dummies(all_data)

# 欠損値を埋める（数値は平均で埋める）
all_data = all_data.fillna(all_data.mean())

# 合体していたデータを、元の「学習用」と「テスト用」に戻す
X = all_data.iloc[:len(train_df)]       # 前半が学習データ
test_X = all_data.iloc[len(train_df):]  # 後半がテストデータ

# 答え（価格）を用意して、対数変換しておく（合わせ技！）
y = train_df['SalePrice']
y_log = np.log1p(y)

# ==========================================
# 4. モデル検証（実力テスト）
# ==========================================
train_X, val_X, train_y_log, val_y_log = train_test_split(X, y_log, random_state=0)

model = RandomForestRegressor(random_state=1)
model.fit(train_X, train_y_log)

# 予測して、金額を元に戻す
pred_log = model.predict(val_X)
pred_real = np.expm1(pred_log)
val_y_real = np.expm1(val_y_log)

# 誤差を確認
mae = mean_absolute_error(val_y_real, pred_real)
print(f"★文字データ追加後の平均誤差: {mae:,.0f} ドル")

# ==========================================
# 5. 結果をグラフで比較
# ==========================================
plt.figure(figsize=(8, 8))
plt.scatter(val_y_real, pred_real, alpha=0.5, color='purple')
plt.plot([0, 600000], [0, 600000], color='red', linestyle='--')
plt.title('Prediction with Categorical Data')
plt.xlabel('Real Price ($)')
plt.ylabel('Predicted Price ($)')
plt.show()

# ==========================================
# 6. 提出ファイル作成
# ==========================================
full_model = RandomForestRegressor(random_state=1)
full_model.fit(X, y_log)
final_pred_log = full_model.predict(test_X)
final_pred_real = np.expm1(final_pred_log)

submission = pd.DataFrame({
    "Id": test_df["Id"],
    "SalePrice": final_pred_real
})
submission.to_csv('submission_cat.csv', index=False)
print("提出ファイル 'submission_cat.csv' ができました！")