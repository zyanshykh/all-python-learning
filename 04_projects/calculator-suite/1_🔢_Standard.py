import streamlit as st

# 1. Page Config (Sabse upar)
st.set_page_config(
    page_title="Dev Hub | Calculator",
    page_icon="🧮",
    layout="centered"
)

# 2. CSS Styling (Ekdum sahi indentation ke sath)
def apply_style():
    st.markdown("""
        <style>
        .block-container { max-width: 450px !important; padding-top: 2rem !important; }
        div.stButton > button {
            height: 60px !important;
            font-size: 20px !important;
            border-radius: 10px !important;
        }
        .stTextInput>div>div>input {
            font-size: 32px !important;
            text-align: right !important;
            font-family: monospace !important;
        }
        </style>
    """, unsafe_allow_html=True)

apply_style()

# 3. App Logic
st.title("🔢 Smart Calculator")
st.caption("Dev Hub | Ecosystem Mode")

if "expr" not in st.session_state:
    st.session_state.expr = ""

user_typed = st.text_input("Input", value=st.session_state.expr, label_visibility="collapsed")

if user_typed != st.session_state.expr:
    st.session_state.expr = user_typed
    st.rerun()

# Grid
col1, col2, col3, col4 = st.columns(4)

buttons = [
    ["C", ".", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"]
]

for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if cols[i].button(btn, use_container_width=True):
            if btn == "C": st.session_state.expr = ""
            else: st.session_state.expr += btn
            st.rerun()

if st.button("=", use_container_width=True):
    try:
        st.session_state.expr = str(round(eval(st.session_state.expr), 4))
    except:
        st.session_state.expr = "Error"
    st.rerun()