from pathlib import Path, PurePosixPath
import asyncio
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
  if hasattr(file_obj, "read"):
      logger.info("Reading from uploaded file object")
      if not hasattr(file_obj, "filename"):
          logger.info("Processed invalid file object")
          raise TypeError("Invalid file object provided")

      file_name = Path(file_obj.filename).stem
      file_extension = PurePosixPath(file_obj.filename).suffix
      content = await file_obj.read()
      content = content.decode("utf-8")
  
  # Support CLI methid
  else:
      path = Path(file_obj)
      logger.info("Reading from local file path")
      file_name = path.stem
      file_extension = path.suffix
      content = await asyncio.to_thread(path.read_text, encoding="utf-8")

  logger.info("Checking if file type is supported")
  if file_extension not in supported_files:
    logger.warning(f"{file_extension} not supported")
    raise NotImplementedError(f"{file_extension} is not supported")


  logger.info("Checking if file content is not empty")
  # Check if the file is empty
  if not content:
    logger.warning("File is empty")
    raise ValueError("The file is empty")

  logger.info("Preparing file content data")
  # Prepare the result dictionary
  document_data = {
      "content": content,
      "file_name": file_name,
      "file_extension": file_extension,
      "word_count": len(content.split()),
      "line_count": len(content.splitlines())
  }


  logger.info(
      "Loaded document name: %s, total of %s words, %s lines",
      document_data["file_name"],
      document_data["word_count"],
      document_data["line_count"],
  )

  return document_data



  
