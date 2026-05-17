from doc_processor.loader import load_novel_in_md
import pytest

"""
Terminology 
- Assert means that the output must equal to this output
"""

"""
Create a tmp directory
with tmp files 

And test if its able to read it or raise exception
"""
md_book = "Sample md book"
txt_book = "Sample txt book"
pdf_book = "Sample pdf book"

def test_reading_md_txt_files(tmp_path): 
  
  tmp_dir = tmp_path / "sub" # sub here means subdirectory
  tmp_dir.mkdir() # Make dir out of this temp path

  # Temporarily create test file
  
  # Create md file
  tmp_md_file = tmp_dir / "test_book.md" # File path
  tmp_md_file.write_text(md_book, encoding="utf-8") 

  # Create txt file 
  tmp_txt_file = tmp_dir / "test_book.txt" 
  tmp_txt_file.write_text(txt_book, encoding="utf-8")

  # Create pdf file =
  from fpdf import FPDF

  tmp_pdf_file = tmp_dir / "test_book.pdf" # File path

  pdf = FPDF()
  pdf.add_page()
  pdf.set_font('helvetica', size=12)

  pdf.cell(text=pdf_book)
  pdf.output(tmp_pdf_file)



  # Test loader to read file path and validate if loader able to read content
  assert load_novel_in_md(tmp_md_file) == md_book
  assert load_novel_in_md(tmp_txt_file) == txt_book

  # Reading pdf file should raise an exception
  with pytest.raises(NotImplementedError):
    load_novel_in_md(tmp_pdf_file)

  






  