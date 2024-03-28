import os
import json
import pandas as pd
import constants
import PyPDF2
import warnings

from langchain._api import LangChainDeprecationWarning
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.callbacks import get_openai_callback
from dotenv import load_dotenv

warnings.simplefilter("ignore", category=LangChainDeprecationWarning)


load_dotenv()
apikey = os.environ["OPENAI_KEY"]

# PATH = "D:\Pyhton\genie-mcq\Response.json"
with open(constants.PATH,"r") as f:
    RESPONSE_JSON=json.load(f)

# Initialize the ChatOpenAI object with the specified parameters
llm = ChatOpenAI(openai_api_key=apikey, model_name="gpt-3.5-turbo", temperature=0.7)

# Prompt for generating MCQs and evaluating them
mcq_prompt = PromptTemplate(input_variables=["text","number","subject","tone","RESPONSE_JSON"],template=constants.TEMPLATE)

# Chain for generating MCQs     
mcq_chain = LLMChain(llm=llm,prompt=mcq_prompt,output_key="mcq",verbose=True)

# Prompt for evaluating the MCQs
review_prompt = PromptTemplate(input_variables=["subject","mcq"],template=constants.TEMPLATE2)

# Chain for evaluating the MCQs
review_chain = LLMChain(llm=llm,prompt=review_prompt,output_key="review",verbose=True)


# Main model
generate_evaluate_chain=SequentialChain(chains=[mcq_chain, review_chain], input_variables=["text", "number", "subject", "tone", "RESPONSE_JSON"],output_variables=["mcq", "review"], verbose=True,)