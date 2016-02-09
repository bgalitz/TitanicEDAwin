
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

get_ipython().magic(u'pylab inline')


# In[39]:

df = pd.read_csv("train.csv")


# In[ ]:

EDA assignment


# In[40]:

df


# In[44]:

df.Survived.value_counts()


# In[43]:

df.Pclass.value_counts()


# In[42]:

df.Sex.value_counts()


# In[41]:

df.Age.value_counts()


# In[45]:

df.SibSp.value_counts()


# In[46]:

df.Parch.value_counts()


# In[47]:

df.Ticket.value_counts()


# In[48]:

df.Fare.value_counts()


# In[49]:

df.Cabin.value_counts()


# In[50]:

df.Embarked.value_counts()


# In[51]:

df[df.PassengerId.isnull()]


# In[55]:

df[df.Survived.isnull()]


# In[56]:

df[df.Pclass.isnull()]


# In[57]:

df[df.Sex.isnull()]


# In[58]:

df[df.Age.isnull()]


# In[59]:

df[df.SibSp.isnull()]df


# In[60]:

df[df.Parch.isnull()]


# In[61]:

df[df.Ticket.isnull()]


# In[62]:

df[df.Fare.isnull()]


# In[63]:

df[df.Cabin.isnull()]


# In[64]:

df[df.Embarked.isnull()]


# In[69]:

df.PassengerId.min()


# In[70]:

df.PassengerId.max()


# In[71]:

df.PassengerId.mean()


# In[73]:

df.PassengerId.std()


# In[122]:

df.PassengerId.plot(kind="hist")


# In[267]:

df.Survived.value_counts().min()


# In[268]:

df.Survived.value_counts().max()


# In[263]:

df.Survived.mean()


# In[100]:

df.Survived.value_counts().std()


# In[105]:

df.Pclass.value_counts().min()


# In[106]:

df.Pclass.value_counts().max()


# In[107]:

df.Pclass.value_counts().mean()


# In[108]:

df.Pclass.value_counts().std()


# In[109]:

df.Sex.value_counts().min()


# In[113]:

df.Sex.value_counts().max()


# In[114]:

df.Sex.value_counts().mean()


# In[115]:

df.Sex.value_counts().std()


# In[120]:

df[df.Sex=='male'].Survived.value_counts().plot(kind='barh')


# In[117]:

df[df.Sex=='female'].Survived.value_counts().plot(kind='barh')


# In[131]:

df.Age.min()


# In[132]:

df.Age.max()


# In[133]:

df.Age.mean()


# In[134]:

df.Age.std()


# In[146]:

df.Age.plot(kind="hist")


# In[128]:

df.Age = df.Age.fillna(value=avgAge)


# In[129]:

df[df.Age.isnull()]


# In[136]:

df.Age.max()


# In[148]:

df.Age.mean()


# In[139]:

df.SibSp.min()


# In[142]:

df.SibSp.max()


# In[143]:

df.SibSp.mean()


# In[144]:

df.SibSp.std()


# In[147]:

df.SibSp.plot(kind="hist")


# In[152]:

df.Parch.min()


# In[153]:

df.Parch.max()


# In[154]:

df.Parch.mean()


# In[155]:

df.Parch.std()


# In[156]:

df.Parch.plot(kind="hist")


# In[161]:

df.Ticket.min()


# In[162]:

df.Ticket.max()


# In[169]:

df.Fare.min()


# In[168]:

df.Fare.max()


# In[167]:

df.Fare.mean()


# In[170]:

df.Fare.std()


# In[193]:

df.Fare.plot(kind="bar")


# In[176]:

df.Cabin.min()


# In[177]:

df.Cabin.max()


# In[184]:

df.Embarked.min()


# In[186]:

df.Embarked.max()


# In[190]:

df.Embarked.value_counts().plot(kind="bar")


# In[194]:

df.Pclass.value_counts().plot(kind="bar")


# In[218]:

fclass = df[df.Pclass==1].Survived.value_counts()


# In[220]:

sclass = df[df.Pclass==2].Survived.value_counts()


# In[221]:

tclass = df[df.Pclass==3].Survived.value_counts()


# In[230]:

fclass


# In[231]:

total = fclass[1] + fclass[0]


# In[232]:

total


# In[251]:

percentDeadFirstClassers = float(fclass[0])/float(total)


# In[252]:

percentDeadFirstClassers


# In[253]:

percentAliveFirstClassers = 1 - percentDeadFirstClassers


# In[254]:

percentAliveFirstClassers


# In[ ]:



