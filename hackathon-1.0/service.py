

import os
from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

os.environ['GOOGLE_API_KEY']="AIzaSyB5MNZuSc0he6C3jsvGR2onARHoMIUW3Ag"
model=ChatGoogleGenerativeAI(model='gemini-1.0-pro')
memory=ConversationBufferMemory()


def reponse_generation(userPrompt):
    prompt1 = PromptTemplate(
    input_variables=["userPrompt"],
    # template="You are a helpful assistant. A user said: {userPrompt}. Respond appropriately."
    template="Review the following code and provide feedback:\n\n{userPrompt}"
    )

    conversation = LLMChain(
        llm=model,
        prompt=prompt1,
        verbose=True,
        memory=memory
    )

    reponse=conversation.invoke(userPrompt)
    print("out pit:::::::",reponse)

def chat_memory():
  raw_memory=memory.load_memory_variables({})
  return raw_memory
