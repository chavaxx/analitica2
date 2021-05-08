#%%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("../ulabox_orders_with_categories_partials_2017.csv")
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

#%%
kmeans = KMeans(n_clusters=k).fit(df[["Fresh%", "Food%"]])

#%%
sns.scatterplot(data=df, x="Fresh%", y="Food%", hue=kmeans.labels_)
plt.show()

#%% 
sns.boxplot(x=kmeans.labels_, y="total_items", data=df, palette='rainbow')
plt.show()

# %%
sns.boxplot(x=kmeans.labels_, y="discount%", data=df, palette='rainbow')
plt.show() 

# %%
sns.boxplot(x=kmeans.labels_, y="weekday", data=df, palette='rainbow')
plt.show() 

# %%
sns.boxplot(x=kmeans.labels_, y="hour", data=df, palette='rainbow')
plt.show() 
#-------------------------------------------------------------------------------

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

#%%
kmeans = KMeans(n_clusters=k).fit(df[["total_items", "discount%"]])

#%%
sns.scatterplot(data=df, x="total_items", y="discount%", hue=kmeans.labels_)
plt.show()

#%% 
sns.boxplot(x=kmeans.labels_, y="Food%", data=df, palette='rainbow')
plt.show()

#%%
grupo2 = df[kmeans.labels_ == 2]
grupo2.describe() 
# %%
sns.boxplot(x=kmeans.labels_, y="Fresh%", data=df, palette='rainbow')
plt.show() 

# %%
sns.boxplot(x=kmeans.labels_, y="weekday", data=df, palette='rainbow')
plt.show() 

# %%
sns.boxplot(x=kmeans.labels_, y="hour", data=df, palette='rainbow')
plt.show() 
#%%
