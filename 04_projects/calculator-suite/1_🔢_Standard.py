import streamlit as st

# Page Config
st.set_page_config(
    page_title="Dev Hub | Calculator", 
    page_icon="🧮", 
    layout="centered",
    initial_sidebar_state="collapsed" 
)

# CSS Function
def apply_style():
    st.markdown("""
        <style>
        /* Container ko full width dene ke liye */
        .block-container { 
            max-width: 100% !important; 
            padding: 0.5rem !important; 
        }
        
        /* Input box ko force full width */
        .stTextInput {
            width: 100% !important;
        }
        
        .stTextInput > div > div > input {
            font-size: 24px !important;
            height: 60px !important;
            width: 100% !important;
        }

        /* Buttons ko screen mein fit karne ke liye */
        div.stButton > button {
            height: 50px !important;
            font-size: 18px !important;
            padding: 0 !important;
            width: 100% !important;
        }
        footer {visibility: hidden !important;}
        
        /* Agar tum apna khud ka branding footer dikhana chahte ho, 
           toh neeche uska style hoga */
        .footer { 
            text-align: center; 
            color: #888; 
            font-size: 12px; 
            margin-top: 20px; 
        }        
                
        
        /* Mobile par Manage App button ko hide ya adjust karna */
        #vg-button { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

apply_style()

# 3. Branding Header
st.title("🔢 Smart Calculator")
st.caption("Dev Hub | Ecosystem Mode")

# 4. App Logic
if "expr" not in st.session_state: st.session_state.expr = ""

user_typed = st.text_input("Input", value=st.session_state.expr, label_visibility="collapsed")
if user_typed != st.session_state.expr:
    st.session_state.expr = user_typed
    st.rerun()

# 5. Responsive Grid (Buttons)
buttons = [
    ["Clear", ".", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "="]
]

for row in buttons:
    # Column layout screen ke hisaab se adjust hoga
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn, use_container_width=True):
            if btn == "C": st.session_state.expr = ""
            elif btn == "=":
                try: st.session_state.expr = str(round(eval(st.session_state.expr), 4))
                except: st.session_state.expr = "Error"
            else: st.session_state.expr += btn
            st.rerun()

# 6. Professional Footer
st.markdown("""
    <div class="footer">
        Dev Hub Ecosystem | Professional Grade Tool
    </div>
""", unsafe_allow_html=True)