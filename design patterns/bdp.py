"""
This script demonstrates the Builder design pattern for creating different types of documents.
"""
class DocumentBuilder:
    """
    Abstract builder interface for creating documents.
    """
    def set_title(self, title):
        """
        Set the title of the document.

        Parameters:
        title (str): The title of the document.

        Returns:
        None
        """
        pass

    def add_content(self, content):
        """
        Add content to the document.

        Parameters:
        content (str): The content to be added.

        Returns:
        None
        """
        pass

    def build(self):
        """
        Build and return the finalized document.

        Returns:
        str: The finalized document.
        """
        pass

# Concrete builder classes
class PDFDocumentBuilder(DocumentBuilder):
    """
    Concrete builder class for creating PDF documents.
    """
    def __init__(self):
        self.document = "PDF Document\n"

    def set_title(self, title):
        self.document += f"Title: {title}\n"

    def add_content(self, content):
        self.document += f"Content: {content}\n"

    def build(self):
        return self.document

class HTMLDocumentBuilder(DocumentBuilder):
    """
    Concrete builder class for creating HTML documents.
    """
    def __init__(self):
        self.document = "<html><head><title></title></head><body>"

    def set_title(self, title):
        self.document = self.document.replace("<title></title>", f"<title>{title}</title>")

    def add_content(self, content):
        self.document += f"<p>{content}</p>"

    def build(self):
        return self.document + "</body></html>"

# Director class
class DocumentDirector:
    """
    Director class for constructing documents using a specified builder.
    """
    def __init__(self, builder):
        self.builder = builder

    def construct(self, title, content):
        """
        Construct a document using the specified title and content.

        Parameters:
        title (str): The title of the document.
        content (str): The content of the document.

        Returns:
        str: The finalized document.
        """
        self.builder.set_title(title)
        self.builder.add_content(content)
        return self.builder.build()

# Client code
pdf_builder = PDFDocumentBuilder()
html_builder = HTMLDocumentBuilder()

pdf_director = DocumentDirector(pdf_builder)
html_director = DocumentDirector(html_builder)

pdf_document = pdf_director.construct("PDF Document", "This is a PDF document.")
html_document = html_director.construct("HTML Document", "This is an HTML document.")

print(pdf_document)
print(html_document)
