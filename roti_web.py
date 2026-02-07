import streamlit as st
from PIL import Image


# Set page configuration
st.set_page_config(page_title="Ozone Rotis", page_icon="🥘", layout="wide")

st.markdown("""
    <style>
        .menu-card {
            background-color: #fff7e6;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            text-align: center;
            transition: 0.3s;
        }
        .menu-card:hover {
            box-shadow: 4px 4px 20px rgba(0,0,0,0.2);
        }
        .menu-card h4 {
            color: #8B0000;
            margin-bottom: 5px;
        }
        .menu-card p {
            font-size: 18px;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)



# Load a banner image
banner = Image.open("roti_banner.jpg")

# Apply custom styles
st.markdown("""
    <style>
        .main {
            background-color: #fffaf0;
        }
        h1, h2 {
            color: #8B4513;
            text-align: center;
        }
        .menu-card {
            background-color: #fff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Banner
st.image(banner, use_container_width=True)


# Title and tagline
st.markdown("## 🫓 **Welcome to Ozone Roti Center** – Organic Fresh. Soft. Delicious.")
st.markdown("<hr>", unsafe_allow_html=True)

# Menu Section
st.markdown("### 🧾 Today's Menu")
menu_items = {
    "Jawar Roti": "₹10",
    "Bajra Roti": "₹10",
    "Rice Roti": "₹10",
    "Chapati": "₹10",
    "Pooran Poli": "₹20",
    "Combo Meal (2 Jawar Roti + Sabzi)": "₹30"
}

cols = st.columns(3)
for i, (item, price) in enumerate(menu_items.items()):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="menu-card">
                <h4>{item}</h4>
                <p style='color:#8B0000; font-weight:bold'>{price}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Order Section
st.markdown("### 🛒 Place Your Order")
with st.form("order_form"):
    name = st.text_input("Your Name")
    selected_item = st.selectbox("Choose Roti Item", list(menu_items.keys()))
    quantity = st.number_input("Quantity", min_value=1, step=1)
    address = st.text_area("Delivery Address")

    submitted = st.form_submit_button("Submit Order")

    if submitted:
        st.success(f"Thank you, {name}! Your order for {quantity} x {selected_item} has been received.")
        st.info("We'll deliver it to your doorstep shortly! 😊")

st.markdown("<hr>", unsafe_allow_html=True)

# Contact Section
st.markdown("### 📞 Contact Us")
st.write("📍 Habbu Complex , Habbuwada Karwar - 581301")
st.write("📱 Phone: +91-8549939928")
st.write("📧 Email: ozonerotis@gmail.com")

st.markdown("##### Follow us on [Instagram](https://instagram.com) | [Facebook](https://facebook.com)")
