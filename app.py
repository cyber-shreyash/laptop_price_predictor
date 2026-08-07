import streamlit as st
import pandas as pd
import pickle

# Load model
with open("catboost_laptop_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻")

st.title("💻 Laptop Price Predictor")

company = st.selectbox("Company", [
    "Apple", "Dell", "HP", "Lenovo", "Asus", "Acer", "MSI", "Toshiba", "Huawei", "Xiaomi"
])

typename = st.selectbox("Type", [
    "Notebook", "Ultrabook", "Gaming", "2 in 1 Convertible", "Workstation", "Netbook"
])

inches = st.number_input("Screen Size (Inches)", 10.0, 20.0, 15.6)

ram = st.selectbox("RAM (GB)", [4, 8, 16, 32, 64])

weight = st.number_input("Weight (kg)", 0.5, 5.0, 2.0)

touchscreen = st.selectbox("Touchscreen", [0, 1])

ips = st.selectbox("IPS Display", [0, 1])

ppi = st.number_input("PPI", 50.0, 400.0, 141.0)

cpu_brand = st.selectbox("CPU Brand", [
    "Intel", "AMD", "Samsung", "Other"
])

gpu_brand = st.selectbox("GPU Brand", [
    "Intel", "Nvidia", "AMD", "ARM"
])

opsys = st.selectbox("Operating System", [
    "Windows", "Mac", "Linux", "No OS", "Chrome OS", "Other"
])

hdd = st.number_input("HDD (GB)", 0, 2000, 0)

ssd = st.number_input("SSD (GB)", 0, 2000, 256)

hybrid = st.number_input("Hybrid Storage (GB)", 0, 2000, 0)

flash_storage = st.number_input("Flash Storage (GB)", 0, 1024, 0)

if st.button("Predict Price"):

    data = pd.DataFrame({
        "Company": [company],
        "TypeName": [typename],
        "Inches": [inches],
        "Ram": [ram],
        "Weight": [weight],
        "Touchscreen": [touchscreen],
        "IPS": [ips],
        "PPI": [ppi],
        "Cpu_Brand": [cpu_brand],
        "Gpu_Brand": [gpu_brand],
        "OpSys": [opsys],
        "HDD": [hdd],
        "SSD": [ssd],
        "Hybrid": [hybrid],
        "Flash_Storage": [flash_storage]
    })

    prediction = model.predict(data)[0]

    st.success(f"Estimated Laptop Price: ₹ {prediction:,.2f}")