import streamlit as st

st.set_page_config(
    page_title="Zyan Studio | Calculator Suite",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Premium Custom CSS for Locked Grid and Premium Dark Vibe
st.markdown("""
    <style>
    /* Main Layout Viewport Constraint */
    div[data-testid="stAppViewContainer"] {
        background-color: #0d0f14 !important;
    }
    
    /* Strict Horizontal Flex Force-Lock to Stop Vertical Collapsing */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 10px !important;
        width: 100% !important;
    }
    
    div[data-testid="stHorizontalBlock"] > div {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    /* Calculator Glassmorphism Container Card */
    .calc-card-wrapper {
        max-width: 360px;
        margin: 0 auto;
        padding: 20px;
        background: #151922;
        border-radius: 20px;
        border: 1px solid #222936;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    /* Sleek Numeric Display Screen */
    .stTextInput>div>div>input {
        font-size: 36px !important;
        text-align: right !important;
        font-family: 'SF Pro Display', -apple-system, monospace !important;
        background-color: #090b0f !important;
        color: #ffffff !important;
        border: 1px solid #222936 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        letter-spacing: 1px;
    }

    /* Pro-Grade Minimalist Button Matrix */
    .stButton>button {
        width: 100% !important;
        height: 52px !important;
        border-radius: 12px !important;
        font-size: 20px !important;
        font-weight: 500 !important;
        background-color: #1e2430 !important;
        color: #e2e8f0 !important;
        border: 1px solid transparent !important;
        transition: all 0.15s ease-in-out !important;
    }

    /* Interactive States Feedback UI */
    .stButton>button:hover {
        background-color: #293142 !important;
        border-color: #3b475e !important;
        color: #ffffff !important;
    }
    
    .stButton>button:active {
        background-color: #161b24 !important;
    }

    /* Distinct Contextual Accent Blocks (Operators) */
    div.operator-btn button {
        background-color: #3b82f6 !important; /* Premium Modern Blue Accent */
        color: #ffffff !important;
    }
    div.operator-btn button:hover {
        background-color: #2563eb !important;
    }

    /* Distinct Contextual Utility Blocks (Clear / Dot) */
    div.utility-btn button {
        background-color: #2d3748 !important;
        color: #cbd5e1 !important;
    }
    div.utility-btn button:hover {
        background-color: #4a5568 !important;
    }
    
    /* Hide Default Top Spacing Streamlit Headers */
    [data-testid="stHeader"] { background: transparent !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu Identity
st.sidebar.markdown("# ⚙️ Main Menu")
st.sidebar.markdown("---")

# Outer Structural Card Initialization
st.markdown('<div class="calc-card-wrapper">', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #ffffff; margin-bottom: 5px;'>Smart Calculator</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 13px; margin-bottom: 20px;'>Zyan Studio Premium Suite</p>", unsafe_allow_html=True)

if 'expr' not in st.session_state:
    st.session_state.expr = ""

# Output Workspace Window
st.text_input("Display", value=st.session_state.expr if st.session_state.expr else "0", disabled=True, label_visibility="collapsed")
st.write("") # Separation Spacer

# Grid Matrix Allocations
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)
row5 = st.columns(1)

# Row 1 Blocks
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

# Row 2 Blocks
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

# Row 3 Blocks
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

# Row 4 Blocks
with row4[0]:
    st.markdown('<div class="utility-btn">', unsafe_allow_html=True)
    if st.button("C", key="ut_clr"): st.session_state.expr = ""; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with row4[1]:
    if st.button("0", key="n0"): st.session_state.expr += "0"; st.rerun()
with row4[2]:
    st.markdown('<div class="utility-btn">', unsafe_allow_html=True)
    if st.button(".", key="ut_dot"): st.session_state.expr += "."; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with row4[3]:
    st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
    if st.button("+", key="op_add"): st.session_state.expr += "+"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Row 5 Block (Equals Evaluation Control)
with row5[0]:
    st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
    if st.button("=", key="op_eq"):
        if st.session_state.expr:
            try:
                # Direct safe mathematical string execution evaluation
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except ZeroDivisionError:
                st.session_state.expr = "Cannot divide by 0"
            except Exception:
                st.session_state.expr = "Error"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Structural Close Wrapper