# **GPT:**
GPT (Generative Pre-trained Transformer) is a type of large language model (LLM) developed by OpenAI. We are using this because it is designed to generate human-like text based on the input it receives and also it powers our most favourite AI tool called ChatGPT so we are going to see how it works with langchain.

## Using GPT in LangChain

1. **Install Dependencies**
   - Ensure you have the necessary packages installed:
     
     ```bash
     pip install langchain openai langchain_core
     ```

2. **Setup GPT with LangChain**
   - First, configure your OpenAI API key. You can set it up in your environment or directly in your code.

3. **Create a GPT Chain**
   - Use LangChain’s API to create a chain that uses GPT for generating responses.

   ```python
    from langchain import OpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    ## Langmith tracking
    os.environ["LANGCHAIN_TRACING_V2"]="true"
    os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

    # Initialize the OpenAI model
    llm = OpenAI()

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
