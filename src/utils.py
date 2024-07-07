from langchain_aws import BedrockLLM

def get_llm(model_id: str = "anthropic.claude-v2"):

    bedrock_llm = BedrockLLM(
        model_id=model_id,
        model_kwargs={
            "temperature": 0.1,
            "max_tokens_to_sample": 4096
        },
        region_name="us-west-2"
    )

    return bedrock_llm