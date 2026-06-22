import streamlit as st

st.set_page_config(
    page_title="Zyan Studio | Calculator Suite",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Responsive CSS Grid Setup (Mobile Friendly)
st.markdown("""
    <style>
    /* Main Layout Responsiveness */
    .calc-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        max-width: 400px;
        margin: 0 auto;
    }
    
    /* Button Premium Styling */
    .stButton>button {
        width: 100% !important;
        border-radius: 12px !important;
        height: 2.8em !important;
        font-size: 22px !important;
        font-weight: bold !important;
        background-color: #262730;
        transition: all 0.2s ease-in-out;
    }
    
    /* Input Box Font Adjustment */
    .stTextInput>div>div>input {
        font-size: 32px !important;
        text-align: right !important;
        font-family: monospace !important;
        padding: 10px !important;
    }

    /* Sidebar Fix for neat navigation */
    [data-testid="stSidebarNav"] ul { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

st.title("🧮 Smart Calculator Suite")
st.caption("Welcome! Use the premium sidebar menu to switch between calculators.")
st.markdown("---")

st.subheader("🔢 Standard Calculator")

if 'expr' not in st.session_state:
    st.session_state.expr = ""

# Calculator Display Box
st.text_input("Display", value=st.session_state.expr, disabled=True, label_visibility="collapsed")

# Native Streamlit grid that remains horizontal even on tiny mobile screens
# Specifying widths avoids auto-stacking on phone viewports
row1 = st.columns([1, 1, 1, 1])
row2 = st.columns([1, 1, 1, 1])
row3 = st.columns([1, 1, 1, 1])
row4 = st.columns([1, 1, 1, 1])
row5 = st.columns([1]) # For Equals sign

with row1[0]:
    if st.button("7", key="btn7"): st.session_state.expr += "7"; st.rerun()
with row1[1]:
    if st.button("8", key="btn8"): st.session_state.expr += "8"; st.rerun()
with row1[2]:
    if st.button("9", key="btn9"): st.session_state.expr += "9"; st.rerun()
with row1[3]:
    if st.button("÷", key="btn_div"): st.session_state.expr += "/"; st.rerun()

with row2[0]:
    if st.button("4", key="btn4"): st.session_state.expr += "4"; st.rerun()
with row2[1]:
    if st.button("5", key="btn5"): st.session_state.expr += "5"; st.rerun()
with row2[2]:
    if st.button("6", key="btn6"): st.session_state.expr += "6"; st.rerun()
with row2[3]:
    if st.button("×", key="btn_mul"): st.session_state.expr += "*"; st.rerun()

with row3[0]:
    if st.button("1", key="btn1"): st.session_state.expr += "1"; st.rerun()
with row3[1]:
    if st.button("2", key="btn2"): st.session_state.expr += "2"; st.rerun()
with row3[2]:
    if st.button("3", key="btn3"): st.session_state.expr += "3"; st.rerun()
with row3[3]:
    if st.button("-", key="btn_sub"): st.session_state.expr += "-"; st.rerun()

with row4[0]:
    if st.button("C", key="btn_clear"): st.session_state.expr = ""; st.rerun()
with row4[1]:
    if st.button("0", key="btn0"): st.session_state.expr += "0"; st.rerun()
with row4[2]:
    if st.button(".", key="btn_dot"): st.session_state.expr += "."; st.rerun()
with row4[3]:
    if st.button("+", key="btn_add"): st.session_state.expr += "+"; st.rerun()

with row5[0]:
    if st.button("=", key="btn_equal"):
        if st.session_state.expr:
            try:
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except ZeroDivisionError:
                st.session_state.expr = "Cannot divide by 0"
            except Exception:
                st.session_state.expr = "Error"
        st.rerun()