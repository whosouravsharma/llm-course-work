from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor 
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI, OpenAI
from langchain_tavily import TavilySearch, tavily_search

tools = [TavilySearch()]
llm = ChatOpenAI(model = 'gpt-4')
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    result = chain.invoke(
        input = {
            "input": "Search for job postings for an AI engineer using langchain in Hyderabad India on linkedin and list their details"
        }
    )

    print(result)

if __name__ == "__main__":
    main()
