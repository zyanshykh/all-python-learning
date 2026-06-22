import streamlit as st

st.set_page_config(
    page_title="Dev Hub | Calculator Suite",
    page_icon="🧮",
    layout="centered"
)

# Premium Dev Hub Minimal Branding Header
st.title("🔢 Smart Calculator Suite")
st.caption("Created by Dev Hub | Modern System")

# Session state crash protection handler
if "expr" not in st.session_state:
    st.session_state.expr = ""

# Display Screen - ReadOnly Native Block
st.text_input(
    label="Calculator Screen",
    value=st.session_state.expr if st.session_state.expr else "0",
    disabled=True,
    label_visibility="collapsed"
)

# Standard Matrix Grid Definition
r1 = st.columns(4)
r2 = st.columns(4)
r3 = st.columns(4)
r4 = st.columns(4)

# Row 1 Core Interactions
with r1[0]:
    if st.button("C", use_container_width=True, key="btn_c"):
        st.session_state.expr = ""
with r1[1]:
    if st.button(".", use_container_width=True, key="btn_dot"):
        st.session_state.expr += "."
with r1[2]:
    if st.button("%", use_container_width=True, key="btn_mod"):
        st.session_state.expr += "/100"
with r1[3]:
    if st.button("÷", use_container_width=True, key="btn_div"):
        st.session_state.expr += "/"

# Row 2 Core Interactions
with r2[0]:
    if st.button("7", use_container_width=True, key="btn_7"):
        st.session_state.expr += "7"
with r2[1]:
    if st.button("8", use_container_width=True, key="btn_8"):
        st.session_state.expr += "8"
with r2[2]:
    if st.button("9", use_container_width=True, key="btn_9"):
        st.session_state.expr += "9"
with r2[3]:
    if st.button("×", use_container_width=True, key="btn_mul"):
        st.session_state.expr += "*"

# Row 3 Core Interactions
with r3[0]:
    if st.button("4", use_container_width=True, key="btn_4"):
        st.session_state.expr += "4"
with r3[1]:
    if st.button("5", use_container_width=True, key="btn_5"):
        st.session_state.expr += "5"
with r3[2]:
    if st.button("6", use_container_width=True, key="btn_6"):
        st.session_state.expr += "6"
with r3[3]:
    if st.button("-", use_container_width=True, key="btn_sub"):
        st.session_state.expr += "-"

# Row 4 Core Interactions
with r4[0]:
    if st.button("1", use_container_width=True, key="btn_1"):
        st.session_state.expr += "1"
with r4[1]:
    if st.button("2", use_container_width=True, key="btn_2"):
        st.session_state.expr += "2"
with r4[2]:
    if st.button("3", use_container_width=True, key="btn_3"):
        st.session_state.expr += "3"
with r4[3]:
    if st.button("+", use_container_width=True, key="btn_add"):
        st.session_state.expr += "+"

# Bottom Custom Execution Block
r5 = st.columns([2, 2])
with r5[0]:
    if st.button("0", use_container_width=True, key="btn_0"):
        st.session_state.expr += "0"
with r5[1]:
    if st.button("=", use_container_width=True, key="btn_eq"):
        if st.session_state.expr:
            try:
                # Direct Safe Mathematical Parsing Evaluation
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except Exception:
                st.session_state.expr = "Error"