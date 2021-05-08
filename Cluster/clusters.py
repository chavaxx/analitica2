#%%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("../ulabox_orders_with_categories_partials_2017.csv")

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

#%%
sns.histplot(x="total_items", data=df, multiple="stack", hue=kmeans.labels_)
plt.show() 

#%%
sns.displot(x=kmeans.labels_, y="discount%", data=df, palette='rainbow')
plt.show() 

#%% 
sns.boxplot(x=kmeans.labels_, y="total_items", data=df, palette='rainbow')
plt.show()

# %%
sns.boxplot(x=kmeans.labels_, y="discount%", data=df, palette='rainbow')
plt.show() 

#%%
sns.histplot(data=df, x="weekday", multiple="stack", hue=kmeans.labels_)

#%%
sns.histplot(data=df, x="hour", multiple="stack", hue=kmeans.labels_)

# %%
sns.boxplot(x=kmeans.labels_, y="weekday", data=df, palette='rainbow')
plt.show() 

# %%
sns.boxplot(x=kmeans.labels_, y="hour", data=df, palette='rainbow')
plt.show() 

# %%
from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier()
tree.fit(df[["total_items","Fresh%", "Food%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]], kmeans.labels_)
print(export_text(tree, feature_names=["total_items","Fresh%", "Food%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]))
# %%