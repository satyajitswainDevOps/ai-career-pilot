from pathlib import Path

import fitz  # PyMuPDF
from docx import Document


class ResumeParser:

    @staticmethod
    def extract_text(file_path: str) -> str:
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return ResumeParser._extract_pdf(file_path)

        if extension == ".docx":
            return ResumeParser._extract_docx(file_path)

        return ""

    @staticmethod
    def _extract_pdf(file_path: str) -> str:
        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    @staticmethod
    def _extract_docx(file_path: str) -> str:
        document = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )