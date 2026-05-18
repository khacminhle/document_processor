from pathlib import Path
import frontmatter
from .loader import load_document

city_that_remembered_rain = "data/sample/the_city_that_remembered_rain.md"
the_library_at_the_edge_of_tomorrow = "data/sample/the_library_at_the_edge_of_tomorrow.txt"
the_lantern_archive_novel = "data/sample/the_lantern_archive_novel.pdf"
empty_novel = "data/sample/empty.txt"
broken_path = "hello" 

def extract_metadata(text: str) -> dict:
  post = frontmatter.loads(text)
  return post.metadata



if __name__ == "__main__":
  text = load_document(city_that_remembered_rain) 
  post = extract_metadata(text)
  print(post)

