import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 修正1: 変数名を test_df に統一
train_df = pd.read_csv('/kaggle/input/titanic/train.csv')
test_df = pd.read_csv('/kaggle/input/titanic/test.csv')
full_data = [train_df, test_df]

for dataset in full_data:
    # 修正2: extract[...] ではなく extract(...)
    dataset['Title'] = dataset['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    # 修正3: parch -> Parch (大文字)
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

# 欠損値の穴埋め
for dataset in full_data:
    # 修正4: [Age] -> ['Age'] (クォーテーション)
    dataset['Age'] = dataset['Age'].fillna(dataset.groupby('Title')['Age'].transform('median'))

# 修正5: それぞれ自分のデータフレームに対して処理を行う
train_df['Embarked'] = train_df['Embarked'].fillna('S')
test_df['Embarked'] = test_df['Embarked'].fillna('S')

# 修正5の続き: Embarked ではなく Fare の処理、かつ test_df 自身に入れる
test_df['Fare'] = test_df['Fare'].fillna(test_df['Fare'].median())

# 文字データを数字に変換
for dataset in full_data:
    # 修正6: dataset['Embarked'] ではなく dataset['Sex'] を変換する
    dataset['Sex'] = dataset['Sex'].map( {'male': 0, 'female': 1} ).astype(int)
    
    dataset['Embarked'] = dataset['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

    title_mapping = {"Mr": 0, "Miss": 1, "Mrs": 2, "Master": 3, "Dr": 4, "Rev": 4, "Col": 4, "Major": 4, "Mlle": 4,"Countess": 4, "Ms": 4, "Lady": 4, "Jonkheer": 4, "Don": 4, "Dona" : 4, "Mme": 4,"Capt": 4,"Sir": 4 }
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)

# 学習に使わない列を削除
drop_elements = ['PassengerId', 'Name', 'Ticket', 'Cabin', 'SibSp', 'Parch']

train_df = train_df.drop(drop_elements, axis=1)
# 修正7: train_df.drop ではなく test_df.drop
test_df = test_df.drop(drop_elements, axis=1)

X_train = train_df.drop("Survived", axis=1)
Y_train = train_df["Survived"]
X_test  = test_df.copy()

# 欠損値チェック
if X_train.isnull().sum().sum() > 0 or X_test.isnull().sum().sum() > 0:
    print("まだ欠損値が残っています！強制的に埋めます")
    X_train = X_train.fillna(X_train.median())
    X_test = X_test.fillna(X_test.median())

# モデルの学習、予測、提出
random_forest = RandomForestClassifier(n_estimators=100)

random_forest.fit(X_train, Y_train)

Y_pred = random_forest.predict(X_test)

print(f"学習データでの正解率: {round(random_forest.score(X_train, Y_train) * 100, 2)}%")

submission = pd.DataFrame({
    "PassengerId": pd.read_csv('/kaggle/input/titanic/test.csv')["PassengerId"],
    "Survived": Y_pred
})
submission.to_csv('submission_v2.csv', index=False)

print("提出ファイル'submission_v2.csv' ができました！")