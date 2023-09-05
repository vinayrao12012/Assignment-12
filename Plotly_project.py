#!/usr/bin/env python
# coding: utf-8

# ## Q1

# In[7]:


import plotly.graph_objects as go
import seaborn as sns


# In[8]:


Titanic = sns.load_dataset("titanic")
fig = go.Figure()
fig.add_trace(go.Scatter(x = Titanic.age,y = Titanic.fare, mode='markers'))


# ## Q2

# In[9]:


import plotly.express as px

tips_data = px.data.tips()
fig = px.box(tips_data, x="day", y="total_bill")
fig.show()


# ## Q3

# In[10]:


Tips = px.data.tips()
fig = px.histogram(Tips, x = "sex" , y = "total_bill",pattern_shape="smoker",color = "day")
fig.show()


# ## Q4

# In[11]:


import plotly.express as px

iris_data = px.data.iris()


fig = px.scatter_matrix(
    iris_data,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",
    title="Scatter Matrix Plot of Iris Dataset"
)


fig.show()


# ## Q5

# A distplot, short for "distribution plot," is a data visualization tool commonly used in Python libraries like Seaborn and Matplotlib to display the distribution of a single variable or a comparison of the distribution between multiple variables. 

# There is no direct function distplot  in plotly.express 

# In[12]:


import plotly.express as px
import pandas as pd

# Sample data 
data = pd.DataFrame({'values': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]})

# Create a histogram
fig = px.histogram(data, x='values', nbins=5, title='Histogram')
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:




