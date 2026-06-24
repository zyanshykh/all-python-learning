import streamlit as st
from modules.ui_components import add_footer

# 1. Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered", initial_sidebar_state="collapsed")

# 2. Styling
st.markdown("""
    <style>
    .block-container { max-width: 500px !important; padding: 1rem !important; }
    div.stButton > button { width: 100% !important; height: 50px !important; margin: 2px !important; }
    .stTextInput > div > div > input { text-align: right !important; font-size: 24px !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🔢 Standard Calculator")

# 3. State Management
if "expr" not in st.session_state: st.session_state.expr = ""
if "history" not in st.session_state: st.session_state.history = []

# 4. Input Display
# Hum key "calc_input" use kar rahe hain taake input box state se synced rahe
user_input = st.text_input("Input", value=st.session_state.expr, label_visibility="collapsed", key="calc_input")

# Update logic: Agar user manual type kare toh bhi update ho
if user_input != st.session_state.expr:
    st.session_state.expr = user_input

# 5. Grid Logic (The core functional part)
btn_rows = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Grid generate karo
for row in btn_rows:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        if cols[i].button(label, use_container_width=True):
            if label == "C":
                st.session_state.expr = ""
            elif label == "=":
                try:
                    # eval() chalao aur history mein add karo
                    result = str(eval(st.session_state.expr))
                    st.session_state.history.append(f"{st.session_state.expr} = {result}")
                    st.session_state.expr = result
                except:
                    st.session_state.expr = "Error"
            else:
                # Value add karo
                st.session_state.expr += label
            
            # Logic khatam hote hi rerun, taake screen update ho
            st.rerun()

# 6. History Sidebar
if st.sidebar.button("Clear History"):
    st.session_state.history = []
    st.rerun()

st.sidebar.subheader("History")
for item in reversed(st.session_state.history):
    st.sidebar.text(item)

# 7. Footer
add_footer()