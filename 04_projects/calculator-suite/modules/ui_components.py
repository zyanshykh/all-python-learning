import streamlit as st

def add_footer():
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: transparent;
            color: #888;
            font-size: 12px;
        }
        </style>
        <div class="footer">
            <hr>
            Dev Hub Ecosystem | © 2026 Analytics
        </div>
                
    """, unsafe_allow_html=True)

@st.cache_resource # Yeh line UI components ko memory mein store rakhegi
def add_footer():
    st.markdown("""...""", unsafe_allow_html=True)