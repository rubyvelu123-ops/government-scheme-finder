import streamlit as st

st.set_page_config(page_title="Government Scheme Finder", page_icon="🇮🇳")

st.title("🇮🇳 Government Scheme Finder")
st.write("Find government schemes based on your needs.")

category = st.selectbox(
    "Choose your category",
    ["Education", "Agriculture", "Business", "Housing"],
    key="category_select"

)

if st.button("Find Schemes",key="find_schemes_btn2"):
    if category == "Education":
        st.subheader("National Scholarship Portal")
        st.write("Students can search for eligible central and state scholarship schemes.")
        st.markdown("[Official Website](https://scholarships.gov.in/)")

    elif category == "Agriculture":
        st.subheader("PM-KISAN Samman Nidhi")
        st.write("Eligible farmer families may receive ₹6,000 per year in three instalments, subject to scheme rules.")
        st.markdown("[Official Website](https://pmkisan.gov.in/)")

    elif category == "Business":
        st.subheader("Pradhan Mantri MUDRA Yojana")
        st.write("Eligible small businesses can explore loans through participating lenders.")
        st.markdown("[Government Scheme Portal](https://www.myscheme.gov.in/)")

    elif category == "Housing":
        st.subheader("Pradhan Mantri Awas Yojana")
        st.write("Eligible families can check housing assistance under current scheme guidelines.")
        st.markdown("[Official Website](https://pmay-urban.gov.in/)")

st.caption("Please check official websites for current eligibility and application details.")

st.set_page_config(page_title="Government Scheme Finder", page_icon="🇮🇳")







    
    