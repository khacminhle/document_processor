# document_processor

A small Python project for turning text documents into structured JSON. It accepts Markdown (`.md`) and plain text (`.txt`) files, extracts basic metadata, splits the document into overlapping chunks, and writes the processed result to disk.

There are two ways to use it locally:

- a command-line interface in `cli.py`
- a FastAPI app in `src/api/main.py`

## What it does

- Validates uploaded `.md` and `.txt` files
- Reads document text and basic file metadata
- Extracts front matter fields such as `author` and `genre`
- Splits text into word chunks using the defaults in `src/doc_processor/config.py`
- Returns JSON containing `metadata` and `chunks`

## CLI Usage

The CLI processes a single local file and saves the structured JSON output under `data/output/`.

### Install dependencies

```bash
uv sync
```

### Run the CLI

```bash
uv run python cli.py path/to/document.md
```

You can also pass a `.txt` file:

```bash
uv run python cli.py path/to/document.txt
```

### Supported input

- `.md`
- `.txt`

### Output

- The CLI writes a JSON file to `data/output/`.
- The output filename is based on the input filename, for example `my_doc.json`.
- If a file with the same name already exists, the CLI creates a copy with a suffix like `_copy_1`.

### What the CLI includes in the JSON

- `metadata`
- `chunks`
- `author` and `genre` extracted from front matter when present

### Example

```bash
uv run python cli.py ./notes/example.md
```

This will print the saved JSON path after processing finishes.

## Requirements

- Python `>= 3.14.4`
- `uv` for dependency management

## Start locally

Install dependencies:

```bash
uv sync
```

Run the API:

```bash
uv run python api/switch_api.py run
```

The server starts at:

```text
http://localhost:8000
```

Check that it is running:

```bash
curl http://localhost:8000/health-check
```

Upload a document:

```bash
curl -X POST http://localhost:8000/upload-document \
  -F "file=@path/to/document.md"
```

## Project structure

```text
api/                  FastAPI app and local server runner
src/doc_processor/    document loading, metadata, chunking, and writing logic
src/services/         API-facing document ingestion flow
tests/                pytest tests
```

## Run tests

```bash
uv run pytest
```

## Notes

- Default chunking uses 10 words per chunk with a 2-word overlap.
- The CLI and API share the same document loading, metadata extraction, chunking, and JSON writing logic.
