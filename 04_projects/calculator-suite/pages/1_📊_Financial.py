import streamlit as st
from modules.finance_logic import calculate_emi, calculate_ci 

st.title("📊 Financial Calculator")
st.markdown("---")

tab1, tab2 = st.tabs(["💰 Loan EMI Calculator", "📈 Compound Interest"])

with tab1:
    st.subheader("Calculate Monthly Loan EMI")
    p_input = st.text_input("Principal Amount ($)", value="50000")
    tenure_years = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=5)
    interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.5, max_value=25.0, value=7.5, step=0.1)

    if st.button("Calculate EMI"):
        try:
            emi, total_payment, total_interest = calculate_emi(float(p_input), tenure_years, interest_rate)
            st.success(f"Monthly EMI: **${emi:,.2f}**")
            c1, c2 = st.columns(2)
            c1.metric("Total Interest", f"${total_interest:,.2f}")
            c2.metric("Total Payable Amount", f"${total_payment:,.2f}")
        except ValueError:
            st.error("Invalid Input")

with tab2:
    st.subheader("Compound Interest Calculator")
    # Text input for CI to keep it consistent
    p_ci = st.text_input("Initial Investment ($)", value="10000")
    rate_ci = st.number_input("Annual Interest Rate (CI %)", min_value=0.1, max_value=50.0, value=8.0, step=0.5)
    time_ci = st.slider("Time Period (Years)", min_value=1, max_value=40, value=10)
    
    if st.button("Calculate CI"):
        try:
            fv, interest = calculate_ci(float(p_ci), rate_ci, time_ci) # Module se logic call kiya
            st.info(f"Future Wealth Value: **${fv:,.2f}**")
            st.metric("Total Interest Earned", f"${interest:,.2f}")
        except ValueError:
            st.error("Invalid Input")