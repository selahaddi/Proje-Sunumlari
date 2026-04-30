import os
import glob
import fitz  # PyMuPDF
from PIL import Image
import io

os.makedirs('project_slides', exist_ok=True)

pdf_files = glob.glob('*_Proje_Detayi.pdf')

for pdf_path in pdf_files:
    project_name = pdf_path.replace('.pdf', '')
    project_dir = os.path.join('project_slides', project_name)
    os.makedirs(project_dir, exist_ok=True)
    
    print(f"Processing {pdf_path}...")
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            # High resolution rendering
            zoom = 2.0
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            
            # Convert to PIL Image
            img = Image.open(io.BytesIO(pix.tobytes()))
            
            # Save as webp for smaller size and faster loading
            output_path = os.path.join(project_dir, f"page_{page_num + 1}.webp")
            img.save(output_path, "WEBP", quality=80)
            
        print(f"Saved {len(doc)} pages for {project_name}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

print("All PDFs processed.")
