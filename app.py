import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import streamlit as st

st.set_page_config(page_title="Phone Details App", page_icon="📞")

st.markdown(
    '''
    <style>
    body {
        background-color: #f0f0f0;  
        font-family: 'Arial';  
    }
    .stApp {
        max-width: 1000px; 
        margin: 0 auto;
    }
    .st-selectbox, .st-text_input {
        background-color: #ffffff; 
        border: 1px solid #cccccc;  
        border-radius: 4px;  
    }
    </style>
    ''',
    unsafe_allow_html=True
)

st.title("Phone Number Details")

country_phone_codes = {
    "India": "+91",
    "United Kingdom": "+44",
    "Australia": "+61",
    "Canada": "+1",
    "United States": "+1",
    "Germany": "+49",
    "France": "+33",
    "Brazil": "+55",
    "China": "+86",
    "Japan": "+81"
}

country_options = list(country_phone_codes.keys())
selected_country = st.selectbox("Select a country", country_options)

if selected_country == "India":
    phone_number = st.text_input("Enter your phone number:", placeholder='9876543210')
    generate_button = st.button("Generate Details")

    if generate_button:
        if phone_number:
            try:
                phone_code = country_phone_codes[selected_country]
                full_phone_number = f"{phone_code} {phone_number}"
                st.write("**Phone number:**", full_phone_number)

                parsed_phone = phonenumbers.parse(full_phone_number)

                if not phonenumbers.is_valid_number(parsed_phone):
                    st.write("**Invalid phone number**")
                else:
                    time_zones = timezone.time_zones_for_number(parsed_phone)
                    cleaned_time_zone = time_zones[0].replace('(', '').replace(')', '').replace("'", '')
                    carr = carrier.name_for_number(parsed_phone, 'en')
                    reg = geocoder.description_for_number(parsed_phone, 'en')

                    st.write('**Time Zone:**', cleaned_time_zone)
                    st.write('**Carrier:**', carr)
                    st.write('**Region:**', reg)

            except phonenumbers.NumberParseException:
                st.write("Error parsing phone number. Please enter a valid number.")
else:
    st.write("Please select 'India' from the dropdown to enter a phone number.")

st.markdown("---")
st.write("Created with ❤️ by Sujal Suthar")
