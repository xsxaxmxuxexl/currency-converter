import streamlit as st

from currency_converter import CurrencyConverter

import pycountry




st.title("Currency Converter")


converter = CurrencyConverter()


currencies = converter.currencies



currency_to_country = {currency: pycountry.currencies.get(alpha_3 = currency).name for currency in currencies if pycountry.currencies.get(alpha_3=currency)}


amount = st.slider("Enter amount:",0,20000,5000)
from_currency = st.selectbox("From currency:",options = list(currency_to_country.keys()))
from_country = currency_to_country.get(from_currency,"Unknown")



st.write(f"From country:{from_country}")


to_currency = st.selectbox("To currency:",options = list(currency_to_country.keys()))


to_country = currency_to_country.get(to_currency,"Unknown")


st.write(f"To country:{to_country}")

converted_amount = converter.convert(amount,from_currency, to_currency)





if st.button("CurrencyConverter"):
	st.write(f"Converted amount:{converted_amount:.2f} {to_currency}")