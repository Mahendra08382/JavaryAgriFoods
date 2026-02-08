import streamlit as st
import urllib.parse
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(
    page_title="Javary Agri Foods",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

EMAIL_SENDER = "javaryagrifoods@gmail.com"
EMAIL_PASSWORD = "your_app_password_here"
EMAIL_RECEIVER = "javaryagrifoods@gmail.com"
WHATSAPP_NUMBER = "918549939928"

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "show_cart" not in st.session_state:
    st.session_state.show_cart = False

products_data = [
    {"name": "Jowar Roti", "price": 50, "original_price": 65, "unit": "Pack of 5",
     "desc": "Premium quality jowar flour roti", "badge": "Bestseller", "badge_color": "#9c27b0",
     "image": r"C:\Users\2025\JavaryAgriFoods\images\roti_banner.jpg", "emoji": "🫓", "rating": 4.9, "reviews": 128},
    {"name": "Bajra Roti", "price": 50, "original_price": 60, "unit": "Pack of 5",
     "desc": "Nutritious pearl millet flatbread", "badge": "Organic", "badge_color": "#ff8f00",
     "image": r"C:\Users\2025\JavaryAgriFoods\images\roti_banner.jpg", "emoji": "🥙", "rating": 4.8, "reviews": 95},
    {"name": "Rice Roti", "price": 50, "original_price": 60, "unit": "Pack of 5",
     "desc": "Traditional Karnataka akki roti", "badge": "Organic", "badge_color": "#ff8f00",
     "image": r"C:\Users\2025\JavaryAgriFoods\images\roti_banner.jpg", "emoji": "🍚", "rating": 4.7, "reviews": 72},
    {"name": "Wheat Chapati", "price": 80, "original_price": 100, "unit": "Pack of 10",
     "desc": "Soft whole wheat phulka chapatis", "badge": "Popular", "badge_color": "#2196f3",
     "image": r"C:\Users\2025\JavaryAgriFoods\images\roti_banner.jpg", "emoji": "🫓", "rating": 4.9, "reviews": 156},
    {"name": "Puran Poli", "price": 80, "original_price": 100, "unit": "Pack of 4",
     "desc": "Sweet stuffed bread with dal filling", "badge": "Festival Special", "badge_color": "#e91e63",
     "image": r"C:\Users\2025\JavaryAgriFoods\images\roti_banner.jpg", "emoji": "🥮", "rating": 5.0, "reviews": 203},
    {"name": "Family Combo Meal", "price": 199, "original_price": 280, "unit": "Serves 4",
     "desc": "Assorted rotis + chapatis + sweet", "badge": "Best Value", "badge_color": "#2e7d32",
     "image": r"C:\Users\2025\JavaryAgriFoods\images\roti_banner.jpg", "emoji": "📦", "rating": 4.9, "reviews": 89},
]

def send_order_email(order_msg, customer_name, customer_phone):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = f"🌾 New Order - {customer_name} ({customer_phone})"
        msg.attach(MIMEText(order_msg, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Email error: {e}")
        return False

def send_whatsapp_callmebot(order_msg):
    import requests
    CALLMEBOT_API_KEY = "YOUR_API_KEY_HERE"
    url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_NUMBER}&text={urllib.parse.quote(order_msg)}&apikey={CALLMEBOT_API_KEY}"
    try:
        return requests.get(url, timeout=30).status_code == 200
    except Exception as e:
        st.error(f"CallMeBot error: {e}")
        return False

def increase_qty(name, price, unit):
    key = f"qty_{name}"
    st.session_state[key] = st.session_state.get(key, 0) + 1
    st.session_state.cart[name] = {"qty": st.session_state[key], "price": price, "unit": unit}

def decrease_qty(name):
    key = f"qty_{name}"
    current = st.session_state.get(key, 0)
    if current > 0:
        st.session_state[key] = current - 1
        if st.session_state[key] == 0 and name in st.session_state.cart:
            del st.session_state.cart[name]
        elif st.session_state[key] > 0:
            st.session_state.cart[name]["qty"] = st.session_state[key]

def toggle_cart():
    st.session_state.show_cart = not st.session_state.show_cart


# ===== CSS =====
st.markdown("""
<style>
/* ===== REMOVE ALL STREAMLIT BRANDING ===== */

/* Hide "Made with Streamlit" footer */
footer { display: none !important; visibility: hidden !important; }

/* Hide Streamlit footer container */
.reportview-container .main footer { display: none !important; }

/* Hide footer via data attribute */
footer[class*="st-"] { display: none !important; }

/* Hide "Manage app" button */
.stApp [data-testid="manage-app-button"] { display: none !important; }

/* Hide Streamlit header bar */
header { display: none !important; visibility: hidden !important; }
header[data-testid="stHeader"] { display: none !important; }

/* Hide hamburger menu */
#MainMenu { display: none !important; visibility: hidden !important; }
button[kind="header"] { display: none !important; }

/* Hide deploy button */
.stDeployButton { display: none !important; }
[data-testid="stDeployButton"] { display: none !important; }

/* Hide Streamlit toolbar */
[data-testid="stToolbar"] { display: none !important; }

/* Hide "Hosted with Streamlit" */
[data-testid="stDecoration"] { display: none !important; }

/* Hide status widget (running/rerunning) */
[data-testid="stStatusWidget"] { display: none !important; }

/* Hide any remaining Streamlit footer text */
.viewerBadge_container__r5tak { display: none !important; }
.viewerBadge_link__qRIco { display: none !important; }

/* Extra safety - hide anything at page bottom from Streamlit */
iframe[title="streamlit_badge"] { display: none !important; }

/* Remove bottom padding that Streamlit adds for footer */
.block-container { padding-bottom: 0 !important; }
.main .block-container { padding-bottom: 0 !important; }

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* { font-family: 'Poppins', sans-serif; box-sizing: border-box; }

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* { font-family: 'Poppins', sans-serif; box-sizing: border-box; }

html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-theme="dark"],
[data-theme="dark"] [data-testid="stAppViewContainer"] {
    background-color: #ffffff !important;
    color: #1a1a1a !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

.block-container {
    padding-top: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100% !important;
}

.stMarkdown, .stMarkdown p, .stMarkdown span,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4,
[data-testid="stMarkdownContainer"] strong,
[data-testid="stMarkdownContainer"] div {
    color: #1a1a1a !important;
}

/* ===== FLOATING STICKY CART BAR ===== */
.floating-cart {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(135deg, #1a5d1a, #2e7d32) !important;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 99999;
    box-shadow: 0 -4px 20px rgba(0,0,0,0.2);
}

.floating-cart * { color: #ffffff !important; }

.fc-left {
    display: flex;
    align-items: center;
    gap: 12px;
}

.fc-icon {
    background: rgba(255,255,255,0.2);
    width: 42px; height: 42px;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    position: relative;
}

.fc-badge {
    position: absolute;
    top: -6px; right: -6px;
    background: #ff5722;
    color: #ffffff !important;
    font-size: 11px; font-weight: 800;
    width: 20px; height: 20px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
}

.fc-info { line-height: 1.3; }

.fc-items {
    font-size: 13px;
    font-weight: 600;
    color: rgba(255,255,255,0.85) !important;
}

.fc-total {
    font-size: 20px;
    font-weight: 900;
    color: #ffffff !important;
}

.fc-btn {
    background: #ff8f00;
    color: #ffffff !important;
    padding: 12px 28px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 700;
    font-size: 14px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 3px 12px rgba(255,143,0,0.4);
    transition: all 0.3s;
    white-space: nowrap;
}

.fc-btn:hover {
    background: #e65100;
    transform: translateY(-2px);
}

/* TOP BAR */
.top-bar {
    background: #1a5d1a !important; text-align: center;
    padding: 6px 10px; font-size: 11px; font-weight: 500; overflow: hidden;
}
.top-bar, .top-bar *, .top-bar span { color: #ffffff !important; }
.top-bar .scroll-text { display: inline-block; animation: scroll-left 22s linear infinite; }
@keyframes scroll-left { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

/* NAVBAR — MOBILE FRIENDLY */
.navbar {
    background: #ffffff !important;
    padding: 10px 15px;
    display: flex; align-items: center; justify-content: space-between;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    border-bottom: 3px solid #2e7d32;
    position: sticky; top: 0; z-index: 9999;
}
.brand { display: flex; align-items: center; gap: 8px; }
.brand .logo { font-size: 28px; }
.brand h2 { margin: 0; font-size: 18px; font-weight: 800; color: #1a5d1a !important; }
.brand span { font-size: 9px; color: #888 !important; letter-spacing: 1px; text-transform: uppercase; }
.nav-links { display: flex; gap: 18px; }
.nav-links a { text-decoration: none; color: #333 !important; font-weight: 600; font-size: 12px; text-transform: uppercase; }
.nav-links a:hover { color: #2e7d32 !important; }

/* HERO — MOBILE FRIENDLY */
.hero {
    background: linear-gradient(135deg, #0d3b0d 0%, #2e7d32 40%, #4caf50 70%, #81c784 100%);
    padding: 40px 20px;
    display: flex; align-items: center; justify-content: space-between;
    min-height: 280px; position: relative; overflow: hidden;
    flex-wrap: wrap; gap: 20px;
}
.hero::before { content: ''; position: absolute; top: -50%; right: -15%; width: 400px; height: 400px; background: rgba(255,255,255,0.04); border-radius: 50%; }
.hero-text { max-width: 520px; z-index: 2; flex: 1; min-width: 250px; }
.hero-badge { display: inline-block; background: #ff8f00; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 14px; }
.hero-badge, .hero-text h1, .hero-text p, .hero-btn { color: #ffffff !important; }
.hero-text h1 { font-size: 32px; font-weight: 900; line-height: 1.15; margin: 0 0 12px; }
.hero-text h1 em { color: #ffeb3b !important; font-style: normal; }
.hero-text p { font-size: 14px; opacity: 0.9; line-height: 1.6; margin-bottom: 22px; }
.hero-btn { background: #ff8f00; padding: 12px 28px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 14px; box-shadow: 0 4px 14px rgba(255,143,0,0.4); display: inline-block; }
.hero-btn:hover { background: #e65100; }
.hero-emoji { font-size: 100px; z-index: 2; animation: bob 3s ease-in-out infinite; filter: drop-shadow(0 10px 25px rgba(0,0,0,0.3)); }
@keyframes bob { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }

/* FEATURES — MOBILE FRIENDLY */
.features {
    display: flex; justify-content: center; background: #ffffff !important;
    box-shadow: 0 3px 15px rgba(0,0,0,0.05); border-bottom: 1px solid #eee;
    flex-wrap: wrap;
}
.feat {
    display: flex; align-items: center; gap: 10px; padding: 15px 20px;
    border-right: 1px solid #f0f0f0; flex: 1; justify-content: center;
    min-width: 150px;
}
.feat:last-child { border-right: none; }
.feat-icon { font-size: 24px; background: #e8f5e9; padding: 8px; border-radius: 50%; width: 42px; height: 42px; display: flex; align-items: center; justify-content: center; }
.feat h4 { margin: 0; font-size: 12px; font-weight: 700; color: #1a1a1a !important; }
.feat p { margin: 0; font-size: 10px; color: #777 !important; }

/* SECTION HEADER */
.sec-head { text-align: center; padding: 35px 15px 8px; }
.sec-badge { display: inline-block; background: #e8f5e9; color: #2e7d32 !important; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px; }
.sec-head h2 { font-size: 24px; font-weight: 800; color: #1a1a1a !important; margin: 0; }
.sec-head h2 em { color: #2e7d32 !important; font-style: normal; }
.sec-head p { font-size: 13px; color: #777 !important; margin-top: 6px; }

/* PRODUCT CARD — MOBILE FRIENDLY */
.p-card-top { background: #ffffff !important; border-radius: 14px 14px 0 0; border: 1px solid #e0e0e0; border-bottom: none; position: relative; margin-top: 12px; height: 8px; }
.p-badge-wrap { position: absolute; top: 6px; left: 8px; z-index: 10; }
.p-badge-tag { display: inline-block; padding: 3px 9px; border-radius: 4px; font-size: 9px; font-weight: 700; color: #ffffff !important; text-transform: uppercase; }
.p-emoji-area { height: 160px; width: 100%; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #f8faf8, #e8f5e9); border-left: 1px solid #e0e0e0; border-right: 1px solid #e0e0e0; }
.p-emoji { font-size: 60px; }

.p-card-bottom { background: #ffffff !important; border-radius: 0 0 14px 14px; border: 1px solid #e0e0e0; border-top: none; padding: 14px; margin-bottom: 4px; }
.p-stars { color: #ff8f00 !important; font-size: 12px; }
.p-rev { font-size: 10px; color: #999 !important; margin-left: 3px; }
.p-card-bottom h3 { font-size: 14px; font-weight: 700; color: #1a1a1a !important; margin: 5px 0 2px; }
.p-desc { font-size: 11px; color: #888 !important; margin: 0 0 6px; }
.p-unit { display: inline-block; background: #f0f0f0; padding: 2px 8px; border-radius: 4px; font-size: 10px; color: #555 !important; margin-bottom: 8px; }
.p-prices { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.p-now { font-size: 20px; font-weight: 800; color: #2e7d32 !important; }
.p-was { font-size: 13px; color: #bbb !important; text-decoration: line-through; }
.p-off { background: #fff3e0; color: #ff8f00 !important; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 700; }

[data-testid="stImage"] { border-left: 1px solid #e0e0e0; border-right: 1px solid #e0e0e0; overflow: hidden; margin: 0 !important; }
[data-testid="stImage"] img { height: 160px !important; object-fit: cover !important; border-radius: 0 !important; }

/* QTY DISPLAY */
.qty-display { text-align: center; font-size: 18px; font-weight: 800; padding: 4px 0; min-height: 36px; display: flex; align-items: center; justify-content: center; }
.qty-zero { color: #ccc !important; }
.qty-active { color: #2e7d32 !important; }

/* WHY US — MOBILE FRIENDLY */
.why-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 15px; padding: 20px 15px 40px; }
.why-card { background: #ffffff !important; border-radius: 12px; padding: 20px 15px; text-align: center; border: 2px solid #f0f0f0; transition: all 0.35s; }
.why-card:hover { transform: translateY(-4px); box-shadow: 0 10px 25px rgba(0,0,0,0.06); border-color: #c8e6c9; }
.why-icon { font-size: 34px; margin-bottom: 10px; display: block; }
.why-card h4 { font-size: 13px; font-weight: 700; color: #1a1a1a !important; margin: 0 0 4px; }
.why-card p { font-size: 11px; color: #777 !important; margin: 0; line-height: 1.5; }

/* CONTACT — MOBILE */
.contact-grid { display: grid; grid-template-columns: 1fr; gap: 15px; padding: 15px 15px 35px; }
.c-card { text-align: center; padding: 22px 15px; border-radius: 12px; border: 2px solid #f0f0f0; background: #ffffff !important; transition: all 0.3s; }
.c-card:hover { border-color: #2e7d32; box-shadow: 0 6px 20px rgba(46,125,50,0.08); }
.c-icon { font-size: 30px; margin-bottom: 10px; display: block; }
.c-card h4 { font-size: 14px; font-weight: 700; color: #1a1a1a !important; margin: 0 0 4px; }
.c-card p { font-size: 12px; color: #555 !important; margin: 0; line-height: 1.5; }

/* FOOTER */
.site-footer { background: #1a1a1a !important; padding: 35px 15px 0; margin-bottom: 70px; }
.site-footer h3 { font-size: 15px; font-weight: 700; color: #4caf50 !important; margin: 0 0 12px; }
.site-footer p { font-size: 12px; color: #aaa !important; line-height: 1.7; margin: 0 0 10px; }
.footer-grid { display: grid; grid-template-columns: 1fr; gap: 25px; padding-bottom: 25px; border-bottom: 1px solid #333; }
.site-footer ul { list-style: none; padding: 0; margin: 0; }
.site-footer ul li { margin-bottom: 6px; }
.site-footer ul li a { color: #aaa !important; text-decoration: none; font-size: 12px; }
.site-footer ul li a:hover { color: #4caf50 !important; }
.footer-bottom { text-align: center; padding: 18px 0; color: #666 !important; font-size: 12px; }
.footer-bottom em { color: #4caf50 !important; font-style: normal; font-weight: 600; }

/* SUCCESS */
.success-box { background: linear-gradient(135deg, #e8f5e9, #c8e6c9) !important; border: 2px solid #4caf50; border-radius: 16px; padding: 30px 20px; text-align: center; margin: 15px 0; }
.success-box .check { font-size: 50px; margin-bottom: 8px; display: block; }
.success-box h2 { color: #1a5d1a !important; font-size: 22px; font-weight: 800; margin: 0 0 6px; }
.success-box p { color: #444 !important; font-size: 13px; margin: 0; }

/* EMPTY CART */
.empty-cart { text-align: center; padding: 30px 15px; background: #fff8e1 !important; border-radius: 14px; border: 2px dashed #ffcc02; }
.empty-cart h3 { color: #333 !important; margin: 8px 0 4px; font-size: 16px; }
.empty-cart p { color: #888 !important; font-size: 13px; }

/* BUTTONS */
div.stButton > button, div.stFormSubmitButton > button {
    background: linear-gradient(135deg, #2e7d32, #4caf50) !important;
    color: #ffffff !important; border: none !important;
    padding: 12px 25px !important; border-radius: 50px !important;
    font-weight: 700 !important; font-size: 14px !important;
    text-transform: uppercase !important; letter-spacing: 0.5px !important;
    width: 100% !important;
}
div.stButton > button:hover, div.stFormSubmitButton > button:hover {
    background: linear-gradient(135deg, #1a5d1a, #2e7d32) !important;
    color: #ffffff !important;
}
div.stButton > button:active, div.stButton > button:focus,
div.stFormSubmitButton > button:active, div.stFormSubmitButton > button:focus { color: #ffffff !important; }
div.stButton > button p, div.stButton > button span, div.stButton > button div,
div.stFormSubmitButton > button p, div.stFormSubmitButton > button span, div.stFormSubmitButton > button div { color: #ffffff !important; }

/* INPUTS */
.stTextInput > div > div > input, .stTextArea > div > div > textarea {
    border: 2px solid #e0e0e0 !important; border-radius: 10px !important;
    color: #1a1a1a !important; background: #ffffff !important; font-size: 14px !important;
}
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
    border-color: #2e7d32 !important; box-shadow: 0 0 0 3px rgba(46,125,50,0.1) !important;
}
.stTextInput > div > div > input::placeholder, .stTextArea > div > div > textarea::placeholder { color: #999 !important; }
.stSelectbox > div > div { border: 2px solid #e0e0e0 !important; border-radius: 10px !important; color: #1a1a1a !important; background: #ffffff !important; }
.stSelectbox > div > div > div { color: #1a1a1a !important; }
.stNumberInput > div > div > input { border: 2px solid #e0e0e0 !important; border-radius: 10px !important; color: #1a1a1a !important; background: #ffffff !important; }
.stTextInput label, .stTextArea label, .stSelectbox label, .stNumberInput label, .stRadio label, [data-testid="stForm"] label { color: #333 !important; font-weight: 600 !important; }
.stRadio > div label p { color: #333 !important; }
.stAlert { border-radius: 10px !important; }
hr { border-color: #e0e0e0 !important; }

/* ===== DESKTOP OVERRIDES ===== */
@media (min-width: 769px) {
    .navbar { padding: 14px 50px; }
    .brand .logo { font-size: 34px; }
    .brand h2 { font-size: 22px; }
    .brand span { font-size: 11px; }
    .nav-links { gap: 28px; }
    .nav-links a { font-size: 13px; }

    .hero { padding: 70px; min-height: 380px; }
    .hero-text h1 { font-size: 44px; }
    .hero-text p { font-size: 16px; }
    .hero-emoji { font-size: 150px; }

    .feat { padding: 22px 36px; }
    .feat-icon { font-size: 28px; width: 50px; height: 50px; }
    .feat h4 { font-size: 13px; }

    .sec-head { padding: 50px 40px 8px; }
    .sec-head h2 { font-size: 32px; }

    .p-emoji-area { height: 200px; }
    .p-emoji { font-size: 80px; }
    .p-card-bottom { padding: 18px; }
    .p-card-bottom h3 { font-size: 15px; }
    .p-now { font-size: 22px; }
    [data-testid="stImage"] img { height: 200px !important; }

    .why-grid { grid-template-columns: repeat(4,1fr); padding: 28px 50px 50px; gap: 22px; }

    .contact-grid { grid-template-columns: repeat(3,1fr); padding: 25px 50px 45px; }

    .footer-grid { grid-template-columns: 2fr 1fr 1fr; }
    .site-footer { padding: 50px 50px 0; }
}
</style>
""", unsafe_allow_html=True)


# ===== TOP BAR =====
st.markdown("""
<div class="top-bar"><span class="scroll-text">
    🌾 Welcome to Javary Agri Foods! &nbsp;|&nbsp; 🚚 Free Delivery Above ₹200 &nbsp;|&nbsp;
    📞 +91 8549939928 &nbsp;|&nbsp; 🌿 100% Organic &amp; Fresh &nbsp;|&nbsp; 📍 Karwar
</span></div>
""", unsafe_allow_html=True)

# ===== NAVBAR =====
st.markdown("""
<div class="navbar">
    <div class="brand"><span class="logo">🌾</span><div><h2>Javary Agri Foods</h2><span>Fresh • Organic • Traditional</span></div></div>
    <div class="nav-links"><a href="#home">Home</a><a href="#products">Products</a><a href="#order">Order</a><a href="#contact">Contact</a></div>
</div>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown("""
<div class="hero" id="home">
    <div class="hero-text">
        <div class="hero-badge">🔥 Farm Fresh Daily</div>
        <h1>Traditional <em>Organic Rotis</em> Delivered To You</h1>
        <p>Handmade from locally sourced grains. Zero preservatives. Authentic Karnataka taste.</p>
        <a href="#products" class="hero-btn">🛒 Order Now</a>
    </div>
    <span class="hero-emoji">🫓</span>
</div>
""", unsafe_allow_html=True)

# ===== FEATURES =====
st.markdown("""
<div class="features">
    <div class="feat"><span class="feat-icon">🚚</span><div><h4>Free Delivery</h4><p>Above ₹200</p></div></div>
    <div class="feat"><span class="feat-icon">🌿</span><div><h4>100% Organic</h4><p>No preservatives</p></div></div>
    <div class="feat"><span class="feat-icon">⏰</span><div><h4>Fresh Daily</h4><p>Every morning</p></div></div>
    <div class="feat"><span class="feat-icon">🔒</span><div><h4>Hygienic</h4><p>FSSAI certified</p></div></div>
</div>
""", unsafe_allow_html=True)

# ===== PRODUCTS =====
st.markdown("""
<div class="sec-head" id="products">
    <div class="sec-badge">⭐ Our Products</div>
    <h2>Select Items &amp; <em>Quantity</em></h2>
    <p>Use + and − buttons to add items</p>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for i, prod in enumerate(products_data):
    with cols[i % 3]:
        discount = round((1 - prod["price"] / prod["original_price"]) * 100)
        qty_key = f"qty_{prod['name']}"
        if qty_key not in st.session_state:
            st.session_state[qty_key] = 0
        current_qty = st.session_state[qty_key]

        st.markdown(f"""
        <div class="p-card-top"><div class="p-badge-wrap"><span class="p-badge-tag" style="background:{prod['badge_color']}">{prod['badge']}</span></div></div>
        """, unsafe_allow_html=True)

        if prod["image"] and os.path.isfile(prod["image"]):
            st.image(prod["image"], use_container_width=True)
        else:
            st.markdown(f'<div class="p-emoji-area"><span class="p-emoji">{prod["emoji"]}</span></div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="p-card-bottom">
            <span class="p-stars">{'★' * int(prod['rating'])}{'☆' * (5 - int(prod['rating']))}</span>
            <span class="p-rev">({prod['reviews']})</span>
            <h3>{prod['name']}</h3>
            <p class="p-desc">{prod['desc']}</p>
            <span class="p-unit">📏 {prod['unit']}</span>
            <div class="p-prices">
                <span class="p-now">₹{prod['price']}</span>
                <span class="p-was">₹{prod['original_price']}</span>
                <span class="p-off">{discount}% OFF</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        b1, b2, b3 = st.columns([1, 1, 1])
        with b1:
            st.button("➖", key=f"minus_{prod['name']}", on_click=decrease_qty, args=(prod["name"],), use_container_width=True)
        with b2:
            qty_class = "qty-active" if current_qty > 0 else "qty-zero"
            st.markdown(f'<div class="qty-display {qty_class}">{current_qty}</div>', unsafe_allow_html=True)
        with b3:
            st.button("➕", key=f"plus_{prod['name']}", on_click=increase_qty, args=(prod["name"], prod["price"], prod["unit"]), use_container_width=True)

# Sync cart
current_cart = {}
for prod in products_data:
    qty_key = f"qty_{prod['name']}"
    qty_val = st.session_state.get(qty_key, 0)
    if qty_val > 0:
        current_cart[prod["name"]] = {"qty": qty_val, "price": prod["price"], "unit": prod["unit"]}
st.session_state.cart = current_cart


# ===== FLOATING STICKY CART BAR =====
if st.session_state.cart:
    cart_total = sum(d["qty"] * d["price"] for d in st.session_state.cart.values())
    cart_qty = sum(d["qty"] for d in st.session_state.cart.values())
    cart_items = len(st.session_state.cart)

    st.markdown(f"""
    <div class="floating-cart">
        <div class="fc-left">
            <div class="fc-icon">
                🛒
                <div class="fc-badge">{cart_qty}</div>
            </div>
            <div class="fc-info">
                <div class="fc-items">{cart_items} item(s) added</div>
                <div class="fc-total">₹{cart_total}</div>
            </div>
        </div>
        <a href="#order" class="fc-btn">View Cart & Order →</a>
    </div>
    """, unsafe_allow_html=True)


# ===== WHY US =====
st.markdown("""
<div class="sec-head"><div class="sec-badge">💚 Why Us</div><h2>Why <em>Javary Agri Foods?</em></h2></div>
<div class="why-grid">
    <div class="why-card"><span class="why-icon">🌾</span><h4>Farm Fresh</h4><p>Local Karnataka farmers</p></div>
    <div class="why-card"><span class="why-icon">👩‍🍳</span><h4>Handmade</h4><p>Traditional methods</p></div>
    <div class="why-card"><span class="why-icon">🚫</span><h4>No Chemicals</h4><p>Zero preservatives</p></div>
    <div class="why-card"><span class="why-icon">🚚</span><h4>Same Day</h4><p>Order by 10 AM</p></div>
</div>
""", unsafe_allow_html=True)


# ===== ORDER SECTION =====
st.markdown("""
<div class="sec-head" id="order">
    <div class="sec-badge">🛒 Checkout</div>
    <h2>Submit Your <em>Order</em></h2>
    <p>Review cart, fill details, submit!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='max-width:780px; margin:0 auto; padding:5px 15px 80px;'>", unsafe_allow_html=True)

if st.session_state.cart:
    grand_total = sum(d["qty"] * d["price"] for d in st.session_state.cart.values())
    item_count = sum(d["qty"] for d in st.session_state.cart.values())

    st.success(f"🛒 **Your Cart** — {len(st.session_state.cart)} item(s), {item_count} total qty")

    for item_name, item_data in st.session_state.cart.items():
        line_total = item_data["qty"] * item_data["price"]
        c1, c2, c3 = st.columns([4, 1, 1])
        with c1:
            st.markdown(f"🫓 **{item_name}** `{item_data['unit']}`")
        with c2:
            st.markdown(f"**× {item_data['qty']}**")
        with c3:
            st.markdown(f"**₹{line_total}**")

    st.divider()
    tc1, tc2 = st.columns([4, 2])
    with tc1:
        st.markdown("### 💰 Grand Total")
    with tc2:
        st.markdown(f"### ₹{grand_total}")
    st.divider()

    st.info("📡 **Notification Method**")
    notify_method = st.radio("method",
        ["📧 Email (Recommended)", "💬 WhatsApp via CallMeBot"],
        index=0, label_visibility="collapsed")
    st.divider()

    st.info("📋 **Your Details**")

    with st.form("order_form"):
        cust_name = st.text_input("👤 Full Name", placeholder="Your name")
        cust_phone = st.text_input("📞 Phone", placeholder="+91 XXXXXXXXXX")
        cust_address = st.text_area("📍 Delivery Address", placeholder="Full address with landmark & pincode")

        c3, c4 = st.columns(2)
        with c3:
            delivery_time = st.selectbox("⏰ Time", ["Morning (8–12)", "Afternoon (12–4)", "Evening (4–8)"])
        with c4:
            payment = st.selectbox("💳 Payment", ["Cash on Delivery", "UPI / GPay", "Bank Transfer"])

        notes = st.text_input("📝 Instructions (optional)")
        submitted = st.form_submit_button("✅ SUBMIT ORDER")

        if submitted:
            if cust_name and cust_phone and cust_address:
                order_msg = f"🌾 NEW ORDER\n{'='*30}\n\n"
                order_msg += f"👤 {cust_name}\n📞 {cust_phone}\n📍 {cust_address}\n"
                order_msg += f"⏰ {delivery_time}\n💳 {payment}\n\n🛒 ITEMS:\n{'-'*25}\n"
                for item_name, item_data in st.session_state.cart.items():
                    lt = item_data["qty"] * item_data["price"]
                    order_msg += f"• {item_name} ({item_data['unit']}) x{item_data['qty']} = ₹{lt}\n"
                order_msg += f"{'-'*25}\n💰 TOTAL: ₹{grand_total}\n"
                if notes: order_msg += f"📝 {notes}\n"

                ok = False
                if "Email" in notify_method:
                    with st.spinner("📧 Sending..."): ok = send_order_email(order_msg, cust_name, cust_phone)
                else:
                    with st.spinner("💬 Sending..."): ok = send_whatsapp_callmebot(order_msg)

                if ok:
                    st.markdown(f"""
                    <div class="success-box"><span class="check">✅</span><h2>Order Submitted!</h2>
                    <p>₹{grand_total} • {len(st.session_state.cart)} items • {item_count} qty</p>
                    <p style="margin-top:8px;">We'll contact you shortly!</p></div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.warning("⚠️ Auto-send failed:")
                    enc = urllib.parse.quote(order_msg)
                    st.markdown(f"""
                    <a href="https://wa.me/{WHATSAPP_NUMBER}?text={enc}" target="_blank" style="
                        display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,#25d366,#128c7e);
                        color:#ffffff !important;padding:12px 30px;border-radius:50px;text-decoration:none;font-weight:700;">
                        💬 Send via WhatsApp</a>
                    """, unsafe_allow_html=True)
            else:
                st.error("⚠️ Fill Name, Phone, Address.")
else:
    st.markdown("""
    <div class="empty-cart"><span style="font-size:45px;">🛒</span>
    <h3>Your cart is empty</h3><p>Use ➕ on any product to add it</p></div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== CONTACT =====
st.markdown("""
<div class="sec-head" id="contact"><div class="sec-badge">📞 Contact</div><h2>Get In <em>Touch</em></h2></div>
<div class="contact-grid">
    <div class="c-card"><span class="c-icon">📍</span><h4>Location</h4><p>Habbu Complex, Habbuwada<br>Karwar – 581301</p></div>
    <div class="c-card"><span class="c-icon">📞</span><h4>Call Us</h4><p>+91 8549939928<br>Mon–Sat: 7AM–9PM</p></div>
    <div class="c-card"><span class="c-icon">📧</span><h4>Email</h4><p>javaryagrifoods@gmail.com</p></div>
</div>
""", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
<div class="site-footer">
    <div class="footer-grid">
        <div><h3>🌾 Javary Agri Foods</h3><p>Traditional recipes, farm-fresh, delivered daily.</p></div>
        <div><h3>Links</h3><ul><li><a href="#home">→ Home</a></li><li><a href="#products">→ Products</a></li><li><a href="#order">→ Order</a></li></ul></div>
        <div><h3>Products</h3><ul><li><a href="#">→ Jowar Roti</a></li><li><a href="#">→ Bajra Roti</a></li><li><a href="#">→ Chapati</a></li></ul></div>
    </div>
    <div class="footer-bottom">© 2026 <em>Javary Agri Foods</em> • Made with ❤️ in Karwar</div>
</div>
""", unsafe_allow_html=True)

# ===== FLOATING WHATSAPP =====
st.markdown(f"""
<a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" style="
    position:fixed;bottom:80px;right:20px;background:#25d366;color:#ffffff !important;
    width:50px;height:50px;border-radius:50%;display:flex;align-items:center;
    justify-content:center;font-size:24px;z-index:99998;text-decoration:none;
    box-shadow:0 4px 15px rgba(37,211,102,0.45);">💬</a>
""", unsafe_allow_html=True)