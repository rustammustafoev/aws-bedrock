
# Prerequisites
1. Make sure that you have set up `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in `.aws` directory within `credentials` file
2. Go to Amazon Bedrock Console's model access section to request an access for models
3. After cloning the repository, run `cd aws_bedrock`
4. Run `export PYTHONPATH=$PYTHONPATH:$(pwd)/src`
5. Then, run `chmod +x run.sh`
6. Using `pyenv` set up your python version above 3.11 e.g. `pyenv local 3.11.5`
7. Run the following command to install project dependencies
```bash
poetry env use $(pyenv which python)
poetry install
```
8. Afterwards, to activate virtual env run `poetry shell`

# How to get demo applications up and running

## Building Bonds
1. Set env for Tavily Search and Nubela in `.env` file, check the naming convention from `.env.example` file
2. Run `./run.sh building_bonds`

## Ingredient to Recipe
1. Set HuggingFace API Token in `.env`
2. Run `./run.sh ingredient_to_recipe`

## Resume Screening
1. Spin up Postgres container with pgvector extension `docker run --name pgvector-container -e POSTGRES_USER=russ -e POSTGRES_PASSWORD=russ -e POSTGRES_DB=resume_screener -p 6024:5432 -d pgvector/pgvector:pg16`
2. Run `./run.sh resume_screening`



# References
- [Official Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon Bedrock Workshop](https://github.com/aws-samples/amazon-bedrock-workshop)
- [GenAI Workshop](https://github.com/build-on-aws/gen-ai-workshop)
- [Amazon Bedrock Agents Quickstart](https://github.com/build-on-aws/amazon-bedrock-agents-quickstart)
- [Amazon Bedrock Agents Outfit Assistant](https://github.com/build-on-aws/amazon-bedrock-agents-outfit-assistant)
- [Amazon Bedrock Agents Webscraper](https://github.com/build-on-aws/bedrock-agents-webscraper)
- [Amazon Bedrock Agents Streamlit](https://github.com/build-on-aws/bedrock-agents-streamlit)
- [Sample Application with Amazon Bedrock](https://github.com/build-on-aws/llm-rag-vectordb-python)

# More
- [Aleksandr Bernadskii - Building GenAI apps with Amazon Bedrock](https://www.youtube.com/watch?v=Ye3_s0oDanc)
- [LangChain - framework for building GenAI applications](https://www.langchain.com/)
- [LangGraph - framework for building multi-agent workflows with LLMs](https://langchain-ai.github.io/langgraph/)
- [Streamlit - framework for AI/ML engineers for building fast interactive data apps](https://streamlit.io/)