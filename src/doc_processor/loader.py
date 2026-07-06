from pathlib import Path, PurePosixPath
from .config import SUPPORTED_VERSION
import logging 

logger = logging.getLogger(__name__)

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
  
  logger.info("Document process started")
  # Check if the file object is valid
  if not hasattr(file_obj, 'read'):
      logger.info("Processed invalid file object")
      raise TypeError("Invalid file object provided")

  
  logger.info("Checking if file type is supported")
  # Check if file is supported
  file_extension = PurePosixPath(file_obj.filename).suffix 
  if file_extension not in supported_files:
    logger.warning(f"{file_extension} not supported i")
    raise NotImplementedError(f"{file_extension} is not supported")

  
  logger.info("Reading file content")
  # Read the file content
  content = await file_obj.read() #file_obj is a co routine, we gotta await it
  content = content.decode("utf-8")


  logger.info("Checking if file content is not empty")
  # Check if the file is empty
  if not content:
    logger.warning("File is empty")
    raise ValueError("The file is empty")

  logger.info("Preparing file content data")
  # Prepare the result dictionary
  document_data = {
      "content": content,
      "file_name": Path(file_obj.filename).stem,
      "file_extension": file_extension,
      "word_count": len(content.split()),
      "line_count": len(content.splitlines())
  }


  logger.info(f"Loaded document name: {document_data["file_name"]}, total of {document_data["word_count"]} words, {document_data["line_count"]} lines")

  return document_data



  
