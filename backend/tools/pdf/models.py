from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class PDFPage:
    page_number: int
    text: str


@dataclass
class PDFChunk:
    chunk_id: str
    page_number: int
    text: str


@dataclass
class PDFDocument:

    document_id: str
    filename: str
    filepath: str
    upload_time: datetime

    total_pages: int = 0

    pages: List[PDFPage] = field(default_factory=list)

    chunks: List[PDFChunk] = field(default_factory=list)

    summary: str = ""

    metadata: dict = field(default_factory=dict)