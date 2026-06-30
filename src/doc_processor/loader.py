from pathlib import Path, PurePosixPath
from typing import Callable, Iterable, Any
from .config import SUPPORTED_VERSION

supported_files = SUPPORTED_VERSION

async def load_document(file_obj):
  
  """
  Read .md and .txt file from an uploaded file object and return a dictionary
  containing the content and metadata

  Args: 
  file_obj: An uploaded file object (e.g., from a request)

  Returns:
  A dictionary containing:

  content: The full text content of the file.

  file_name: The file name, without extension.

  file_extension: The file extension, such as ".md" or ".txt".

  word_count: Number of words in the document.

  line_count: Number of lines in the document.

  Raises:

  TypeError: If the file object is not valid.
  NotImplementedError: If the file extension is unsupported.
  ValueError: If the file is empty.
  """
  
  # Check if the file object is valid
  if not hasattr(file_obj, 'read'):
      raise TypeError("Invalid file object provided")

  # Check if file is supported
  file_extension = PurePosixPath(file_obj.filename).suffix 
  if file_extension not in supported_files:
    raise NotImplementedError("File type is not supported in this version")

  # Read the file content
  content = await file_obj.read() #file_obj is a co routine, we gotta await it
  content = content.decode("utf-8")

  # Check if the file is empty
  if not content:
      raise ValueError("The file is empty")

  # Prepare the result dictionary
  document_data = {
      "content": content,
      "file_name": Path(file_obj.filename).stem,
      "file_extension": file_extension,
      "word_count": len(content.split()),
      "line_count": len(content.splitlines())
  }

  return document_data



  
