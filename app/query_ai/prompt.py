from langchain.prompts import PromptTemplate
import os

no_answer_instruction = os.environ['NO_ANSWER_INSTRUCTION']


prompt_template = """
Use the following pieces of context to answer the question at the end. 
""" + no_answer_instruction + """

{context}

Question: {question}

""" + no_answer_instruction + """
Remember: DO NOT USE ANY INFORMATION IN YOUR RESPONSE THAT IS NOT PROVIDED ABOVE!
"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)