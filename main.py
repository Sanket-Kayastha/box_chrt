import pandas as pd
import plotly.express as px

df_app = pd.read_csv("Android_App_Analytics/apps.csv")
# print(df_app.head())
# print(df_app.shape)
# print(df_app.columns)
# print(df_app.sample(5))
df_app.drop(axis=1 ,columns=['Last_Updated','Android_Ver'], inplace=True)
# print(df_app.sample(5))
# print(df_app['Rating'].isna().values.sum())
df_apps_clean = df_app.dropna(axis=0)
# print(df_apps_clean['Rating'].isna().values.sun())
# print(df_apps_clean.head())
# print(df_apps_clean.isna().values.any())
# print(df_apps_clean.sample(10))
# print(df_apps_clean.duplicated().values.sum())
# print(df_apps_clean[df_apps_clean.App=='Instagram'])
df_apps_cleans = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
# print(df_apps_clean.duplicated().values.any())
# print(df_apps_clean.sample(12))
# print(df_apps_clean[df_apps_clean.App=='Instagram'])
# print(df_apps_clean.sort_values('Rating', ascending=False))
# print(df_apps_cleans.sort_values('Size_MBs', ascending=False).head())
# print(df_apps_cleans.sort_values('Reviews', ascending=False).head(50))
# print(df_apps_cleans.columns)
ratings = df_apps_cleans.Content_Rating.value_counts()
# review = df_apps_cleans['Reviews']
# print(rating.values)
# print(rating.index)
# fig=px.pie(values=ratings.values, names=ratings.index ,title="Content Ratings", hole=0.5)
# fig.update_traces(textposition="inside", textfont_size=15, textinfo='percent')

# fig.show()

# print(df_apps_cleans.columns)
# print(df_apps_cleans.Installs.value_counts())
# print(type(df_apps_cleans['Installs']))
# print(df_apps_cleans.Installs.describe())
# print(df_apps_cleans.describe())
# print(df_apps_cleans.info())
# df_apps_cleans.Installs = df_apps_cleans.Installs.astype(str).str.replace(',',"")
# df_apps_cleans.Installs = pd.to_numeric(df_apps_cleans.Installs)
# print(df_apps_cleans[["App","Installs"]].groupby('Installs').count())

# print(df_apps_cleans.Price.describe())
# df_apps_cleans.Price = df_apps_cleans.Price.astype(str).str.replace('$',"")
# df_apps_cleans.Price = pd.to_numeric(df_apps_cleans.Price)
# # print(df_apps_cleans.sort_values('Price', ascending=False).head(20))

# df_app_clean_price = df_apps_cleans[df_apps_cleans['Price']<250]
# print(df_app_clean_price.sort_values('Price', ascending=False).head(10))

# # print(df_apps_cleans.nunique())
# top10_category = df_apps_cleans.Category.value_counts()[:10]
# print(top10_category)
# bar = px.bar(x=top10_category.values, y=top10_category.index, orientation='h', title="Category Popularity")
# bar.update_layout(xaxis_title="Number of Downloads", yaxis_title="Category")
# scatter = px.scatter(x=top10_category.index, y=top10_category.values, color='top10_category',title="Category Concentration")

# scatter.show()

# print(len(df_apps_cleans.Genres.unique()))
# print(df_apps_cleans.Genres.value_counts().sort_values(ascending=True)[:50])

df_stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
num_genres = df_stack.value_counts()
# print(num_genres.values)

# fig = px.bar(x=num_genres.index[:15], y=num_genres.values[:15]
#              , title='Top Genres',
#              color=num_genres.values[:15],
#              color_continuous_scale='Agsunset',
#              hover_name=num_genres.index[:15]
#              )
# fig.update_layout(xaxis_title="App Genre", yaxis_title="Number of App", coloraxis_showscale=False)
# fig.show()
# print(df_apps_cleans.Type.value_counts())
# print(df_apps_cleans.head())

df_free_vs_paid = df_apps_cleans.groupby(["Category","Type"], as_index=False).agg({'App': pd.Series.count})
# print(df_free_vs_paid.shape)
# print(df_free_vs_paid.columns)
# bar = px.bar(df_free_vs_paid, x='Category',
#              title="Free vs Paid Apps by Category",
#              color='Type',
#              barmode='group'
#               ,y='App')
# bar.update_layout(xaxis_title='Category', yaxis_title='Number of Apps',
#                  xaxis={'categoryorder':'total descending'},
#                   yaxis= dict(type='log') )
# bar.show()

box = px.box(df_apps_cleans, x="Type", y="Installs",
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')

box.update_layout(yaxis=dict(type='log'))
box.show()