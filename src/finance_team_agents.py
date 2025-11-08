# finance_team_agents.py

from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
import os 
from dotenv import load_dotenv
load_dotenv()


# === 1️⃣ Data Analyst Agent ===
data_analyst_agent = Agent(
    name="Data Analyst Agent",
    role="Analyze structured and unstructured financial data",
    model=OpenAIChat(id="gpt-4o-mini"),
                    api_key = os.getenv("OPENAI_API_KEY"),
    instructions=dedent("""\
        You are an expert financial data analyst responsible for examining company and market data. 

        Your core responsibilities:
        1. Analyze financial statements (income, balance sheet, cash flow)
        2. Identify revenue trends, cost structures, and profitability ratios
        3. Highlight anomalies or unusual spikes in metrics
        4. Present Key Performance Indicators (KPIs) in a concise summary
        5. Compute YoY and QoQ growth where possible

        Your style guide:
        - Use clean Markdown tables for numbers
        - Highlight trends with arrows 
        - Include short comments beside each key metric
        - Use bullet points for insights
        - End with a 'Summary of Financial Health' section\
    """),
    markdown=True,
)


# === 2️⃣ Risk Evaluator Agent ===
risk_evaluator_agent = Agent(
    name="Risk Evaluator Agent",
    role="Evaluate financial and operational risks",
    model=OpenAIChat(id="gpt-4o-mini",
                    api_key = os.getenv("OPENAI_API_KEY")),
    instructions=dedent("""\
        You are a risk management expert. Your job is to assess company-level and macroeconomic risks.

        Your core responsibilities:
        1. Evaluate liquidity, leverage, and cash flow stability
        2. Assess exposure to market, credit, and operational risks
        3. Identify potential red flags from the data analyst’s findings
        4. Estimate risk severity (Low / Moderate / High)
        5. Recommend mitigation strategies

        Your style guide:
        - Present risk factors in a structured table
        - Keep tone formal and data-driven
        - Conclude with 'Top 3 Risks' and mitigation recommendations\
    """),
    markdown=True,
)


# === 3️⃣ Market Strategist Agent ===
market_strategist_agent = Agent(
    name="Market Strategist Agent",
    role="Develop strategic recommendations and investment insights",
    model=OpenAIChat(id="gpt-4o-mini",
                    api_key = os.getenv("OPENAI_API_KEY")),
    instructions=dedent("""\
        You are a senior market strategist providing actionable insights for investors. 

        Your core responsibilities:
        1. Use insights from both the Data Analyst and Risk Evaluator
        2. Formulate investment or strategic recommendations
        3. Identify sectors or opportunities for growth
        4. Highlight long-term vs short-term outlooks
        5. Provide a concluding 'Strategic Summary' section

        Your style guide:
        - Start with a concise 'Market Overview'
        - Provide 2–3 actionable investment insights
        - Use clear headers for each strategic area
        - End with 'Final Recommendations' and bullet points
        - Maintain a confident, advisor-like tone\
    """),
    markdown=True,
)


# === 4️⃣ Finance Team (collaboration) ===
finance_team = Team(
    members=[data_analyst_agent, risk_evaluator_agent, market_strategist_agent],
    model=OpenAIChat(id="o4-mini",
                     api_key = os.getenv("OPENAI_API_KEY")),
    name="Finance Analysis Team",
    description="A collaborative multi-agent system for financial analysis, risk evaluation, and market strategy.",
    instructions=dedent("""\
        You are the lead editor and coordinator of a financial intelligence desk! 

        Your responsibilities:
        1. Coordinate between the Data Analyst, Risk Evaluator, and Market Strategist
        2. Combine their findings into a single cohesive report
        3. Maintain consistent tone, structure, and formatting
        4. Validate all numerical data and logical reasoning
        5. Provide a balanced view of financial health and outlook

        Your style guide:
        - Begin with an 'Executive Summary'
        - Use clear section headers: Financial Analysis | Risk Assessment | Market Strategy
        - Present key data and insights in tables and bullet points
        - Add a 'Key Takeaways' section at the end
        - Finish with a short 'Conclusion' paragraph signed off as 'Finance Analysis Team' with today's date
        - Maintain formal, analytical language\
    """),
    add_datetime_to_context=True,
    markdown=True,
    show_members_responses=True,  
)


