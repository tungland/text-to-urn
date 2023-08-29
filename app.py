import streamlit as st
import pandas as pd
import re

PATTERN = re.compile(r"URN:NBN:no-nb[a-zA-Z0-9_]+")

# Define the Streamlit app
def app():
    # Set the app title
    st.title("Tekst til URN")

    # Add a text input for the user to enter text
    text_input = st.text_area("Enter text:")

    # Add a regex pattern input for the user to enter a pattern to search for
    #pattern_input = st.text_input("Enter regex pattern:")
    # st.markdown("`Pattern: URN:NBN:no-nb[a-zA-Z0-9_]+`")
    
    # Define a function to search for the pattern in the text and return all matches as a Pandas dataframe
    def search_pattern(text, pattern):
        # Use the re module to search for the pattern in the text
        matches = re.findall(pattern, text)

        # Create a Pandas dataframe from the matches
        df = pd.DataFrame(matches, columns=["Match"])

        return df

    # Add a button to run the pattern search and download the results as a CSV file
    if st.button("Search and Download"):
        # Call the search_pattern function with the user's inputs
        results = search_pattern(text_input, PATTERN)

        # Download the results as a CSV file
        st.download_button(
            label="Download Results as CSV",
            data=results.to_csv(index=False),
            file_name="regex_results.csv",
            mime="text/csv"
        )

        # Display the results as a Pandas dataframe
        st.dataframe(results)

# Run the Streamlit app
if __name__ == "__main__":
    app()