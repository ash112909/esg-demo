import streamlit as st
import plotly.graph_objects as go
import os
import numpy as np

# Ensure the path to the image is correct
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, 'bok_logo.png')

# Sample data extracted from PDFs
sample_data = {
    'Apple Inc.': {
        'Carbon Footprint': 70,
        'Energy Management': 65,
        'Water Management': 80,
        'Waste Management': 75,
        'Biodiversity and Land Use': 60,
        'Pollution and Toxics': 55,
        'Resource Management': 68,
        'Labor Practices': 70,
        'Diversity and Inclusion': 60,
        'Community Engagement': 75,
        'Customer Satisfaction': 85,
        'Human Rights': 50,
        'Employee Development': 80,
        'Social Impact': 65,
        'Animal Welfare': 55,
        'Board Diversity and Structure': 70,
        'Executive Compensation': 60,
        'Business Ethics': 75,
        'Transparency and Disclosure': 65,
        'Shareholder Rights': 70,
        'Regulatory Compliance': 80,
        'Risk Management': 85,
    },
    'Bank of America Corporation': {
        'Carbon Footprint': 75,
        'Energy Management': 70,
        'Water Management': 65,
        'Waste Management': 80,
        'Biodiversity and Land Use': 60,
        'Pollution and Toxics': 70,
        'Resource Management': 75,
        'Labor Practices': 80,
        'Diversity and Inclusion': 85,
        'Community Engagement': 90,
        'Customer Satisfaction': 95,
        'Human Rights': 60,
        'Employee Development': 85,
        'Social Impact': 75,
        'Animal Welfare': 55,
        'Board Diversity and Structure': 80,
        'Executive Compensation': 70,
        'Business Ethics': 80,
        'Transparency and Disclosure': 75,
        'Shareholder Rights': 85,
        'Regulatory Compliance': 90,
        'Risk Management': 95,
    },
    'Duke Energy Corporation': {
        'Carbon Footprint': 80,
        'Energy Management': 85,
        'Water Management': 75,
        'Waste Management': 70,
        'Biodiversity and Land Use': 65,
        'Pollution and Toxics': 75,
        'Resource Management': 80,
        'Labor Practices': 85,
        'Diversity and Inclusion': 70,
        'Community Engagement': 75,
        'Customer Satisfaction': 80,
        'Human Rights': 65,
        'Employee Development': 75,
        'Social Impact': 70,
        'Animal Welfare': 60,
        'Board Diversity and Structure': 75,
        'Executive Compensation': 80,
        'Business Ethics': 85,
        'Transparency and Disclosure': 70,
        'Shareholder Rights': 75,
        'Regulatory Compliance': 80,
        'Risk Management': 85,
    },
    'Eli Lilly and Company': {
        'Carbon Footprint': 85,
        'Energy Management': 80,
        'Water Management': 70,
        'Waste Management': 75,
        'Biodiversity and Land Use': 85,
        'Pollution and Toxics': 80,
        'Resource Management': 85,
        'Labor Practices': 80,
        'Diversity and Inclusion': 75,
        'Community Engagement': 85,
        'Customer Satisfaction': 90,
        'Human Rights': 75,
        'Employee Development': 80,
        'Social Impact': 85,
        'Animal Welfare': 65,
        'Board Diversity and Structure': 85,
        'Executive Compensation': 75,
        'Business Ethics': 85,
        'Transparency and Disclosure': 80,
        'Shareholder Rights': 85,
        'Regulatory Compliance': 90,
        'Risk Management': 80,
    },
    'Exxon Mobil Corporation': {
        'Carbon Footprint': 70,
        'Energy Management': 65,
        'Water Management': 80,
        'Waste Management': 75,
        'Biodiversity and Land Use': 60,
        'Pollution and Toxics': 55,
        'Resource Management': 68,
        'Labor Practices': 70,
        'Diversity and Inclusion': 60,
        'Community Engagement': 75,
        'Customer Satisfaction': 85,
        'Human Rights': 50,
        'Employee Development': 80,
        'Social Impact': 65,
        'Animal Welfare': 55,
        'Board Diversity and Structure': 70,
        'Executive Compensation': 60,
        'Business Ethics': 75,
        'Transparency and Disclosure': 65,
        'Shareholder Rights': 70,
        'Regulatory Compliance': 80,
        'Risk Management': 85,
    },
    'General Dynamics Corporation': {
        'Carbon Footprint': 65,
        'Energy Management': 60,
        'Water Management': 55,
        'Waste Management': 70,
        'Biodiversity and Land Use': 50,
        'Pollution and Toxics': 45,
        'Resource Management': 55,
        'Labor Practices': 60,
        'Diversity and Inclusion': 50,
        'Community Engagement': 65,
        'Customer Satisfaction': 75,
        'Human Rights': 40,
        'Employee Development': 70,
        'Social Impact': 55,
        'Animal Welfare': 45,
        'Board Diversity and Structure': 60,
        'Executive Compensation': 50,
        'Business Ethics': 65,
        'Transparency and Disclosure': 55,
        'Shareholder Rights': 60,
        'Regulatory Compliance': 70,
        'Risk Management': 75,
    },
    'Under Armour, Inc.': {
        'Carbon Footprint': 60,
        'Energy Management': 55,
        'Water Management': 50,
        'Waste Management': 65,
        'Biodiversity and Land Use': 45,
        'Pollution and Toxics': 40,
        'Resource Management': 50,
        'Labor Practices': 55,
        'Diversity and Inclusion': 45,
        'Community Engagement': 60,
        'Customer Satisfaction': 70,
        'Human Rights': 35,
        'Employee Development': 65,
        'Social Impact': 50,
        'Animal Welfare': 40,
        'Board Diversity and Structure': 55,
        'Executive Compensation': 45,
        'Business Ethics': 60,
        'Transparency and Disclosure': 50,
        'Shareholder Rights': 55,
        'Regulatory Compliance': 65,
        'Risk Management': 70,
    },
}
# Custom CSS for header, footer, and sidebar styling
st.markdown("""
    <style>
        .main-header {
            background-color: #800000;
            padding: 20px;
            text-align: center;
            color: #FFFFFF;
            font-size: 36px;
            font-weight: bold;
        }
        .main-footer {
            background-color: #800000;
            padding: 10px;
            text-align: center;
            color: #FFFFFF;
            font-size: 12px;
        }
        .sidebar .sidebar-content {
            background-color: #FFFFFF;
        }
        .reportview-container {
            background-color: #FFFFFF;
        }
        .stSlider > div > div > div > div {
            background-color: #800000;
        }
        .st-bq, .st-ae, .st-cm, .st-dm {
            color: #800000;
        }
        .reportview-container .markdown-text-container {
            font-family: 'Arial', sans-serif;
        }
        .final-score {
            font-size: 32px;
            font-weight: bold;
            color: #800000;
            text-align: center;
        }
        .list-scores {
            padding: 10px;
        }
        .summary-section {
            background-color: #f8f8f8;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .filter-options {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Add header
st.markdown('<div class="main-header">BOK Financial ESG Scoring Application</div>', unsafe_allow_html=True)

# Sidebar content
st.sidebar.image(logo_path, use_column_width=True)
st.sidebar.header("Set Your Preferences")

# Function to calculate the average ESG score across all holdings
def calculate_average_esg(scores):
    total_companies = len(scores)
    average_scores = {key: 0 for key in scores[0].keys()}
    for score in scores:
        for key in score:
            average_scores[key] += score[key]
    for key in average_scores:
        average_scores[key] = average_scores[key] / total_companies
    return average_scores

# Main section for the home dashboard
st.title("Score Dashboard")

# Summary Section
st.markdown('<div class="summary-section"><h3>ESG Scoring Summary</h3><p>Get key insights and trends from the ESG scores of your selected companies.</p></div>', unsafe_allow_html=True)

# Select companies to include in the average calculation
selected_companies = st.multiselect(
    "Select Companies for Average ESG Score",
    options=list(sample_data.keys()),
    default=list(sample_data.keys())
)

weights = {}
for subsector in sample_data['Apple Inc.']:
    weights[subsector] = st.sidebar.slider(f"{subsector} Weight", 0, 100, 50)

total_weight = sum(weights.values())

if selected_companies:
    scores = [sample_data[company] for company in selected_companies]
    average_scores = calculate_average_esg(scores)
    
    # Calculate final score
    final_score = sum(
        average_scores[subsector] * weights[subsector] / total_weight for subsector in average_scores
    )

    st.subheader(f"Final ESG Score Across Selected Holdings: {final_score:.2f}")

    # Determine the top 5 preferences
    sorted_avg_scores = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)
    top_preferences = sorted_avg_scores[:5]
    other_preferences = sorted_avg_scores[5:]

    # Plotting average ESG scores for top 5 preferences using color-coded gauges
    fig_avg = go.Figure()

    for i, (preference, value) in enumerate(top_preferences):
        fig_avg.add_trace(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': preference},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#800000"},
                'steps': [
                    {'range': [0, 50], 'color': "red"},
                    {'range': [50, 75], 'color': "yellow"},
                    {'range': [75, 100], 'color': "green"}
                ],
            },
            domain={'row': i // 2, 'column': i % 2}
        ))

    fig_avg.update_layout(
        grid={'rows': 3, 'columns': 2, 'pattern': "independent"},
        height=600, width=800
    )

    st.plotly_chart(fig_avg)

    # Display other preferences as a list
    st.subheader("Other ESG Scores")
    other_scores_list = '<div class="list-scores">'
    for preference, value in other_preferences:
        other_scores_list += f'<p><b>{preference}:</b> {value:.2f}</p>'
    other_scores_list += '</div>'
    st.markdown(other_scores_list, unsafe_allow_html=True)

    # Filter Options Section
    st.markdown('<div class="filter-options"><h3>Filter Options</h3></div>', unsafe_allow_html=True)
    filter_options = [preference for preference, _ in top_preferences]
    filters = st.multiselect(
        "Filter by ESG Criteria",
        options=list(sample_data['Apple Inc.'].keys()),
        default=filter_options
    )
    if filters:
        filtered_data = {company: {key: value for key, value in sample_data[company].items() if key in filters} for company in selected_companies}
        filtered_fig = go.Figure()
        for company in selected_companies:
            filtered_fig.add_trace(go.Bar(
                x=list(filtered_data[company].keys()),
                y=list(filtered_data[company].values()),
                name=company
            ))
        filtered_fig.update_layout(barmode='group', title="Filtered ESG Scores Comparison")
        st.plotly_chart(filtered_fig)

# Add footer
st.markdown('<div class="main-footer">Powered by BOK Financial</div>', unsafe_allow_html=True)
