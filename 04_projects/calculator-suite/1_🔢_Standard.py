import streamlit as st

st.set_page_config(
    page_title="Dev Hub | Calculator Suite",
    page_icon="🧮",
    layout="centered"
)

# Premium Modern Branding Header
st.title("🔢 Smart Calculator Suite")
st.caption("Created by Dev Hub | Ecosystem Sync Mode")

# Initialize session state for expression
if "expr" not in st.session_state:
    st.session_state.expr = ""

# --- ECOSYSTEM KEYBOARD & TOUCH SYNC INTERACTION ---
# input screen active rakhi hai taaki phone me touch karne se keyboard khule aur backspace/numbers chaley
user_input = st.text_input(
    label="Calculator Screen",
    value=st.session_state.expr,
    placeholder="0",
    label_visibility="collapsed",
    key="calc_screen"
)

# Agar user laptop keyboard ya mobile numerical pad se direct type kare, toh state sync ho jaye
if user_input != st.session_state.expr:
    st.session_state.expr = user_input
    st.rerun()


# --- STANDARD UI MATRIX GRID ---
r1 = st.columns(4)
r2 = st.columns(4)
r3 = st.columns(4)
r4 = st.columns(4)

# Row 1: Clear, Decimal, Percentage, Division
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

# Row 2: 7, 8, 9, Multiplication
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

# Row 3: 4, 5, 6, Subtraction
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

# Row 4: 1, 2, 3, Addition
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

# Bottom Row: 0 and Execution Evaluation
r5 = st.columns([2, 2])
with r5[0]:
    if st.button("0", use_container_width=True, key="btn_0"):
        st.session_state.expr += "0"
        st.rerun()
with r5[1]:
    if st.button("=", use_container_width=True, key="btn_eq"):
        if st.session_state.expr:
            try:
                # Direct Safe Mathematical Parsing
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except Exception:
                st.session_state.expr = "Error"
        st.rerun()git add .