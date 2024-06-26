import cohere

import streamlit as st

import html




# Your Cohere API key (ensure this is kept secret in actual deployments)

cohere_api_key = "btu0gWrLzedOkMOrjGC1k6gEhVbIcR0GdsrNlT24"




# Initialize conversation history in session state

if "messages" not in st.session_state:

    st.session_state["messages"] = []




def append_message(role, content):

    """Appends a message to the conversation history."""

    st.session_state["messages"].append({"role": role, "content": content})




def display_conversation():

    """Displays the conversation history."""

    for message in st.session_state["messages"]:

        if message['role'] == 'user':

            st.write(f"**You**: {message['content']}")

        else:

            st.write(f"**Chatbot**: {message['content']}")




# Define the sidebar navigation

st.sidebar.markdown("<h1 style='font-size: 32px;'>Code Assist+</h1>", unsafe_allow_html=True)

st.sidebar.title("Navigation")

app_mode = st.sidebar.selectbox("Choose the app mode", ["Code Review Chatbot", "About"])




if app_mode == "Code Review Chatbot":

    st.title("Code Review Chatbot")




    # User input field for code

    user_code_input = st.text_area("Enter your code here:")




    # Button to submit code

    if st.button("Send"):

        if user_code_input:

            # Append user code to history

            append_message("user", user_code_input)




            # Display conversation including the loading state

            with st.spinner('Waiting for response...'):

                try:

                    # Initialize Cohere client

                    co = cohere.Client(cohere_api_key)




                    # Generate response from the chatbot

                    response = co.generate(

                        model='command-xlarge-nightly',

                        prompt=f"Review the following code and provide feedback:\n\n{user_code_input}",

                        max_tokens=1000  # Increased max tokens for a longer response

                    )




                    # Extract chatbot response

                    bot_response = response.generations[0].text.strip()

                    append_message("bot", bot_response)

                except Exception as e:

                    bot_response = f"An error occurred: {e}"

                    append_message("bot", bot_response)

        

        # Display conversation history

        display_conversation()




elif app_mode == "About":

    st.title("About Code Assist+")

    st.markdown("""

    **Code Assist+** is a powerful tool designed to help developers with their coding needs. Whether you are looking for code reviews, debugging assistance, or learning new programming concepts, Code Assist+ has you covered.




    ### Features

    - **Code Review Chatbot**: Get feedback and suggestions on your code snippets.

    - **Learning Resources**: Access tutorials and guides on various programming topics.

    - **Debugging Tools**: Find and fix errors in your code quickly and efficiently.

    - **Community Support**: Join a community of developers to share knowledge and collaborate on projects.




    ### How to Use

    1. Navigate to the desired tab using the sidebar.

    2. Enter your code or query in the input fields provided.

    3. Click "Send" to get feedback or assistance.




    We hope Code Assist+ becomes an essential part of your development workflow. Happy coding!

    """)
