import streamlit as st

st.set_page_config(
    page_title="Zyan Studio | Calculator Suite",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Enterprise Grade Mobile-First Lock & Premium Minimalistic UI/UX
st.markdown("""
    <style>
    /* Absolute Layout Core Overwrite */
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117 !important;
    }
    
    /* Grid Engine Core: Mobile and Laptop behavior uniform lock */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
        width: 100% !important;
    }
    
    div[data-testid="stHorizontalBlock"] > div {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }
    
    /* Main App Card Container */
    .main-calc-body {
        max-width: 380px;
        margin: 20px auto;
        padding: 24px;
        background: #161a24;
        border-radius: 24px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.4);
        border: 1px solid #262c3a;
    }
    
    /* Input Display Panel */
    .stTextInput>div>div>input {
        font-size: 36px !important;
        text-align: right !important;
        font-family: 'Courier New', monospace !important;
        background-color: #0a0d14 !important;
        color: #00ff66 !important; /* Premium Retro Digital Green Glow */
        border: 2px solid #22293a !important;
        border-radius: 16px !important;
        padding: 15px !important;
        letter-spacing: 1px;
    }
    
    /* Modern Premium Button Architecture */
    .stButton>button {
        width: 100% !important;
        height: 55px !important;
        border-radius: 14px !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        background: #22293a !important;
        color: #ffffff !important;
        border: none !important;
        transition: all 0.15s ease-in-out !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    
    /* Hover & Active Feedback Interaction States */
    .stButton>button:hover {
        background: #2d364f !important;
        border-color: transparent !important;
        transform: translateY(-2px);
    }
    
    .stButton>button:active {
        transform: translateY(1px);
        background: #1b202e !important;
    }
    
    /* Stylized Operation Operators for distinct contrast UX */
    div.row-op button {
        background: #ff9f0a !important; /* iOS inspired Accent Colors */
        color: white !important;
    }
    div.row-op button:hover { background: #cc7f08 !important; }
    
    div.row-util button {
        background: #a5a5a5 !important;
        color: black !important;
    }
    div.row-util button:hover { background: #8e8e8e !important; }
    
    /* Clean Sidebar Nav elements spacing */
    [data-testid="stSidebarNav"] { background-color: #11151f !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Design
st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

# Main Container Wrapper
st.markdown('<div class="main-calc-body">', unsafe_allow_html=True)

st.title("🧮 Smart Calculator")
st.caption("Engineered by Zyan Studio")
st.markdown("---")

if 'expr' not in st.session_state:
    st.session_state.expr = ""

# Display Output screen
st.text_input("Display", value=st.session_state.expr, disabled=True, label_visibility="collapsed")
st.write("") # Padding spacing

# Layout Grid Matrix Setup
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)
row5 = st.columns(1) # Extended Equals execution block

# Row 1 Allocation
with row1[0]:
    if st.button("7", key="n7"): st.session_state.expr += "7"; st.rerun()
with row1[1]:
    if st.button("8", key="n8"): st.session_state.expr += "8"; st.rerun()
with row1[2]:
    if st.button("9", key="n9"): st.session_state.expr += "9"; st.rerun()
with row1[3]:
    st.markdown('<div class="row-op">', unsafe_allow_html=True)
    if st.button("÷", key="op_div"): st.session_state.expr += "/"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 2 Allocation
with row2[0]:
    if st.button("4", key="n4"): st.session_state.expr += "4"; st.rerun()
with row2[1]:
    if st.button("5", key="n5"): st.session_state.expr += "5"; st.rerun()
with row2[2]:
    if st.button("6", key="n6"): st.session_state.expr += "6"; st.rerun()
with row2[3]:
    st.markdown('<div class="row-op">', unsafe_allow_html=True)
    if st.button("×", key="op_mul"): st.session_state.expr += "*"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 3 Allocation
with row3[0]:
    if st.button("1", key="n1"): st.session_state.expr += "1"; st.rerun()
with row3[1]:
    if st.button("2", key="n2"): st.session_state.expr += "2"; st.rerun()
with row3[2]:
    if st.button("3", key="n3"): st.session_state.expr += "3"; st.rerun()
with row3[3]:
    st.markdown('<div class="row-op">', unsafe_allow_html=True)
    if st.button("-", key="op_sub"): st.session_state.expr += "-"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 4 Allocation
with row4[0]:
    st.markdown('<div class="row-util">', unsafe_allow_html=True)
    if st.button("C", key="ut_clr"): st.session_state.expr = ""; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with row4[1]:
    if st.button("0", key="n0"): st.session_state.expr += "0"; st.rerun()
with row4[2]:
    if st.button(".", key="ut_dot"): st.session_state.expr += "."; st.rerun()
with row4[3]:
    st.markdown('<div class="row-op">', unsafe_allow_html=True)
    if st.button("+", key="op_add"): st.session_state.expr += "+"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 5 Allocation
with row5[0]:
    st.markdown('<div class="row-op">', unsafe_allow_html=True)
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

st.markdown('</div>', unsafe_allow_html=True) # End Wrap