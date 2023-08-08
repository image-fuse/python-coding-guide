# Abstract builder interface
class DocumentBuilder:
    def set_title(self, title):
        pass
    
    def add_content(self, content):
        pass
    
    def build(self):
        pass

# Concrete builder classes
class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = "PDF Document\n"
        
    def set_title(self, title):
        self.document += f"Title: {title}\n"
        
    def add_content(self, content):
        self.document += f"Content: {content}\n"
        
    def build(self):
        return self.document

class HTMLDocumentBuilder(DocumentBuilder):
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
    def __init__(self, builder):
        self.builder = builder
        
    def construct(self, title, content):
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
