import os
import sys


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Agent.Prompt.Prompts import *


def recommend_sectors_chain(llm, macro_data, sector_data, prompt):

    chain = prompt | llm | recommend_sectors_output_parser
    result = chain.invoke({
        "macro_data": macro_data,
        "sector_data": sector_data
    })
    
    return result


def summarize_data_chain(llm, data_package, prompt):
    chain = prompt | llm | summary_output_parser
    result = chain.invoke({
        "data_package": data_package
    })
    return result


def evaluation_chain(llm, summary_data, now_macro_data, now_sector_data, prompt):
    chain = prompt | llm | backtest_output_parser
    result = chain.invoke({
        "summary_data": summary_data,
        "now_macro_data": now_macro_data,
        "now_sector_data": now_sector_data
    })
    return result


def feedback_analysis_chain(llm, summary_data, evaluation_response, prompt):
    chain = prompt | llm | feedback_output_parser
    result = chain.invoke({
        "summary_data": summary_data,
        "evaluation_response": evaluation_response
    })
    return result


def final_summary_chain(llm, result, prompt):
    chain = prompt | llm | final_summary_output_parser
    result = chain.invoke({
        "result": result
    })
    return result