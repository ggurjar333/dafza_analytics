# -- USER AUTHENTICATION ---
names = ['Gaurav Gurjar', 'John Smith']
usernames = ['ggurjar', 'jsmith']

# # Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "dafza_dashboard", "abcdef", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    

    # --- SIDEBAR ---
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")

