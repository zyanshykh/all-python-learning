def inject_style():
    st.markdown("""
        <style>
        /* Mobile-First Optimization */
        .block-container { max-width: 450px !important; padding: 1rem !important; }
        
        /* Consistent Header */
        h1 { color: #f0f2f6; font-size: 1.8rem !important; }
        
        /* Button Styling */
        div.stButton > button {
            border-radius: 8px !important;
            border: 1px solid #333 !important;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

  