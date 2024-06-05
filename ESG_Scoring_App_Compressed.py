import streamlit as st
import numpy as np

# Sample data (replace with your actual data)
sample_data = {
    'Apple Inc.': 80.60,
    'Bank of America Corporation': 75.20,
    'Duke Energy Corporation': 78.40,
    'Eli Lilly and Company': 82.10,
    'Exxon Mobil Corporation': 77.90,
    'General Dynamics Corporation': 69.80,
    'Under Armour, Inc.': 65.50,
}

# Function to calculate the average ESG score across selected holdings
def calculate_average_score(data):
    return np.mean(list(data.values()))

# Main section for the compressed app
st.title("Overall ESG Score")

# Display the overall ESG score using a gauge
overall_score = calculate_average_score(sample_data)
st.subheader("Overall ESG Score")
st.write(f"The overall ESG score is: {overall_score:.2f}")
# Display the score using a gauge (for demonstration purposes, using a progress bar instead of a gauge)
st.progress(overall_score / 100)  # Assuming overall_score ranges from 0 to 100

# Option to filter holdings
st.sidebar.title("Filter Holdings")
selected_companies = st.sidebar.multiselect(
    "Select Companies",
    options=list(sample_data.keys()),
    default=list(sample_data.keys())
)

# Calculate the overall score based on selected holdings
filtered_data = {company: score for company, score in sample_data.items() if company in selected_companies}
filtered_score = calculate_average_score(filtered_data)

# Display filtered score
st.sidebar.subheader("Filtered ESG Score")
st.sidebar.write(f"The filtered ESG score is: {filtered_score:.2f}")
st.sidebar.progress(filtered_score / 100)  # Assuming filtered_score ranges from 0 to 100

# Link to change preferences (redirects to the original app)
st.sidebar.markdown("[Change Preferences](https://esg-scoring-demo.streamlit.app/)")
