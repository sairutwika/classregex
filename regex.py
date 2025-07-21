import streamlit as st
import re
import pandas as pd

# ------------------ Page Setup ------------------
st.set_page_config(page_title="User Info Form", layout="centered")

# ------------------ Styling ------------------
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://png.pngtree.com/background/20230525/original/pngtree-female-developer-working-at-a-table-at-night-picture-image_2734060.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }

    .custom-heading {
        background: linear-gradient(90deg, #007BFF, #00C9A7);
        color: white;
        text-align: center;
        padding: 1rem 2rem;
        border-radius: 15px;
        font-size: 2.5rem;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin: 2rem auto 1rem auto;
        max-width: 800px;
    }

    label, .stMarkdown p, .stTextInput label, .stDateInput label {
        color: white !important;
    }

    .submitted-box {
        background-color: rgba(255, 255, 255, 0.2);
        border-left: 6px solid #2E8B57;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1.5rem;
        color: white;
    }

    .stTextInput>div>div>input,
    .stDateInput>div>div>input {
        background-color: #f0f4f8;
        color: black;
        padding: 0.5rem;
        border-radius: 8px;
    }

    .stDownloadButton button {
        color: black;
        font-weight: bold;
    }

    .stAlert {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Heading ------------------
st.markdown("<div class='custom-heading'>🌟 User Information Form</div>", unsafe_allow_html=True)
st.markdown("Please enter your details below and click **Submit**.")

# ------------------ Validation Function ------------------
def validate_input(pattern, text):
    return re.fullmatch(pattern, text)

# ------------------ Form ------------------
with st.form("user_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Full Name", placeholder="e.g., John Doe")
        dob = st.date_input("📅 Date of Birth")

    with col2:
        email = st.text_input("📧 Email ID", placeholder="e.g., example@gmail.com")
        mobile = st.text_input("📞 Mobile Number", placeholder="10-digit number")

    submitted = st.form_submit_button("🚀 Submit")

# ------------------ Validation ------------------
name_valid = validate_input(r'^[A-Za-z ]+$', name)
email_valid = validate_input(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$', email)
mobile_valid = validate_input(r'^[0-9]{10}$', mobile)
dob_str = dob.strftime("%d-%m-%Y")

# ------------------ Output ------------------
if submitted:
    if all([name_valid, email_valid, mobile_valid]):
        st.success("✅ All details are valid!")

        st.markdown(f"""
        <div class="submitted-box">
            <p><strong>👤 Name:</strong> {name}</p>
            <p><strong>📅 DOB:</strong> {dob_str}</p>
            <p><strong>📧 Email:</strong> {email}</p>
            <p><strong>📞 Mobile:</strong> {mobile}</p>
        </div>
        """, unsafe_allow_html=True)

        df = pd.DataFrame({
            "Name": [name],
            "DOB": [dob_str],
            "Email": [email],
            "Mobile": [mobile]
        })
        st.download_button("⬇ Download Info as CSV", df.to_csv(index=False), file_name="user_info.csv", mime="text/csv")

    else:
        st.error("⚠ Please fix the invalid fields below:")

        # Custom white-background warning style
        warning_style = """
        <div style="background-color: white; padding: 10px 15px; border-radius: 8px;
                    color: #000; font-weight: 500; margin-bottom: 10px;">
            🔴 {message}
        </div>
        """

        if not name_valid:
            st.markdown(warning_style.format(message="Name should contain only letters and spaces."), unsafe_allow_html=True)

        if not email_valid:
            st.markdown(warning_style.format(message="Email should be like: example@gmail.com"), unsafe_allow_html=True)

        if not mobile_valid:
            st.markdown(warning_style.format(message="Mobile number should be exactly 10 digits."), unsafe_allow_html=True)
