#%%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
#%%
dfp = df[["Fresh%", "Food%"]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters suggested by knee method: {k}")

kmeans = KMeans(n_clusters=k).fit(df[["Fresh%", "Food%"]])
sns.scatterplot(data=df, x="Fresh%", y="Food%", hue=kmeans.labels_)
plt.show()


from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier()
tree.fit(df[["total_items", "Fresh%", "Food%"]], kmeans.labels_)
print(export_text(tree, feature_names=["total_items", "Fresh%", "Food%"]))
# %%
dfp = df[["total_items", "discount%"]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters suggested by knee method: {k}")

kmeans = KMeans(n_clusters=k).fit(df[["total_items", "discount%"]])
sns.scatterplot(data=df, x="total_items", y="discount%", hue=kmeans.labels_)
plt.show()


from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier()
tree.fit(df[["Food%", "total_items", "discount%"]], kmeans.labels_)
print(export_text(tree, feature_names=["Food%", "total_items", "discount%"]))
# %%
dfp = df[["Fresh%", "Food%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters suggested by knee method: {k}")
# %%

kmeans = KMeans(n_clusters=k).fit(df[["Fresh%", "Food%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]])
sns.boxplot(x=kmeans.labels_, y="total_items", data=df, palette='rainbow')
plt.show()

# %%
cluster0 = df[kmeans.labels_ == 0]
cluster0.describe()
# %%
cluster1 = df[kmeans.labels_ == 1]
cluster1.describe()
# %%
cluster2 = df[kmeans.labels_ == 2]
cluster2.describe()
# %%
cluster3 = df[kmeans.labels_ == 3]
cluster3.describe()
# %%
cluster4 = df[kmeans.labels_ == 4]
cluster4.describe()
# %%
from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier()
tree.fit(df[["total_items","Fresh%", "Food%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]], kmeans.labels_)
print(export_text(tree, feature_names=["total_items","Fresh%", "Food%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]))
# %%