import streamlit as st

st.set_page_config(
    page_title="Dev Hub | Calculator Suite",
    page_icon="🧮",
    layout="centered"
)

st.title("🔢 Smart Calculator Suite")
st.write("Created by Dev Hub")

# Session state initialization
if 'expr' not in st.session_state:
    st.session_state.expr = ""

# Clean display input
st.text_input("Result", value=st.session_state.expr if st.session_state.expr else "0", disabled=True)

# Grid formation using native responsive structures
r1 = st.columns(4)
r2 = st.columns(4)
r3 = st.columns(4)
r4 = st.columns(4)

# Row 1
with r1[0]:
    if st.button("C", use_container_width=True):
        st.session_state.expr = ""
        st.rerun()
with r1[1]:
    if st.button(".", use_container_width=True):
        st.session_state.expr += "."
        st.rerun()
with r1[2]:
    if st.button("%", use_container_width=True):
        st.session_state.expr += "/100"
        st.rerun()
with r1[3]:
    if st.button("÷", use_container_width=True):
        st.session_state.expr += "/"
        st.rerun()

# Row 2
with r2[0]:
    if st.button("7", use_container_width=True):
        st.session_state.expr += "7"
        st.rerun()
with r2[1]:
    if st.button("8", use_container_width=True):
        st.session_state.expr += "8"
        st.rerun()
with r2[2]:
    if st.button("9", use_container_width=True):
        st.session_state.expr += "9"
        st.rerun()
with r2[3]:
    if st.button("×", use_container_width=True):
        st.session_state.expr += "*"
        st.rerun()

# Row 3
with r3[0]:
    if st.button("4", use_container_width=True):
        st.session_state.expr += "4"
        st.rerun()
with r3[1]:
    if st.button("5", use_container_width=True):
        st.session_state.expr += "5"
        st.rerun()
with r3[2]:
    if st.button("6", use_container_width=True):
        st.session_state.expr += "6"
        st.rerun()
with r3[3]:
    if st.button("-", use_container_width=True):
        st.session_state.expr += "-"
        st.rerun()

# Row 4
with r4[0]:
    if st.button("1", use_container_width=True):
        st.session_state.expr += "1"
        st.rerun()
with r4[1]:
    if st.button("2", use_container_width=True):
        st.session_state.expr += "2"
        st.rerun()
with r4[2]:
    if st.button("3", use_container_width=True):
        st.session_state.expr += "3"
        st.rerun()
with r4[3]:
    if st.button("+", use_container_width=True):
        st.session_state.expr += "+"
        st.rerun()

# Bottom Row for 0 and =
r5 = st.columns([2, 2])
with r5[0]:
    if st.button("0", use_container_width=True):
        st.session_state.expr += "0"
        st.rerun()
with r5[1]:
    if st.button("=", use_container_width=True):
        if st.session_state.expr:
            try:
                st.session_state.expr = str(round(eval(st.session_state.expr), 4))
            except Exception:
                st.session_state.expr = "Error"
        st.rerun()