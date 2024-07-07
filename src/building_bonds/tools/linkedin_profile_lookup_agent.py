from langchain_core.prompts import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults

from src.utils import get_llm


def profile_url_lookup_agent(person_name: str) -> str:
    template = """Find a LinkedIn profile page of {name_of_person}. I want you to get me a link to his/her LinkedIn profile page.
                  Your answer should contain only a URL of the LinkedIn profile"""

    tools = [
        TavilySearchResults(
            max_results=1,
            description="Useful for getting LinkedIn profile page url by searching the web"
        )
    ]

    llm = get_llm()
    agent_chain = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True,
        handle_parsing_errors=True
    )

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    try:
        agent_output = agent_chain.invoke(handle_parsing_errors=True, input=prompt_template.format_prompt(name_of_person=person_name))
        profile_url = agent_output.get('output')

    except ValueError as e:
        print("Error while parsing LLM output:", e)
        return None
    
    return profile_url
