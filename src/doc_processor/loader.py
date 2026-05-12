from pathlib import Path

city_that_remembered_rain = "data/sample/the_city_that_remembered_rain.md"
the_library_at_the_edge_of_tomorrow = "data/sample/the_library_at_the_edge_of_tomorrow.txt"


def load_novel_in_md(path: str) -> str:
  
  """
  Read .md and .txt file and return string of text
  """
  
  with open(path, "r") as f: 
    result = f.read()
  return result

if __name__ == "__main__": 
  
  result = load_novel_in_md(city_that_remembered_rain)
  print(result)
  print("Finish loading the result")

  
