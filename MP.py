#pip install scikit-learn==1.2.2
#altair==4.2.2
#matplotlib==3.7.1
#pandas==1.5.3
#plotly==5.13.1
#streamlit==1.19.0
#openpyxl==3.1.2

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import time

st.header("Theft Detection in a Smart Grid Environment")

with st.form("my_form"):
    #with col1:
        st.subheader(":red[ELECTRICITY VALUES]")
        two=st.number_input(":red[Enter for Fans :]",step=None,max_value=1726.432223,help="Value in [kW] Hourly")
        three=st.number_input(":red[Enter for Cooling:]",min_value=0.1,max_value=240.0152978,help="Value in [kW] Hourly")
        four =st.number_input(":red[Enter for Heating:]",min_value=0.1,max_value=890.6219066,help="Value in [kW] Hourly")
        five =st.number_input(":red[Enter for InteriorLights:]",min_value=0.1,max_value=50.3,help="Value in [kW] Hourly")
        six =st.number_input(":red[Enter for InteriorEquipment:]",min_value=0.1,max_value=50.9,help="Value in [kW] Hourly)")
        

    #with col2:
        st.subheader(":green[FACILITY VALUES]")
        one=st.number_input(":green[Enter for Electricity]",step=None,min_value=0.1,max_value=50.3,help="Value in [kW] Hourly")
        seven =st.number_input(":green[Enter Gas]",step=None,min_value=0.1,max_value=500.3,help="Value in [kW] Hourly")
    
    #with col3:
        st.subheader(":blue[ENTER THE GAS VALUES]")
        eight =st.number_input(":blue[Enter for Heating]",step=None,min_value=0.1,max_value=500.3,help="Value in [kW] Hourly")
        nine =st.number_input(":blue[Enter for InteriorEquipment]",step=None,min_value=0.1,max_value=500.3,help="Value in [kW] Hourly")
        ten =st.number_input(":blue[Enter for Water Heater]",step=None,min_value=0.1,max_value=500.3,help="Value in [kW] Hourly")



        
        option = st.selectbox(
        'How would you like to be contacted?',
        ('FullServiceRestaurant' , 'Hospital' , 'LargeHotel' , 'MediumOffice' , 'MidriseApartment' , 'OutPatient' , 'PrimarySchool' , 'QuickServiceRestaurant' , 'SecondarySchool' , 'SmallHotel' , 'SmallOffice' , 'Stand-aloneRetail' , 'StripMall' , 'SuperMarket' , 'Warehouse' ))

        submitted = st.form_submit_button("Submit")


customer={'FullServiceRestaurant':1, 'Hospital':2, 'LargeHotel':3, 'LargeOffice':4,
        'MediumOffice':5, 'MidriseApartment':6, 'OutPatient':7, 'PrimarySchool':8,
        'QuickServiceRestaurant':9, 'SecondarySchool':10, 'SmallHotel':11,
        'SmallOffice':12, 'Stand-aloneRetail':13, 'StripMall':14, 'SuperMarket':15,
        'Warehouse':16}

if option in customer:
    eleven=customer[option]




if submitted:
    st.header(":blue[Given Info :]")
    c1,c2=st.columns(2)
    with c1:
        st.subheader(f":green[Electricity] : {one}")
        st.subheader(f":green[Fan] : {two}")
        st.subheader(f":green[Cooling] : {three}")
        st.subheader(f":green[Heating] : {four}")
        st.subheader(f":green[InteriorLights] : {five}")
    with c2:
        st.subheader(f":green[InteriorEquipment]: {six}")
        st.subheader(f":green[Gas] : {seven}")
        st.subheader(f":green[Heating] : {eight}")
        st.subheader(f":green[InteriorEquipment] : {nine}")
        st.subheader(f":green[Water Heater] : {ten}")
    
    st.subheader(f":red[Customer Type] : {option}")
    st.write("----------------------------------------------------------------------------------------------------")
    
        
    with st.spinner('Predicting... Please wait!!!'):
        time.sleep(7)





























####################################################





    with open ("classifier.pkl","rb") as file:
        clf=pickle.load(file)
    
    predictions=clf.predict([[one, two, three, four, five, six, seven, eight, nine, ten,eleven]])

    
    st.header(":blue[Result:]")


    if predictions[0]=="Normal":
        st.header(f"The Current Situation is : :green[{predictions[0]}]")
    else:
         st.header(f"The Current Situation is : :red[{predictions[0]}]")
    
    st.write("----------------------------------------------------------------------------------------------------")

    accuracy=94.71
    st.write(f"* Result ACCURACY :{accuracy}")


#one, two, three, four, five, six, seven, eight, nine, ten,eleven
#THEFT 3       13.81680571,2.245572725,0,0,2.874059242,5.127805848,74.01146451,66.13049057,2.091322253,5.789651692,1