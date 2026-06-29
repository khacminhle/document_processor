from pathlib import Path, PurePosixPath
import os
from typing import Callable, Iterable, Any
from .config import SUPPORTED_VERSION

supported_files = SUPPORTED_VERSION


# def load_document(path: str) -> dict:
  
#   """
#   Read .md and .txt file and return a dictionary
#   containing the content and metadata

#   Args: 
#     path: Path to the document file

#   Returns:
#     A dictionary containing:

#       content: The full text content of the file.
#       file_name: The file name, without extension.
#       file_extension: The file extension, such as ".md" or ".txt".
#       word_count: Number of words in the document.
#       line_count: Number of lines in the document.

#   Raises:
#     TypeError: If path does not point to a valid file.
#     NotImplementedError: If the file extension is unsupported.
#     ValueError: If the file is empty.
#   """
  

#   def check_path_is_file(path: str):
    
#     "Check whether path argument is a file"

#     if Path(path).is_file():
#       return path
#     else: 
#       raise TypeError("Path must be a valid file")
    
#   def check_for_supported_filetypes(path: str):

#     "Check if the file is supported"

#     supported_files = SUPPORTED_VERSION

#     if PurePosixPath(path).suffix in supported_files:
#       return path
#     raise NotImplementedError("File type is not supported in this version")

#   def run_checks(path: str, check_list: Iterable[Callable[[str], str]]):
    
#     # Look at the  type hint for check list, 
#     # we can clearly read that its a an iterable (so list, or tuple)
#     # that's callable and takes str as input argument and return str
#     for check in check_list: 
#       path = check(path)
#     return path  


#   def check_file_empty(path: str):

#     "Check if the file empty"

#     file_stats = os.stat(path)
#     if not file_stats.st_size :
#       raise ValueError("The file is empty")
    
#     return path
  
#   check_list = [check_path_is_file, 
#                 check_for_supported_filetypes, 
#                 check_file_empty]

#   result = run_checks(path, check_list)

#   # Read the file 
#   document_data = {}
  
#   if result:
#     with open(path, "r", encoding="utf-8") as f: 
      
#       result = f.read()

#       # Checks have been completed prior, data should be available
#       document_data["content"] = result
#       document_data["file_name"] = Path(path).stem
#       document_data["file_extension"] = PurePosixPath(path).suffix
#       document_data["word_count"] = len(result.split())
#       document_data["line_count"] = len(result.splitlines())
      
#     return document_data


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



  
