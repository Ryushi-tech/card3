import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.feature_selection import SelectFromModel

# 前処理
df = pd.read_csv('input/train.csv')
test = pd.read_csv('input/test.csv')

df["AG_ratio"].fillna(df["Alb"] / (df["TP"] - df["Alb"]), inplace=True)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

df["Gender"] = df["Gender"].apply(lambda x: 1 if x == "Male" else 0)
test["Gender"] = test["Gender"].apply(lambda x: 1 if x == "Male" else 0)

X = df.drop(["disease"], axis=1)
y = df["disease"]

X_target = X.drop(["Gender"], axis=1)
X_test = test.drop(["Gender"], axis=1)

# 多項式・交互作用特徴量
pf = PolynomialFeatures(degree=1, include_bias=False)
pf.fit(X_target)
pf_arr = pf.transform(X_target)
X_polynomial = pd.DataFrame(pf_arr, columns=["poly" + str(x) for x in range(pf_arr.shape[1])])

pf_test_arr = pf.transform(X_test)
X_test_poly = pd.DataFrame(pf_test_arr, columns=["poly" + str(x) for x in range(pf_test_arr.shape[1])])

# 組み込み法のモデル、閾値の指定
fs_model = LogisticRegression(penalty='l2', random_state=0, max_iter=1000)
fs_threshold = "0.1*median"
selector = SelectFromModel(fs_model, threshold=fs_threshold)

# 特徴量選択の実行
selector.fit(X_polynomial, y)
mask = selector.get_support()

# 選択された特徴量だけのサンプル取得
X_polynomial_masked = X_polynomial.loc[:, mask]
X_test_poly_masked = X_test_poly.loc[:, mask]

X_train = X_polynomial_masked
y_train = y
X_test2 = X_test_poly_masked

# モデルの学習・予測
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict_proba(X_train)[:, 1]

# AUCスコアの算出
auc_score = roc_auc_score(y_true=y_train, y_score=y_pred)
print("AUC:", auc_score)
