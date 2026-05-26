from pathlib import Path, PurePosixPath
import os
import logging
from typing import Callable, Iterable
from .config import SUPPORTED_VERSION

# Can configure different level to output logging
logging.basicConfig(level=logging.WARNING)

def load_document(path: str) -> dict:
  
  """
  Read .md and .txt file and return a dictionary
  containing the content and metadata
  """
  

  def check_path_is_file(path: str):
    
    "Check whether path argument is a file"

    if Path(path).is_file():
      return path
    else: 
      raise TypeError("Path must be a valid file")
    
  def check_for_supported_filetypes(path: str):

    "Check if the file is supported"

    supported_files = SUPPORTED_VERSION

    if PurePosixPath(path).suffix in supported_files:
      return path
    raise NotImplementedError("File type is not supported in this version")

  def run_checks(path: str, check_list: Iterable[Callable[[str], str]]):
    
    # Look at the  type hint for check list, 
    # we can clearly read that its a an iterable (so list, or tuple)
    # that's callable and takes str as input argument and return str
    for check in check_list: 
      path = check(path)
    return path  


  def check_file_empty(path: str):

    "Check if the file empty"

    file_stats = os.stat(path)
    if not file_stats.st_size :
      raise ValueError("The file is empty")
    
    return path
  
  check_list = [check_path_is_file, 
                check_for_supported_filetypes, 
                check_file_empty]

  logging.info("Run checks to validate file path")
  result = run_checks(path, check_list)

  # If result passed then read the files
  logging.info("Checks completed, proceeding to open file")

  # Read the file 
  document_data = {}
  
  if result:
    with open(path, "r", encoding="utf-8") as f: 
      
      result = f.read()

      # Checks have been completed prior, data should be available
      document_data["content"] = result
      document_data["file_name"] = Path(path).name
      document_data["file_extension"] = PurePosixPath(path).suffix
      document_data["word_count"] = len(result.split())
      document_data["line_count"] = len(result.splitlines())


    
    return document_data


if __name__ == "__main__":

  city_that_remembered_rain = "data/sample/the_city_that_remembered_rain.md"
  the_library_at_the_edge_of_tomorrow = "data/sample/the_library_at_the_edge_of_tomorrow.txt"
  the_lantern_archive_novel = "data/sample/the_lantern_archive_novel.pdf"
  empty_novel = "data/sample/empty.txt"
  broken_path = "hello" 
  
  result = load_document(city_that_remembered_rain)
  print(result)

  
