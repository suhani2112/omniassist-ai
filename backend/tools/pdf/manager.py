import os
import uuid
from datetime import datetime

from backend.tools.pdf.models import PDFDocument


class PDFManager:

    def __init__(self):

        self.documents = {}

        self.upload_folder = "backend/storage/uploads"

        os.makedirs(self.upload_folder, exist_ok=True)

    def register_document(self, filepath: str):

        filename = os.path.basename(filepath)

        document = PDFDocument(
            document_id=str(uuid.uuid4()),
            filename=filename,
            filepath=filepath,
            upload_time=datetime.now()
        )

        self.documents[document.document_id] = document

        return document

    def get_document(self, document_id: str):

        return self.documents.get(document_id)

    def list_documents(self):

        return list(self.documents.values())

    def delete_document(self, document_id: str):

        if document_id in self.documents:
            del self.documents[document_id]
            return True

        return False