import streamlit as st
import time as time

uploadedImage=None
uploaded_file=None
promts = []

from memory import chat_memory
from memory import add_to_memory

from service import reponse_generation
from service import chat_memory

def main():
    # cssCodeExecution() 
    col1,col2=st.columns([1,2])
    st.sidebar.markdown("<h1 style='font-size: 32px;'>Code Assist+</h1>", unsafe_allow_html=True)
   
    
    
    selected_option=st.sidebar.selectbox("Navigation :",options=["Code Review Chatbot", "About"])
    
    if selected_option=="Code Review Chatbot":
        st.title("Code Review Chatbot")
        userPrompt=st.chat_input(placeholder="Please Enter Your promt")

        if userPrompt:
            answer=reponse_generation(userPrompt)
            
            # add_to_memory(response=answer,user_input= userPrompt)
        
        raw_memory_history=chat_memory()
        human_strings,ai_strings=formatAIResponse(raw_memory_history)
        printUi(human_strings,ai_strings)



    elif selected_option=="About":
        st.title("About")
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

    

    

# .header
#         {
#             background-color: white; /* Light grey background for header */
#             padding: 35px;
#             color: aqua;
#             position: fixed; /* Fix the header to the top */
#             top: 0; /* Position it at the top of the viewport */
#             width: 100%; /* Make it span the entire width */
#             z-index: 5; /* Ensure the header stays on top during scrolling */
#         }


# def cssCodeExecution():
#     st.markdown("""
#     <style>
        
#         .question-container 
#         {
#             border-radius: 10px; /* Round corners */
#             overflow-y: auto; /* Enable scrolling for content within */
#         }
#         .human 
#         {
#             background-color: #e0e0e0; /* Light grey background for question */
#             padding: 5px; /* Add some padding for better separation */
#             border-radius: 5px; /* Round corners for the question paragraph */
#             font-weight: bold; /* Bold text for question */
#         }
#         .st-emotion-cache-18ni7ap.ezrtsby2
#         {
#             visibility:hidden;
#         }
#     </style>
#     """,unsafe_allow_html=True)




def printUi(human,AI):
    for i in range(len(human)):
        with st.container():
            st.markdown(f"<div class='question-container'><div class='text-container'><p class='human'>{human[i]}</p ><p class='ai'>{AI[i]}</p></div></div>", unsafe_allow_html=True)

def formatAIResponse(raw_memory_history):
    full_string = raw_memory_history['history'] 
    human_strings, ai_strings = [], []
    current_speaker = None  
    for line in full_string.splitlines():  
        if line.startswith('Human:'):
            current_speaker = 'Human'
            human_strings.append(line.replace('Human:', '', 1).strip())  
        elif line.startswith('AI:'):
            current_speaker = 'AI'
            ai_strings.append(line.replace('AI:', '', 1).strip())  
        elif current_speaker:  
            human_strings[-1] += '\n' + line if current_speaker == 'Human' else ''
            ai_strings[-1] += '\n' + line if current_speaker == 'AI' else ''
    return human_strings,ai_strings   

                 
if __name__ == "__main__":
    main()