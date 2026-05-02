import os

pdf_dir = r"C:\Users\n.anand\Desktop\python file\PlanoDrives\pdf"
output_file = r"C:\Users\n.anand\Desktop\python file\PlanoDrives\pdf_text.txt"

def extract_text():
    extracted = False
    
    # Try PyMuPDF
    try:
        import fitz
        with open(output_file, 'w', encoding='utf-8') as f:
            for filename in os.listdir(pdf_dir):
                if filename.lower().endswith('.pdf'):
                    f.write(f"--- {filename} ---\n")
                    doc = fitz.open(os.path.join(pdf_dir, filename))
                    for page in doc:
                        f.write(page.get_text() + "\n")
                    f.write("\n\n")
        print("Successfully extracted using PyMuPDF (fitz)")
        return True
    except ImportError:
        pass

    # Try PyPDF2
    try:
        from PyPDF2 import PdfReader
        with open(output_file, 'w', encoding='utf-8') as f:
            for filename in os.listdir(pdf_dir):
                if filename.lower().endswith('.pdf'):
                    f.write(f"--- {filename} ---\n")
                    reader = PdfReader(os.path.join(pdf_dir, filename))
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            f.write(text + "\n")
                    f.write("\n\n")
        print("Successfully extracted using PyPDF2")
        return True
    except ImportError:
        pass
        
    print("Could not extract text. Please install PyMuPDF ('pip install pymupdf') or PyPDF2 ('pip install PyPDF2')")
    return False

if __name__ == "__main__":
    extract_text()
