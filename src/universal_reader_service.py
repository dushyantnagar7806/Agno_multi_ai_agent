import os
from pathlib import Path
from typing import Union, List

# Agno document readers
from agno.knowledge.reader.csv_reader import CSVReader
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.reader.docx_reader import DocxReader
from agno.knowledge.reader.pptx_reader import PPTXReader
from agno.knowledge.reader.json_reader import JSONReader
from agno.knowledge.reader.text_reader import TextReader

# Optional: enable Excel support if available
try:
    from agno.knowledge.reader.excel_reader import ExcelReader
    EXCEL_SUPPORTED = True
except ImportError:
    ExcelReader = None
    EXCEL_SUPPORTED = False


class UniversalReaderService:
    """A universal document ingestion service using Agno readers."""

    def __init__(self):
        """Initialize all supported readers."""
        self.readers = {
            ".pdf": PDFReader(),
            ".csv": CSVReader(),
            ".docx": DocxReader(),
            ".pptx": PPTXReader(),
            ".json": JSONReader(),
            ".txt": TextReader(),
        }

        if EXCEL_SUPPORTED:
            self.readers[".xlsx"] = ExcelReader()
            self.readers[".xls"] = ExcelReader()

    def read(self, file_path: Union[str, Path]) -> List:
        """
        Detects file type and reads the content using the correct Agno reader.

        Args:
            file_path: Path to the input file (string or Path object)

        Returns:
            List of Document objects, each with a `.content` property.
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        ext = path.suffix.lower()

        if ext not in self.readers:
            raise ValueError(f"Unsupported file type: {ext}")

        reader = self.readers[ext]
        print(f"Using reader: {reader.__class__.__name__} for {path.name}")

        try:
            docs = reader.read(path)
            if not docs:
                print(f" No content extracted from {path.name}")
            return docs
        except Exception as e:
            print(f"Error reading {path.name} with {reader.__class__.__name__}: {e}")
            return []

    def extract_text(self, docs: List) -> str:
        """
        Concatenates text from Agno Document objects into a single string.

        Args:
            docs: List of Agno document chunks

        Returns:
            Combined text content as a string
        """
        content = ""
        for doc in docs:
            if hasattr(doc, "content"):
                content += doc.content.strip() + "\n"
        return content.strip()


