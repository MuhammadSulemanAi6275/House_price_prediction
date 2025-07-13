import streamlit as st
import pandas as pd
import joblib

# ===========================
# 🎨 Background and Credits Style
# ===========================
def set_bg():
    st.markdown("""
        <style>
        .stApp {
            background-image: url('https://www.slideteam.net/media/catalog/product/cache/330x186/h/o/house_price_prediction_through_machine_learning_ml_cd_slide01.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .credits-top-right {
            position: fixed;
            top: 10px;
            right: 20px;
            font-size: 18px;
            color: #ffffff;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 6px 10px;
            border-radius: 8px;
        }
        .credits-bottom-right {
            position: fixed;
            bottom: 10px;
            right: 20px;
            font-size: 16px;
            color: #ffffff;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 6px 10px;
            border-radius: 8px;
        }
        </style>
        <div class="credits-top-right">👨‍🏫 Guided by: Respected Sir Hamza</div>
        <div class="credits-bottom-right">👨‍💻 Developed by: Muhammad Suleman Shah</div>
    """, unsafe_allow_html=True)

set_bg()

# ======================
# 🏠 Title
# ======================
st.markdown("<h1 style='text-align: center; color: white;'>🏠 Smart House Price Prediction</h1>", unsafe_allow_html=True)

# ======================
# 🔄 Load Model
# ======================
@st.cache_resource
def load_model():
    return joblib.load("house_price_model.pkl")

model = load_model()

# ======================
# 📋 Sidebar Inputs
# ======================
st.sidebar.markdown("<h2 style='color:white;'>Enter House Features</h2>", unsafe_allow_html=True)

square_feet = st.sidebar.number_input("📏 Square Feet", min_value=500, max_value=10000, value=2000)
bedrooms = st.sidebar.slider("🛏️ Bedrooms", 1, 10, value=3)
bathrooms = st.sidebar.slider("🛁 Bathrooms", 1, 5, value=2)
year_built = st.sidebar.number_input("📅 Year Built", min_value=1900, max_value=2025, value=2000)
neighborhood = st.sidebar.selectbox("📍 Neighborhood", ["Rural", "Suburb", "Urban"])

# ======================
# 🔢 Prepare DataFrame
# ======================
neigh_suburb = 1 if neighborhood == "Suburb" else 0
neigh_urban = 1 if neighborhood == "Urban" else 0

input_df = pd.DataFrame([[square_feet, bedrooms, bathrooms, year_built, neigh_suburb, neigh_urban]],
                        columns=['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt',
                                 'Neighborhood_Suburb', 'Neighborhood_Urban'])

# ======================
# 🖥️ Display Input Data
# ======================
#st.markdown("<h2 style='color:white;'>📋 Input Summary</h2>", unsafe_allow_html=True)
#st.dataframe(input_df.style.set_properties(**{'font-size': '80px'}), use_container_width=True)
# ======================
# 🖥️ Display Input Data (with large font)
# ======================
#st.markdown("<h2 style='color:Orange;'>📋 Input Summary</h2>", unsafe_allow_html=True)
st.markdown("""
    <h2 style="
        color: white;
        text-shadow: 2px 2px 4px black;
        font-weight: 900;
        font-size: 38px;
        font-family: 'Segoe UI', sans-serif;
        letter-spacing: 1px;
    ">
    📋 Input Summary
    </h2>
""", unsafe_allow_html=True)

# Convert DataFrame to HTML table
table_html = input_df.to_html(index=False)

# Inject custom HTML/CSS styling
styled_table = f"""
<style>
    table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 24px;  /* 3x default */
    }}
    th, td {{
        border: 2px solid Black;
        padding: 12px;
        text-align: center;
        background-color: rgba(0,0,0,0.4);
        color: white;
    }}
    th {{
        background-color: #1f77b4;
    }}
</style>
{table_html}
"""

# Display the styled table
st.markdown(styled_table, unsafe_allow_html=True)


# ======================
# 🔮 Predict Price
# ======================
#if st.sidebar.button("🔍 Predict Price"):
 #   price = model.predict(input_df)[0]
  #  st.markdown(f"<h2 style='color:lightgreen;'>🏡 Estimated House Price: ${price:,.2f}</h2>", unsafe_allow_html=True)
if st.sidebar.button("🔍 Predict Price"):
    price = model.predict(input_df)[0]
    st.markdown(f"""
        <div style="
            background-color: rgba(255, 255, 255, 0.7);
            padding: 20px;
            border-radius: 12px;
            border: 3px solid red;
            color: black;
            font-size: 30px;
            font-weight: bold;
            text-align: center;
            text-shadow: 1px 1px 2px white;
            margin-top: 20px;
        ">
        🏡 Estimated House Price: ${price:,.2f}
        </div>
    """, unsafe_allow_html=True)
