import streamlit as st
import re
import string

st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for black and yellow theme
st.markdown("""
<style>
    .main {
        background-color: #121212;
        color: #FFF;
    }
    .stTextInput > div > div > input {
        background-color: #1E1E1E;
        color: #FFF;
        border: 1px solid #FFD700;
    }
    .password-very-weak {
        background-color: #3D3D3D;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .password-weak {
        background-color: #3D3D3D;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .password-medium {
        background-color: #3D3D3D;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .password-strong {
        background-color: #3D3D3D;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .password-very-strong {
        background-color: #3D3D3D;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    h1, h2, h3 {
        color: #FFD700 !important;
    }
    .stButton button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Password Strength Meter")
st.markdown("### Check how strong your password is")

password = st.text_input("Enter your password", type="password")

def check_password_strength(password):
    score = 0
    feedback = []
 
    if len(password) == 0:
        return 0, ["Please enter a password"]
    elif len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters)")
    else:
        score += 1
        if len(password) >= 12:
            score += 1
 
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r'[' + re.escape(string.punctuation) + ']', password):
        score += 1
    else:
        feedback.append("Add special characters")

    common_patterns = ['123456', 'password', 'qwerty', 'admin', '12345']
    if any(pattern in password.lower() for pattern in common_patterns):
        score = max(0, score - 2)
        feedback.append("Avoid common patterns")

    if not feedback and score >= 4:
        feedback.append("Strong password!")
        
    return score, feedback

if password:
    strength_score, feedback = check_password_strength(password)
    if strength_score == 0:
        strength_category = "Very Weak"
        color = "#FF0000"
        percentage = 10
    elif strength_score <= 2:
        strength_category = "Weak"
        color = "#FF4500"
        percentage = 25
    elif strength_score <= 3:
        strength_category = "Medium"
        color = "#FFA500"
        percentage = 50
    elif strength_score <= 4:
        strength_category = "Strong"
        color = "#9ACD32"
        percentage = 75
    else:
        strength_category = "Very Strong"
        color = "#00FF00"
        percentage = 100
    st.markdown(f"### Password Strength: {strength_category}")
    st.markdown(
        f"""
        <div style="background-color: #3D3D3D; border-radius: 10px; height: 30px; width: 100%;">
            <div style="background-color: {color if strength_score > 0 else '#3D3D3D'}; 
                        width: {percentage}%; 
                        height: 100%; 
                        border-radius: 10px;
                        background: linear-gradient(90deg, #FFD700 0%, {color} 100%);">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("### Feedback")
    for item in feedback:
        st.markdown(f"- {item}")
    st.markdown("### Password Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"**Length:** {len(password)}")
    
    with col2:
        uppercase_count = sum(1 for c in password if c.isupper())
        st.markdown(f"**Uppercase:** {uppercase_count}")
    
    with col3:
        lowercase_count = sum(1 for c in password if c.islower())
        st.markdown(f"**Lowercase:** {lowercase_count}")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        digit_count = sum(1 for c in password if c.isdigit())
        st.markdown(f"**Numbers:** {digit_count}")
    
    with col5:
        special_count = sum(1 for c in password if c in string.punctuation)
        st.markdown(f"**Special:** {special_count}")
    
    with col6:
        unique_chars = len(set(password))
        st.markdown(f"**Unique Chars:** {unique_chars}")
with st.expander("Password Security Tips"):
    st.markdown("""
    ### Tips for a Strong Password
    
    1. **Use at least 12 characters** - The longer, the better
    2. **Mix uppercase and lowercase letters**
    3. **Include numbers and special characters** (!@#$%^&*)
    4. **Avoid common words or patterns**
    5. **Don't use personal information** (birthdays, names, etc.)
    6. **Use a different password for each account**
    7. **Consider using a password manager**
    """)
st.markdown("---")
st.markdown("Made by ♥ Mussawir Sohail")