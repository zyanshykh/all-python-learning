import streamlit as st
from modules.ui_components import add_footer

# Page Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered", initial_sidebar_state="collapsed")

# 1. Custom Styling (Modern & Clean)
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; }
    /* Standardized Input Box */
    .stTextInput > div > div > input {
        font-size: 24px !important;
        height: 60px !important;
        text-align: right !important;
    }
    /* Standardized Buttons */
    div.stButton > button {
        height: 50px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔢 Standard Calculator")

# 2. State Initialization
if "expr" not in st.session_state: st.session_state.expr = ""

# 3. UI Display (Using Text Input like other pages)
user_typed = st.text_input("Calculator Input", value=st.session_state.expr, label_visibility="hidden")

# 4. Modern Button Grid
btn_rows = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""] # Empty cell for grid balance
]

for row in btn_rows:
    cols = st.columns(4)
    for i, label in enumerate(row):
        if label and cols[i].button(label, use_container_width=True):
            if label == "C": st.session_state.expr = ""
            elif label == "=":
                try: st.session_state.expr = str(eval(st.session_state.expr))
                except: st.session_state.expr = "Error"
            else: st.session_state.expr += label
            st.rerun()

# 5. Add Footer (Modular)
add_footer()