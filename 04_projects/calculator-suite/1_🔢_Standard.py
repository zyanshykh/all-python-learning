import streamlit as st
from modules.ui_components import add_footer

# Page Config
st.set_page_config(page_title="Dev Hub | Calculator", page_icon="🧮", layout="centered", initial_sidebar_state="collapsed")

def apply_style():
    st.markdown("""
        <style>
        /* Mobile aur Desktop ke liye force full width */
        .block-container { max-width: 500px !important; padding: 1rem !important; }
        
        /* Buttons ka size fix karo */
        div.stButton > button {
            width: 100% !important; 
            height: 50px !important;
            margin: 2px !important;
        }
        
        /* Input Box ka style */
        .stTextInput > div > div > input {
            text-align: right !important;
            font-size: 24px !important;
        }
        </style>
    """, unsafe_allow_html=True)

st.title("🔢 Standard Calculator")

# 1. Session State mein history initialize karo (Upar kahi rakho)
if "history" not in st.session_state:
    st.session_state.history = []

# 2. Jab Calculation ho jaye (Inside your "=" button logic)
if st.button("Enter"):
    try:
        result = str(round(eval(st.session_state.expr), 4))
        # History mein add karo
        entry = f"{st.session_state.expr} = {result}"
        st.session_state.history.append(entry)
        st.session_state.expr = result
    except:
        st.session_state.expr = "Error"

# 3. History UI Display (Sidebar ya niche show karo)
if st.sidebar.button("Clear History"):
    st.session_state.history = []

st.sidebar.subheader("History")
for item in reversed(st.session_state.history): # Latest history upar dikhe
    st.sidebar.text(item)

# 2. State Initialization
if "expr" not in st.session_state: st.session_state.expr = ""

# 3. UI Display (Using Text Input like other pages)

user_typed = st.text_input("Input", value=st.session_state.expr, placeholder="0", label_visibility="collapsed",key="calc_input")

# 4. Modern Button Grid
btn_rows = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""] # Empty cell for grid balance
]

for row in btn_rows:
    cols = st.columns(4)
    for i, label in enumerate(row):
        if label and cols[i].button(label, use_container_width=True):
            if label == "C": st.session_state.expr = ""
            elif label == "=":
                try: st.session_state.expr = str(eval(st.session_state.expr))
                except: st.session_state.expr = "Error"
            else: st.session_state.expr += label
            st.rerun()

# 5. Add Footer (Modular)
add_footer()