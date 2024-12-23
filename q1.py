import streamlit as st

st.header("Enter grades for chef 1 :")
a1=st.number_input("Presentation ",min_value=1,max_value=100,key='a1')
a2=st.number_input("Taste ",min_value=1,max_value=100,key='a2')
a3=st.number_input("Hygiene ",min_value=1,max_value=100,key='a3')
a=[a1,a2,a3]

st.write("Score for chef 1 is : ",a1,a2,a3)

st.header("Enter grades for chef 2 :")
b1=st.number_input("Presentation ",min_value=1,max_value=100,key='b1')
b2=st.number_input("Taste ",min_value=1,max_value=100,key='b2')
b3=st.number_input("Hygiene ",min_value=1,max_value=100,key='b3')
b=[b1,b2,b3]
count1=0
count2=0
for i in range(0,3):
    if(a[i]>b[i]):
        count1+=1
    elif(b[i]>a[i]):
        count2+=1
if(count1>count2):
    winner="chef1"
elif(count1==count2):
    winner="Tie"
else:
    winner="chef2"
st.write("## Congratulations ",winner)
if (winner!="Tie"):
    st.write("score is ",count1,count2)
    