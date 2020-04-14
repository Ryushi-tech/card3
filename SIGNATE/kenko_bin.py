# ライブラリのインポート
from sklearn.linear_model import LogisticRegression
import pandas as pd

# 前処理
df = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

df["AG_ratio"].fillna(df["Alb"] / (df["TP"] - df["Alb"]), inplace=True)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

df["Gender"] = df["Gender"].apply(lambda x: 1 if x=="Male" else 0)
test["Gender"] = test["Gender"].apply(lambda x: 1 if x == "Male" else 0)

X = df.drop(["disease"], axis=1)
y = df["disease"]

X_test = test

# 境界値を指定したbinの分割
bins_T_Bil = [0, 0.5, 0.8, 100]
X_cut, bin_indice = pd.cut(X["T_Bil"], bins=bins_T_Bil, retbins=True, labels=False)
X_dummies = pd.get_dummies(X_cut, prefix=X_cut.name)
X_binned = pd.concat([X, X_dummies], axis=1)

bins_test_T_Bil = [0, 0.5, 0.8, 100]
X_test_cut, bin_test_indice = pd.cut(X_test["T_Bil"], bins=bins_test_T_Bil, retbins=True, labels=False)
X_test_dummies = pd.get_dummies(X_test_cut, prefix=X_test_cut.name)
X_test_binned = pd.concat([X_test, X_test_dummies], axis=1)

# 学習用・評価用データの分割（元の説明変数Xの代わりに、bin分割したX_binnedを使う）
X_train = X_binned
y_train = y
X_test = X_test_binned

# モデルの学習・予測
model = LogisticRegression()
model.fit(X_train, y_train)
#y_pred = model.predict_proba(X_train)[:, 1]
y_pred = model.predict_proba(X_test)[:, 1]

submit = pd.read_csv("../input/sample_submit.csv", header=None)
submit[1] = y_pred
submit.to_csv("submit.csv", index=False, header=False)

# AUCスコアの算出
#auc_score = roc_auc_score(y_true=y_train, y_score=y_pred)
#print("AUC:", auc_score)