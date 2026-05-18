from doc_processor.loader import load_document
import pytest

# Test variables
md_book = "Sample md book"
txt_book = "Sample txt book"
pdf_book = "Sample pdf book"

def test_loader_md_file(tmp_path): 

  tmp_dir = tmp_path / "sub" # sub here means subdirectory
  tmp_dir.mkdir() # Make dir out of this temp path

  # Temporarily create test file
  
  # Create md file
  tmp_md_file = tmp_dir / "test_book.md" # File path
  tmp_md_file.write_text(md_book, encoding="utf-8") 

  assert load_document(tmp_md_file) == md_book

  
def test_loader_txt_file(tmp_path):
  
  # Create txt file
  tmp_dir = tmp_path / "sub" # sub here means subdirectory
  tmp_dir.mkdir()

  tmp_txt_file = tmp_dir / "test_book.txt" 
  tmp_txt_file.write_text(txt_book, encoding="utf-8")
  
  assert load_document(tmp_txt_file) == txt_book

def test_loader_pdf_file(tmp_path): 

  # Create pdf file
  tmp_dir = tmp_path / "sub" # sub here means subdirectory
  tmp_dir.mkdir()
  
  tmp_pdf_file = tmp_dir / "test_book.pdf"
  tmp_pdf_file.write_text(pdf_book, encoding="utf-8")

  # Reading pdf file should raise an exception
  with pytest.raises(NotImplementedError):
    load_document(tmp_pdf_file) 
  






  