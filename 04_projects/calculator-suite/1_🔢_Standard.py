import streamlit as st

st.set_page_config(
    page_title="Zyan Studio | Calculator Suite",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 🚨 MASTER COMPONENT RESPONSIVE OVERRIDE
# Is CSS se Streamlit mobile par columns ko tod kar vertical line nahi bana payega
st.markdown("""
    <style>
    /* Dark Premium Canvas Setup */
    [data-testid="stAppViewContainer"], .main {
        background-color: #0b0d12 !important;
    }
    
    /* Strict Column Control for ALL viewports (Mobile Lock) */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
        width: 100% !important;
    }
    
    [data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    /* Calculator Main Premium Card Frame */
    .calc-box {
        max-width: 360px;
        margin: 0 auto;
        padding: 20px;
        background-color: #131722;
        border: 1px solid #1e2538;
        border-radius: 24px;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.6);
    }

    /* Sleek Display screen */
    .stTextInput>div>div>input {
        font-size: 38px !important;
        text-align: right !important;
        font-family: monospace !important;
        background-color: #07090d !important;
        color: #ffffff !important;
        border: 1px solid #1e2538 !important;
        border-radius: 14px !important;
        padding: 14px !important;
    }

    /* Premium Minimalist Keypad buttons */
    .stButton>button {
        width: 100% !important;
        height: 54px !important;
        border-radius: 14px !important;
        font-size: 22px !important;
        font-weight: 600 !important;
        background-color: #1c2130 !important;
        color: #f1f5f9 !important;
        border: none !important;
        transition: all 0.1s ease !important;
    }

    .stButton>button:hover {
        background-color: #262d42 !important;
        color: #ffffff !important;
    }

    .stButton>button:active {
        transform: scale(0.95);
    }

    /* Operator & Utility Styles */
    div.op-btn button { background-color: #2563eb !important; color: white !important; }
    div.op-btn button:hover { background-color: #1d4ed8 !important; }
    
    div.util-btn button { background-color: #334155 !important; color: #cbd5e1 !important; }
    div.util-btn button:hover { background-color: #475569 !important; }

    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding-top: 2rem !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu Info
st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

# Outer UI Wrapper Init
st.markdown('<div class="calc-box">', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffffff; margin-bottom: 2px;'>Smart Calculator</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 12px; margin-bottom: 18px;'>Zyan Studio Premium Suite</p>", unsafe_allow_html=True)

if 'expr' not in st.session_state:
    st.session_state.expr = ""

# Dynamic Input Box Screen
st.text_input("Display", value=st.session_state.expr if st.session_state.expr else "0", disabled=True, label_visibility="collapsed")
st.write("") 

# Strict Row Matrix Framework
r1 = st.columns(4)
r2 = st.columns(4)
r3 = st.columns(4)
r4 = st.columns(4)

# Row 1 Mapping
with r1[0]:
    st.markdown('<div class="util-btn">', unsafe_allow_html=True)
    if st.button("C", key="c1"): st.session_state.expr = ""; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with r1[1]:
    st.markdown('<div class="util-btn">', unsafe_allow_html=True)
    if st.button(".", key="d1"): st.session_state.expr += "."; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with r1[2]:
    st.markdown('<div class="util-btn">', unsafe_allow_html=True)
    if st.button("%", key="p1"): st.session_state.expr += "/100"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with r1[3]:
    st.markdown('<div class="op-btn">', unsafe_allow_html=True)
    if st.button("÷", key="o1"): st.session_state.expr += "/"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2 Mapping
with r2[0]:
    if st.button("7", key="b7"): st.session_state.expr += "7"; st.rerun()
with r2[1]:
    if st.button("8", key="b8"): st.session_state.expr += "8"; st.rerun()
with r2[2]:
    if st.button("9", key="b9"): st.session_state.expr += "9"; st.rerun()
with r2[3]:
    st.markdown('<div class="op-btn">', unsafe_allow_html=True)
    if st.button("×", key="o2"): st.session_state.expr += "*"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 3 Mapping
with r3[0]:
    if st.button("4", key="b4"): st.session_state.expr += "4"; st.rerun()
with r3[1]:
    if st.button("5", key="b5"): st.session_state.expr += "5"; st.rerun()
with r3[2]:
    if st.button("6", key="b6"): st.session_state.expr += "6"; st.rerun()
with r3[3]:
    st.markdown('<div class="op-btn">', unsafe_allow_html=True)
    if st.button("-", key="o3"): st.session_state.expr += "-"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 4 Mapping
with r4[0]:
    if st.button("1", key="b1"): st.session_state.expr += "1"; st.rerun()
with r4[1]:
    if st.button("2", key="b2"): st.session_state.expr += "2"; st.rerun()
with r4[2]:
    if st.button("3", key="b3"): st.session_state.expr += "3"; st.rerun()
with r4[3]:
    st.markdown('<div class="op-btn">', unsafe_allow_html=True)
    if st.button("+", key="o4"): st.session_state.expr += "+"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Final Execution Alignment Block (Row 5 - Bottom Extended Keys)
r5 = st.columns([2, 2])
with r5[0]:
    if st.button("0", key="b0"): st.session_state.expr += "0"; st.rerun()
with r5[1]:
    st.markdown('<div class="op-btn">', unsafe_allow_html=True)
    if st.button("=", key="o5"):
        if st.session_state.expr:
            try:
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except ZeroDivisionError:
                st.session_state.expr = "Cannot divide by 0"
            except Exception:
                st.session_state.expr = "Error"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)