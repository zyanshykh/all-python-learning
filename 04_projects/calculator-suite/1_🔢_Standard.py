import streamlit as st

st.set_page_config(
    page_title="Dev Hub | Calculator Suite",
    page_icon="🧮",
    layout="centered"
)

# Premium Dev Hub Layout Styling Injection
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"], .main {
        background-color: #0b0d12 !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    .block-container { max-width: 420px !important; padding-top: 2rem !important; }
    
    /* Input field styling for a premium glassmorphism touch */
    .stTextInput>div>div>input {
        font-size: 32px !important;
        text-align: right !important;
        font-family: monospace !important;
        background-color: #07090d !important;
        color: #ffffff !important;
        border: 1px solid #1e2538 !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Branding Headers
st.title("🔢 Smart Calculator Suite")
st.caption("Created by Dev Hub | Ecosystem Sync Mode")

# Initialize central session state safely
if "expr" not in st.session_state:
    st.session_state.expr = ""

# --- LIVE ECOSYSTEM INTERACTION ENGINE ---
# Input active rakha hai taake mobile me keyboard pop-up ho aur backspace kaam kare
user_typed = st.text_input(
    label="Calculator Input Screen",
    value=st.session_state.expr,
    placeholder="0",
    label_visibility="collapsed",
    key="calc_screen"
)

# Agar user physical keyboard/mobile input se value change kare toh state sync karein
if user_typed != st.session_state.expr:
    st.session_state.expr = user_typed
    st.rerun()

# --- RESPONSIVE GRID GRID MATRIX ---
r1 = st.columns(4)
r2 = st.columns(4)
r3 = st.columns(4)
r4 = st.columns(4)

# Row 1 Keypad Mapping
with r1[0]:
    if st.button("C", use_container_width=True, key="btn_c"):
        st.session_state.expr = ""
        st.rerun()
with r1[1]:
    if st.button(".", use_container_width=True, key="btn_dot"):
        st.session_state.expr += "."
        st.rerun()
with r1[2]:
    if st.button("%", use_container_width=True, key="btn_mod"):
        st.session_state.expr += "/100"
        st.rerun()
with r1[3]:
    if st.button("÷", use_container_width=True, key="btn_div"):
        st.session_state.expr += "/"
        st.rerun()

# Row 2 Keypad Mapping
with r2[0]:
    if st.button("7", use_container_width=True, key="btn_7"):
        st.session_state.expr += "7"
        st.rerun()
with r2[1]:
    if st.button("8", use_container_width=True, key="btn_8"):
        st.session_state.expr += "8"
        st.rerun()
with r2[2]:
    if st.button("9", use_container_width=True, key="btn_9"):
        st.session_state.expr += "9"
        st.rerun()
with r2[3]:
    if st.button("×", use_container_width=True, key="btn_mul"):
        st.session_state.expr += "*"
        st.rerun()

# Row 3 Keypad Mapping
with r3[0]:
    if st.button("4", use_container_width=True, key="btn_4"):
        st.session_state.expr += "4"
        st.rerun()
with r3[1]:
    if st.button("5", use_container_width=True, key="btn_5"):
        st.session_state.expr += "5"
        st.rerun()
with r3[2]:
    if st.button("6", use_container_width=True, key="btn_6"):
        st.session_state.expr += "6"
        st.rerun()
with r3[3]:
    if st.button("-", use_container_width=True, key="btn_sub"):
        st.session_state.expr += "-"
        st.rerun()

# Row 4 Keypad Mapping
with r4[0]:
    if st.button("1", use_container_width=True, key="btn_1"):
        st.session_state.expr += "1"
        st.rerun()
with r4[1]:
    if st.button("2", use_container_width=True, key="btn_2"):
        st.session_state.expr += "2"
        st.rerun()
with r4[2]:
    if st.button("3", use_container_width=True, key="btn_3"):
        st.session_state.expr += "3"
        st.rerun()
with r4[3]:
    if st.button("+", use_container_width=True, key="btn_add"):
        st.session_state.expr += "+"
        st.rerun()

# Bottom Control Alignment (0 and Execution)
r5 = st.columns([2, 2])
with r5[0]:
    if st.button("0", use_container_width=True, key="btn_0"):
        st.session_state.expr += "0"
        st.rerun()
with r5[1]:
    if st.button("=", use_container_width=True, key="btn_eq"):
        if st.session_state.expr:
            try:
                # Execution parsing via safe evaluation
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except Exception:
                st.session_state.expr = "Error"
        st.rerun()