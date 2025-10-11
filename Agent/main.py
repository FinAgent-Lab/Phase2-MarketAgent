import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

from Agent.Util.util import create_llm
from Agent.Graph.FredGraph import FredGraph



ANALYSIS_PROMPT = PromptTemplate.from_template(
    """너의 동료들은 최고의 미국 주식 전문가들이야
    동료들은 각각 미국 메크로 지표를 보고 판단해 S&P500 섹터를 3가지 씩 추천했어 
    추천한 섹터와 내용을 보고 종합적으로 판단해 향후 유망한 섹터 3개를 추천해줘
    

    #동료들의 추천섹터

    ## 미국 기준금리 기준 추천 섹터
    {FredGraph}



    ## 

    
    """
)




llm = create_llm(model="openai/gpt-4o")
chain = ANALYSIS_PROMPT | llm | StrOutputParser()
result = chain.invoke({
    "FredGraph": FredGraph.invoke({}),
    # "GDPGraph": GDPGraph
})


if __name__ == "__main__":
    print(result)