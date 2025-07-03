import streamlit as st
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# OpenAI Client
client = OpenAI()

# Streamlit App
st.title("OpenAI Moderation API Demo")
st.write("Test the OpenAI Moderation API with your own text")

# Text Input
user_input = st.text_area("Text to moderate:", placeholder="Enter your text here...")

if st.button("Moderate Text"):
    if user_input:
        with st.spinner("Moderating text..."):
            try:
                # OpenAI API call
                response = client.moderations.create(
                    model="omni-moderation-latest",
                    input=user_input,
                )
                
                result = response.results[0]
                
                # Display status
                if result.flagged:
                    st.error("Text was flagged as problematic")
                else:
                    st.success("Text is safe")
                
                # Scores as bar chart
                st.subheader("Category Scores")
                
                # Prepare data for chart
                categories = []
                scores = []
                
                for category, score in result.category_scores.__dict__.items():
                    # Only show categories with score > 0.001
                    if score > 0.001:
                        categories.append(category.replace('_', '/'))
                        scores.append(score)
                
                if categories:
                    # DataFrame for Streamlit
                    df = pd.DataFrame({
                        'Category': categories,
                        'Score': scores
                    })
                    
                    # Bar chart
                    st.bar_chart(df.set_index('Category'))
                    
                    # Detailed table
                    st.subheader("Detailed Results")
                    st.dataframe(df.sort_values('Score', ascending=False))
                else:
                    st.info("All category scores are very low (< 0.001)")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text!")
