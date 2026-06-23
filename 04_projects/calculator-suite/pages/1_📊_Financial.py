import streamlit as st
from modules.finance_logic import calculate_emi  # YE IMPORT ZAROORI HAI

# Page Config sirf main file mein hona chahiye, yahan se hata do
st.title("📊 Financial Calculator")
st.markdown("---")

tab1, tab2 = st.tabs(["💰 Loan EMI Calculator", "📈 Compound Interest"])

with tab1:
    st.subheader("Calculate Monthly Loan EMI")
    # Text input for flexibility
    p_input = st.text_input("Principal Amount ($)", value="50000")
    tenure_years = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=5)
    interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.5, max_value=25.0, value=7.5, step=0.1)

    if st.button("Calculate EMI", key="emi_btn"):
        try:
            # Type conversion zaroori hai
            p_val = float(p_input)
            
            # Function call (Logic yahan se trigger hoga)
            emi, total_payment, total_interest = calculate_emi(p_val, tenure_years, interest_rate)
            
            st.success(f"Monthly EMI: **${emi:,.2f}**")
            c1, c2 = st.columns(2)
            c1.metric("Total Interest", f"${total_interest:,.2f}")
            c2.metric("Total Payable Amount", f"${total_payment:,.2f}")
        except ValueError:
            st.error("Please enter a valid Principal Amount")

with tab2:
    st.subheader("Compound Interest Calculator")
    p_ci = st.number_input("Initial Investment ($/Rs)", min_value=100, value=10000, step=500)
    rate_ci = st.number_input("Annual Interest Rate (CI %)", min_value=0.1, max_value=50.0, value=8.0, step=0.5)
    time_ci = st.slider("Time Period (Years)", min_value=1, max_value=40, value=10)
    
    future_value = p_ci * ((1 + (rate_ci / 100)) ** time_ci)
    net_interest = future_value - p_ci
    
    st.info(f"Future Wealth Value: **${future_value:,.2f}**")
    st.metric("Total Interest Earned", f"${net_interest:,.2f}")