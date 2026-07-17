import streamlit as st
import pandas as pd
import pickle
import re

# ==========================
# Load Model
# ==========================
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

# ==========================
# Page Config
# ==========================
st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Spam Detection")
st.write("Predict whether an email is **Spam** or **Not Spam**.")

# ==========================
# User Input
# ==========================
subject = st.text_input("Email Subject")

body = st.text_area(
    "Email Body",
    height=250
)

attachment = st.selectbox(
    "Has Attachment?",
    ["No", "Yes"]
)

# ==========================
# Prediction
# ==========================
if st.button("Predict"):

    if body.strip() == "":
        st.warning("Please enter an email body.")
        st.stop()

    # Use body text for feature extraction
    text = body

    email_length = len(text)

    num_links = len(
        re.findall(r"http[s]?://|www\.", text)
    )

    num_special_chars = len(
        re.findall(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", text)
    )

    capital_words = len(
        re.findall(r"\b[A-Z]{2,}\b", text)
    )

    has_attachment = 1 if attachment == "Yes" else 0

    # Create feature dataframe
    features = pd.DataFrame({
        "Email_Length": [email_length],
        "Num_Links": [num_links],
        "Num_Special_Chars": [num_special_chars],
        "Capital_Words": [capital_words],
        "Has_Attachment": [has_attachment]
    })

    # If model expects Subject, provide a dummy value
    if hasattr(model, "feature_names_in_"):
        if "Subject" in model.feature_names_in_:
            features.insert(0, "Subject", 0)

        # Ensure column order matches model
        features = features[model.feature_names_in_]

    try:
        prediction = model.predict(features)[0]

        confidence = None
        if hasattr(model, "predict_proba"):
            confidence = model.predict_proba(features).max() * 100

        st.divider()

        if prediction == 1:
            st.error("🚨 Spam Email Detected")
        else:
            st.success("✅ Legitimate Email")

        if confidence is not None:
            st.progress(int(confidence))
            st.write(f"Confidence: **{confidence:.2f}%**")

        with st.expander("Extracted Features"):
            st.dataframe(features)

    except Exception:
        st.error("Prediction failed. Please make sure the model matches the input features.")

st.markdown("---")
st.caption("Developed with ❤️ using Streamlit & Scikit-learn")