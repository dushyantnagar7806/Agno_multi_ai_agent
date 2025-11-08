import os
from universal_reader_service import UniversalReaderService
from finance_team_agents import finance_team
from pdf_generator import generate_financial_pdf

def run_financial_analysis(file_path: str):
    """
    Full flow:
    1. Reads file using UniversalReaderService
    2. Passes content to finance_team
    3. Saves the AI-generated output as a PDF
    """
    print(f"Reading file: {file_path}")

    reader = UniversalReaderService()
    docs = reader.read(file_path)
    file_context = reader.extract_text(docs)

    if not file_context.strip():
        print("No readable text found in file.")
        return

    print(f" Extracted {len(file_context)} characters")

    prompt = f"""
    You are a collaborative financial analysis team (Data Analyst, Risk Evaluator, Market Strategist).
    Analyze the following document and produce a structured report including:
    - Financial summary
    - Risks & mitigations
    - Actionable strategic recommendations

    File Context:
    {file_context[:8000]}
    """

    print("\nRunning finance agents...\n")
    result = finance_team.run(prompt.strip())
    output_text = result.output_text

    # Save PDF
    pdf_path = "output/final_financial_report.pdf"
    generate_financial_pdf(output_text, pdf_path)
    print(f"\n Final financial report saved to: {pdf_path}\n")

if __name__ == "__main__":
    print("Agno Multi-Agent Financial Analyzer")
    print("Supported formats: CSV, XLSX, PDF, DOCX, JSON, PPTX, TXT")
    file_path = input("Enter file path to analyze: ").strip()
    if os.path.exists(file_path):
        run_financial_analysis(file_path)
    else:
        print("File not found. Please check the path.")
