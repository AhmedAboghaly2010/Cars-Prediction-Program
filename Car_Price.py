import streamlit as st
import pandas as pd
import pickle

# Upload Data

data=pickle.load(open(r'C:\Users\Ahmed\Car_Prediction.sav','rb'))

# Streamlit Page

st.title('Cares Prediction Web App')

st.sidebar.header('Feature selecting')
st.image('http://www.indianbluebook.com/themes/ibb/assets/images/home/banner1.jpg')
st.info('Easy Application For Predicting Cares_Price')

st.sidebar.info('Easy Application For Predictiong Cares_Price')
# .........................................................................................
m1=['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
       'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
       'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
       'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
       'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
       'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
       'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
       'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
       'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
       'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
       'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']
m2=[27,  6, 18, 13, 20, 49, 31, 39, 23, 51,  2, 40, 35,  3, 47,  9, 24,
       34, 46, 30, 15, 12, 21, 48, 36,  0,  8, 33, 11, 26, 50, 22, 45,  7,
       28,  4, 10, 37, 52, 53, 17,  5, 43, 32, 44, 25, 29, 41,  1, 19, 38,
       42, 14, 16]
Manufacturer_mapping = dict(zip(m1, m2))
Manufacturer1=st.selectbox('Manufacturer', m1)
Manufacturer = Manufacturer_mapping[Manufacturer1]
# ...................................................................................
mm1=['RX 450', 'Equinox', 'FIT','E 230 124', 'RX 450 F SPORT',
       'Prius C aqua']
mm2=[890, 458, 477,485, 470, 833]
Model_mapping = dict(zip(mm1, mm2))
Model1=st.selectbox('Model',mm1 )
Model=Model_mapping[Model1]
# ....................................................................................
c1=['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
       'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
       'Pickup']
c2=[ 4,  3,  9,  2, 10,  7,  0,  1,  6,  8,  5]
Category_Mapping=dict(zip(c1,c2))
Category1=st.selectbox('Category', c1)
Category=Category_Mapping[Category1]
# ................................................................................
l1 = ['yes', 'no']
l2 = [1,2]
leather_mapping = dict(zip(l1, l2))
Leather1 = st.selectbox('Leather interior', l1)
Leather = leather_mapping[Leather1]

# .................................................................................    
f1=['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG',
       'Hydrogen']
f2=[2, 5, 1, 6, 4, 0, 3]
Fuel_Mapping=dict(zip(f1,f2))
Fuel1=st.selectbox('Fuel type',f1 )
Fuel=Fuel_Mapping[Fuel1]
# .................................................................................
g1=['Automatic', 'Tiptronic', 'Variator', 'Manual']
g2=[0, 2, 3, 1]
Gear_mapping=dict(zip(g1,g2))
Gear1=st.selectbox('	Gear box type', g1)
Gear=Gear_mapping[Gear1]
# ...................................................................................
d1=['4x4', 'Front', 'Rear']
d2=[0,1,2]
Drive_mapping=dict(zip(d1,d2))
Drive1=st.selectbox('Drive wheels', d1)
Drive=Drive_mapping[Drive1]
# ...................................................................................
w1=['Left wheel', 'Right-hand drive']
w2=[0,1]
Wheel_mapping=dict(zip(w1,w2))
Wheel1=st.selectbox('Wheel',w1)
Wheel=Wheel_mapping[Wheel1]
# ....................................................................................
cc1=['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
       'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
cc2=[12,  1, 14,  7,  2, 13, 11,  8,  6, 15,  3,  5,  0,  4, 10,  9]
color_mapping=dict(zip(cc1,cc2))
Color1=st.selectbox('Color', cc1)
Color=color_mapping[Color1]
# .....................................................................................

Engine=st.selectbox('Engine volume', [3.5, 3. , 1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 3.3, 1.4, 2.3,
       3.2, 1.2, 1.7, 2.9, 1.9, 2.7, 2.8, 2.1, 1. , 0.8, 3.4, 2.6, 1.1])
# ..................................................................................................
Airbags=st.selectbox('Airbags', [12,  8,  2,  0,  4,  6, 10,  3,  1, 16,  5,  7,  9, 11, 14, 15, 13])  
# ................................................................................................... 
Age=st.number_input('Age')
# ....................................................................................................
Mileage=st.number_input('Mileage')
# ....................................................................................................
Levy=st.number_input('Levy')
# ..................................................................................................
df=pd.DataFrame({'Manufacturer':Manufacturer,'Model':Model,'Category':Category,'Leather interior':Leather,'Fuel type':Fuel,
                    'Mileage':Mileage,'Gear box type':Gear,'Drive wheels':Drive,'Wheel':Wheel,'Color':Color,'Levy':Levy,
                    'Engine volume':Engine,'Airbags':Airbags,'Age':Age },index=[0])
p=st.sidebar.button('Predict Price')
if p:
    Pre=data.predict(df)
    st.sidebar.write('Pice is :',Pre)
    st.table(df)
