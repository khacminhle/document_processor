import frontmatter
from .loader import load_document
import logging

city_that_remembered_rain = "data/sample/the_city_that_remembered_rain.md"
the_library_at_the_edge_of_tomorrow = "data/sample/the_library_at_the_edge_of_tomorrow.txt"
the_lantern_archive_novel = "data/sample/the_lantern_archive_novel.pdf"
empty_novel = "data/sample/empty.txt"
broken_path = "hello" 

# Configure logging
logging.basicConfig(level=logging.WARNING)

def extract_metadata(text: str) -> dict:
  
  # Try to extract metadata
  post = frontmatter.loads(text)

  # If metadata is empty, raise warning to console
  if not post.metadata :
    logging.warning("Metadata not available for this file")

  return post.metadata



if __name__ == "__main__":
  text = load_document(the_library_at_the_edge_of_tomorrow) 
  post = extract_metadata(text)
  print(post)


