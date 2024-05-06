import zipfile




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import time

st.header("Theft Detection in a Smart Grid Environment")

with st.form("my_form"):
    #with col1:
        st.subheader(":red[ELECTRICITY VALUES]")
        two=st.number_input(":red[Enter for Fans :] Values Range : (0-1726)",step=None,max_value=1726.432223,help="Value in [kW] Hourly")
        three=st.number_input(":red[Enter for Cooling:]",max_value=240.0152978,help="Value in [kW] Hourly")
        four =st.number_input(":red[Enter for Heating:]",max_value=890.6219066,help="Value in [kW] Hourly")
        five =st.number_input(":red[Enter for InteriorLights:]",max_value=50.3,help="Value in [kW] Hourly")
        six =st.number_input(":red[Enter for InteriorEquipment:]",max_value=50.9,help="Value in [kW] Hourly)")
        

    #with col2:
        st.subheader(":green[FACILITY VALUES]")
        one=st.number_input(":green[Enter for Electricity]",step=None,max_value=50.3,help="Value in [kW] Hourly")
        seven =st.number_input(":green[Enter Gas]",step=None,max_value=500.3,help="Value in [kW] Hourly")
    
    #with col3:
        st.subheader(":blue[GAS VALUES]")
        eight =st.number_input(":blue[Enter for Heating]",step=None,max_value=500.3,help="Value in [kW] Hourly")
        nine =st.number_input(":blue[Enter for InteriorEquipment]",step=None,max_value=500.3,help="Value in [kW] Hourly")
        ten =st.number_input(":blue[Enter for Water Heater]",step=None,max_value=500.3,help="Value in [kW] Hourly")



        
        option = st.selectbox(
        'Customer Type',
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

    
    
    # Specify the path to your .zip file
    zip_file_path = "classifier.zip"
    
    # Open the .zip file in read mode
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # List all files and directories in the .zip file
        zip_ref.printdir()
        with zip_ref.open("classifier.pkl") as file:    
            clf=pickle.load(file)
        
    predictions=clf.predict([[one, two, three, four, five, six, seven, eight, nine, ten,eleven]])

    
    st.header(":blue[Result:]")


    if predictions[0]=="Normal":
        st.header(f"The Current Situation is : :green[{predictions[0]}]")
    elif predictions[0]=="Theft1":
        st.header(f"The Current Situation is : :red[{predictions[0]}]")
        st.write(" Involves a considerable reduction in electricity consumption during the day, calculated by multiplying the consumption by a randomly chosen value between 0.1 and 0.8.")
    elif predictions[0]=="Theft2":
        st.header(f"The Current Situation is : :red[{predictions[0]}]")
        st.write(" Electricity consumption drops to zero at random and during an arbitrary period.")
    elif predictions[0]=="Theft3":
        st.header(f"The Current Situation is : :red[{predictions[0]}]")
        st.write("Similar to Theft Type 1, but each consumption value (each hour) is multiplied by a random number.")
    elif predictions[0]=="Theft4":
        st.header(f"The Current Situation is : :red[{predictions[0]}]")
        st.write("A random fraction of the mean consumption is generated for each hour.")
    elif predictions[0]=="Theft5":
        st.header(f"The Current Situation is : :red[{predictions[0]}]")
        st.write("Reports the mean consumption for each hour.")
    st.write("----------------------------------------------------------------------------------------------------")

    accuracy=95.3
    st.write(f"* Result ACCURACY :{accuracy}")


#one, two, three, four, five, six, seven, eight, nine, ten,eleven
#THEFT 3       13.81680571,2.245572725,0,0,2.874059242,5.127805848,74.01146451,66.13049057,2.091322253,5.789651692,1
