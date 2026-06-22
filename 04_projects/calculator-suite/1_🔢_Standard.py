import streamlit as st

st.set_page_config(
    page_title="Zyan Studio | Calculator Suite",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Robust Multi-Device Layout Lock & Premium UI Engine
st.markdown("""
    <style>
    /* Force completely dark core background */
    [data-testid="stAppViewContainer"], .main {
        background-color: #0d0f14 !important;
    }
    
    /* 🚨 ABSOLUTE MOBILE GRID LOCK - Stops ALL vertical stacking on phones */
    div[data-testid="stHorizontalBlock"], 
    .stHorizontalBlock, 
    [data-testid="column"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
        width: 100% !important;
    }
    
    /* Ensure individual columns behave like standard grid cells */
    div[data-testid="stHorizontalBlock"] > div,
    .stHorizontalBlock > div {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    /* Calculator Premium Floating Container */
    .calc-card-wrapper {
        max-width: 360px;
        margin: 0 auto;
        padding: 18px;
        background: #151922;
        border-radius: 20px;
        border: 1px solid #222936;
        box-shadow: 0px 10px 35px rgba(0, 0, 0, 0.6);
    }
    
    /* High-Definition Input Screen Panel */
    .stTextInput>div>div>input {
        font-size: 38px !important;
        text-align: right !important;
        font-family: monospace !important;
        background-color: #090b0f !important;
        color: #ffffff !important;
        border: 1px solid #222936 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        letter-spacing: 1px;
    }

    /* Minimalist Button Matrix Logic */
    .stButton>button {
        width: 100% !important;
        height: 52px !important;
        border-radius: 12px !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        background-color: #1e2430 !important;
        color: #e2e8f0 !important;
        border: none !important;
        transition: all 0.1s ease-in-out !important;
    }

    /* Active Tap Feedback Interaction States */
    .stButton>button:hover {
        background-color: #293142 !important;
        color: #ffffff !important;
    }
    
    .stButton>button:active {
        transform: scale(0.96);
    }

    /* Modern Blue Accent for Core Operators */
    div.operator-btn button {
        background-color: #3b82f6 !important;
        color: #ffffff !important;
    }
    div.operator-btn button:hover { background-color: #2563eb !important; }

    /* Neutral Slate Accent for Utilities */
    div.utility-btn button {
        background-color: #2d3748 !important;
        color: #cbd5e1 !important;
    }
    div.utility-btn button:hover { background-color: #4a5568 !important; }
    
    /* Clean up default Streamlit headers padding */
    [data-testid="stHeader"] { background: transparent !important; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

# Render Outer Container Card
st.markdown('<div class="calc-card-wrapper">', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #ffffff; margin-bottom: 2px; font-family: sans-serif;'>Smart Calculator</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 12px; margin-bottom: 18px;'>Zyan Studio Premium Suite</p>", unsafe_allow_html=True)

if 'expr' not in st.session_state:
    st.session_state.expr = ""

# Output Window
st.text_input("Display", value=st.session_state.expr if st.session_state.expr else "0", disabled=True, label_visibility="collapsed")
st.write("") 

# Strict Row Grid Setup
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)

# ROW 1
with row1[0]:
    if st.button("7", key="n7"): st.session_state.expr += "7"; st.rerun()
with row1[1]:
    if st.button("8", key="n8"): st.session_state.expr += "8"; st.rerun()
with row1[2]:
    if st.button("9", key="n9"): st.session_state.expr += "9"; st.rerun()
with row1[3]:
    st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
    if st.button("÷", key="op_div"): st.session_state.expr += "/"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ROW 2
with row2[0]:
    if st.button("4", key="n4"): st.session_state.expr += "4"; st.rerun()
with row2[1]:
    if st.button("5", key="n5"): st.session_state.expr += "5"; st.rerun()
with row2[2]:
    if st.button("6", key="n6"): st.session_state.expr += "6"; st.rerun()
with row2[3]:
    st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
    if st.button("×", key="op_mul"): st.session_state.expr += "*"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ROW 3
with row3[0]:
    if st.button("1", key="n1"): st.session_state.expr += "1"; st.rerun()
with row3[1]:
    if st.button("2", key="n2"): st.session_state.expr += "2"; st.rerun()
with row3[2]:
    if st.button("3", key="n3"): st.session_state.expr += "3"; st.rerun()
with row3[3]:
    st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
    if st.button("-", key="op_sub"): st.session_state.expr += "-"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ROW 4 (Cleaned up Grid Structure without full-width blocks)
with row4[0]:
    st.markdown('<div class="utility-btn">', unsafe_allow_html=True)
    if st.button("C", key="ut_clr"): st.session_state.expr = ""; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with row4[1]:
    if st.button("0", key="n0"): st.session_state.expr += "0"; st.rerun()
with row4[2]:
    st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
    if st.button("=", key="op_eq"):
        if st.session_state.expr:
            try:
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except ZeroDivisionError:
                st.session_state.expr = "Cannot divide by 0"
            except Exception:
                st.session_state.expr = "Error"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with row4[3]:
    st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
    if st.button("+", key="op_add"): st.session_state.expr += "+"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)