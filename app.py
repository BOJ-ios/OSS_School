import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

myPage = """# Kim-MinGyu [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBOJ-ios&count_bg=%23FFDE00&title_bg=%23DBBFFF&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## Social
![](https://dcbadge.vercel.app/api/shield/376298017730461706)

![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white&link=mailto:jun3021303@gmail.com) : **jun3021303@gmail.com**

![KakaoTalk](https://img.shields.io/badge/kakaotalk-ffcd00.svg?style=for-the-badge&logo=kakaotalk&logoColor=000000) : **@namu.wiki**

![WeChat](https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white) : **@namu_wiki**
"""


st.title("This is my streamlit page")
st.markdown(myPage)

x = st.slider('Select a value')
st.write(x, 'squared is', x*x)

st.code('System.out.println("Hello")')

st.subheader("Rolling Hashing")
st.latex(r'''
         H = c_1a^{L-1} + c_2a^{L-2} + ... + c_La^0 (mod n)
         ''')

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df = pd.DataFrame(np.random.randn(500, 2) /
                  [50, 50]+[37.76, -122.4], columns=['lat', 'lon'])
st.map(df)
