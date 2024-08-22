# Open-source llms:
In case you want to work with open-source llms, you need to install a tool called OLLama

## What is Ollama?
With Ollama, you can use open-source large language models (LLMs) in Langchain, such as Llama3.1, Gemma2, and Mistral. Similar procedures apply to using Ollama with some LLM in LangChain but there may be differences in the APIs or installations. The following describes how to utilize Llama3.1 in LangChain with Ollama:

## Using Llama3.1 with LangChain via Ollama

First of all, you have to install Ollama. You can get it from here https://ollama.com/. Since Llama3.1 is open-source, you need to install the llm on your computer. This can take time and require space. You can check for different llms available here: https://github.com/ollama/ollama. To install llm you have to run ollama run [llm_name] in your cmd.

1. **Install Dependencies**

   ```bash
   pip install langchain langchain_core langchain_community ollama
   ```

2. **Create a Llama3.1 Chain**

   ```python
    from langchain_community.llms import Ollama
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    ## Langmith tracking

    # Initialize the OpenAI model
    llm = Ollama(model="llama3.1")

    # Define a prompt template

    prompt = PromptTemplate("Give answer to {question}.")
    
    # You have to use outputparser
    outputparser = StrOutputParser

    # Create an LLM chain
    chain = prompt | llm | outputparser
    
    # Use the chain to generate text
    response = chain.invoke({"question": "What is the capital of Belgium?"})
    print(response)
   ```