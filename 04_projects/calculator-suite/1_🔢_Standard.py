import streamlit as st

st.title("🔢 Smart Calculator Suite")
st.write("Welcome! Use the menu to switch between calculators.")

# Display screen
if 'expression' not in st.session_state:
    st.session_state.expression = ""

st.text_input("Result", value=st.session_state.expression, disabled=True, key="screen")

# Calculator Grid Definitions
# Har row ke liye 4 equal-width columns banayein taaki mobile par layout break na ho
row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)

# Row 1 Buttons
with row1[0]:
    if st.button("7", use_container_width=True):
        st.session_state.expression += "7"
with row1[1]:
    if st.button("8", use_container_width=True):
        st.session_state.expression += "8"
with row1[2]:
    if st.button("9", use_container_width=True):
        st.session_state.expression += "9"
with row1[3]:
    if st.button("÷", use_container_width=True):
        st.session_state.expression += "/"

# Row 2 Buttons
with row2[0]:
    if st.button("4", use_container_width=True):
        st.session_state.expression += "4"
with row2[1]:
    if st.button("5", use_container_width=True):
        st.session_state.expression += "5"
with row2[2]:
    if st.button("6", use_container_width=True):
        st.session_state.expression += "6"
with row2[3]:
    if st.button("×", use_container_width=True):
        st.session_state.expression += "*"

# Row 3 Buttons
with row3[0]:
    if st.button("1", use_container_width=True):
        st.session_state.expression += "1"
with row3[1]:
    if st.button("2", use_container_width=True):
        st.session_state.expression += "2"
with row3[2]:
    if st.button("3", use_container_width=True):
        st.session_state.expression += "3"
with row3[3]:
    if st.button("−", use_container_width=True):
        st.session_state.expression += "-"

# Row 4 Buttons
with row4[0]:
    if st.button("C", use_container_width=True):
        st.session_state.expression = ""
with row4[1]:
    if st.button("0", use_container_width=True):
        st.session_state.expression += "0"
with row4[2]:
    if st.button(".", use_container_width=True):
        st.session_state.expression += "."
with row4[3]:
    if st.button("+", use_container_width=True):
        st.session_state.expression += "+"

# Equal Button
if st.button("=", use_container_width=True):
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"