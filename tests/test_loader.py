import pytest
from doc_processor.loader import load_document

class FakeUploadFile:

  def __init__(self, file_name, content):
    self.filename = file_name
    self._content = content

  async def read(self):
    return self._content

# Test whether the load function can return expected data
@pytest.mark.asyncio
async def test_load_document_func_happy_path():

  # Set up pytest for happy path
  file_name = "fake_document.md"
  content = "This is a fake document used for testing".encode("utf-8")

  fake_upload_file = FakeUploadFile(file_name=file_name, content=content)

  test_data = await load_document(fake_upload_file)

  assert test_data["content"] == "This is a fake document used for testing"
  assert test_data["file_name"] == "fake_document"
  assert test_data["file_extension"] == ".md"
  assert test_data["word_count"] == 8
  assert test_data["line_count"] == 1

# Test whether load function can raise TypeError when receiving abnormal object
@pytest.mark.asyncio
async def test_load_document_func_type_error():
  with pytest.raises(TypeError, match="Invalid file object provided"):
    await load_document(object())

# Test whether load function can raise NotImplementedError 
# when receiving unsupported file 
@pytest.mark.asyncio
async def test_load_document_func_not_implemented_error():
  file_name = "fake_document.docx"
  content = "This is a fake document used for testing".encode("utf-8")
  fake_upload_file = FakeUploadFile(file_name=file_name, content=content)

  with pytest.raises(NotImplementedError, match=r"\.docx is not supported"):
    await load_document(fake_upload_file)


# Test whether load function reject empty files 
@pytest.mark.asyncio
async def test_load_document_func_reject_empty_file():
  file_name = "fake_document.md"
  content = "".encode("utf-8")
  fake_upload_file = FakeUploadFile(file_name=file_name, content=content)

  with pytest.raises(ValueError, match="The file is empty"):
    await load_document(fake_upload_file)











 








  
