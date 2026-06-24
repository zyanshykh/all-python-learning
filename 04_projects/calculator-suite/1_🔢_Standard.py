import streamlit as st
from modules.ui_components import add_footer

# Page Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered", initial_sidebar_state="collapsed")

# Apply Styling
def apply_style():
    st.markdown("""
        <style>
        .block-container { max-width: 500px !important; padding: 1rem !important; }
        div.stButton > button { width: 100% !important; height: 50px !important; margin: 2px !important; }
        .stTextInput > div > div > input { text-align: right !important; font-size: 24px !important; }
        </style>
    """, unsafe_allow_html=True)

apply_style()

st.title("🔢 Standard Calculator")

# State Initialization
if "expr" not in st.session_state: st.session_state.expr = ""
if "history" not in st.session_state: st.session_state.history = []

# Input Display (Sirf EK baar)
user_typed = st.text_input("Input", value=st.session_state.expr, label_visibility="collapsed", key="calc_input")

# Update logic: Agar user khud type kare toh session update ho
if user_typed != st.session_state.expr:
    st.session_state.expr = user_typed

# Button Grid
btn_rows = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for row in btn_rows:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        if cols[i].button(label, use_container_width=True):
            if label == "C": 
                st.session_state.expr = ""
            elif label == "=":
                try:
                    result = str(eval(st.session_state.expr))
                    st.session_state.history.append(f"{st.session_state.expr} = {result}")
                    st.session_state.expr = result
                except:
                    st.session_state.expr = "Error"
            else: 
                st.session_state.expr += label
            st.rerun()

# History Sidebar
if st.sidebar.button("Clear History"): st.session_state.history = []
st.sidebar.subheader("History")
for item in reversed(st.session_state.history):
    st.sidebar.text(item)

add_footer()