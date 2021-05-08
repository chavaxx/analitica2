# %%
clusterX = df[kmeans.labels_ == 4]
clusterX.describe()

#%%
sns.heatmap(clusterX.corr(), annot=True)

#%%
sns.boxplot(x="weekday", y="hour", data=clusterX, palette='rainbow') 

# %%
