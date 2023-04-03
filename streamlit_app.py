import streamlit

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header(' Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kele, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#display the table on the page
streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index)) 

#display the table on the page
streamlit.dataframe(my_fruit_list)
