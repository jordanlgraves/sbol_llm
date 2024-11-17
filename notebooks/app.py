import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

prompt_1 = "<Enter your prompt which will take user input in the textbox and incorporate it, then get a response from openai which will print in a second textbox>. Use f strings"

def chatgpt_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

def main():
    st.title("SBOL Description Generator")

    # Create an input text box
    user_input = st.text_area("Enter your description:", "Type here...", height=150)

    # Create two columns for buttons
    col1, col2 = st.columns(2)

    # Create a container for the response
    response_container = st.container()

    # Button to refine description
    with col1:
        if st.button("Refine Description"):
            if user_input and user_input != "Type here...":
                with response_container:
                    refined_text = chatgpt_response(user_input)
                    st.text_area("Refined Description:", value=refined_text, height=150, disabled=True)

    # Button to convert to SBOL
    with col2:
        if st.button("Convert to SBOL"):
            # For now, just create a blank CSV
            import io
            import pandas as pd

            # Create an empty DataFrame
            df = pd.DataFrame()

            # Convert to CSV
            csv = df.to_csv(index=False).encode('utf-8')

            # Create download button
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="blank_sbol.csv",
                mime="text/csv"
            )

    # Display the original input below
    if user_input and user_input != "Type here...":
        st.write("Original input:", user_input)

if __name__ == "__main__":
    main()
