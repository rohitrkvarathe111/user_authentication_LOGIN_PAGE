'''

import streamlit as st

def login(username, password):
    if len(username) < 6 or len(username) > 12:
        return False
    if not username.isalnum():
        return False
    if len(password) < 6:
        return False
    return True

def main():
    st.title("Login App")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success("You have successfully logged in!")
        else:
            st.error("Login failed. Please enter the correct username and password"
                     "a. username to be alphanumeric"
                     "b. username to be between 6-12 letters"
                     "c. password to allow alphabet, numbers, special characters"
                     "d. minimum password length is 6 ")

if __name__ == "__main__":
    main()
'''


