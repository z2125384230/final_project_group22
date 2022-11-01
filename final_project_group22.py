import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
plt.style.use('seaborn')

st.title('Final project by Ziyue Zhang and Qige Pang')
# Delete irrelevant variables, like 0
missing_values = ["n/a", "0", "--", "The Grandmaster"]
df_movies = pd.read_csv('tmdb_5000_movies.csv', na_values = missing_values)
df_movies = df_movies.dropna()

st.write(df_movies)

# drawing
st.subheader('the relationship between budget and revenue') 
fig, ax = plt.subplots()
df_movies.plot.scatter(ax=ax,x='budget',y='revenue')
st.pyplot(fig)

# corr(R)
a = df_movies.budget
b = df_movies.revenue
budget_revenue_corr =  a.corr(b)
st.write(f'Because the r is {budget_revenue_corr}, higher than 0.7. We believe that budget and revenue is high positive correlation ')

# set the slider
df_movies.revenue = df_movies.revenue/1000000
revenue_value_filter = st.slider('Movies revenue(Unit: Million)', 0, 280, 52) 

# filter data by revenue value
df_movies = df_movies[df_movies.revenue <= revenue_value_filter]

st.subheader('Histogram of movie language types') 
fig, ax = plt.subplots()
df_movies.original_language.hist(ax = ax, bins = 45)
plt.xlabel('language types',fontsize=10)
st.pyplot(fig)

#Change the missing target
missing_values2 = ["n/a", "0", "--", "The Grandmaster",'en']
df_movies = pd.read_csv('tmdb_5000_movies.csv', na_values = missing_values2)
df_movies = df_movies.dropna()
st.write(df_movies)

# set the slider
df_movies.revenue = df_movies.revenue/1000000
revenue_value_filter2 = st.slider('Movies revenue(Unit: Million)', 0, 281, 52) 

# filter data by revenue value
df_movies = df_movies[df_movies.revenue <= revenue_value_filter2]

# set the sidebar of a radio button
vote_filter = st.sidebar.radio('Choose vote level :', ('Low', 'Medium', 'High'))  

# filter data by vote average
if vote_filter == 'Low':
    df_movies = df_movies[df_movies.vote_average <= 6]
elif vote_filter == 'Medium':
    df_movies = df_movies[(df_movies.vote_average > 6) & (df_movies.vote_average <= 8)]
elif vote_filter == 'High':
    df_movies = df_movies[df_movies.vote_average > 8]   

# draw the graph
st.subheader("movie language types and nums")
f=plt.figure(figsize=(10,6))
plt.pie(df_movies.original_language.value_counts(),startangle=90,autopct='%.2f%%',labels=list(df_movies.original_language.value_counts().index),radius=10,colors=['blue', 'red', 'pink', 'yellow', 'green'])
plt.axis('equal')
plt.title('Movie language', fontdict={'fontsize':22,'fontweight':'bold'})
st.pyplot(f)
