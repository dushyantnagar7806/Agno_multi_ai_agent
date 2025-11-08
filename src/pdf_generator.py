# pdf_generator.py

from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.pagesizes import letter
import os


def generate_financial_pdf(input_text: str, pdf_path: str = "output/financial_report.pdf"):
    """
    Generate a paginated, wrapped PDF file from the AI-generated financial report text.

    Args:
        input_text (str): The financial report text to write into the PDF.
        pdf_path (str): Output path for the generated PDF.
    """

    # Ensure output directory exists
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    # Create ReportLab canvas
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Page and margin configuration
    margin_x = 40
    margin_top = 750
    line_height = 16
    max_width = 520  # page width minus margins

    y = margin_top

    # Write content with text wrapping and page breaks
    for line in input_text.split("\n"):
        wrapped_lines = simpleSplit(line, "Helvetica", 12, max_width)
        for wrapped_line in wrapped_lines:
            c.drawString(margin_x, y, wrapped_line)
            y -= line_height
            if y < 40:  # new page if running out of space
                c.showPage()
                c.setFont("Helvetica", 12)
                y = margin_top

    c.save()
    print(f"PDF successfully generated at: {pdf_path}")
