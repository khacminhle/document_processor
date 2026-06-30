# document_processor

A small Python service for turning text documents into structured JSON. It accepts Markdown (`.md`) and plain text (`.txt`) files, extracts basic metadata, splits the document into overlapping chunks, and returns the processed result.

The main local entry point is a FastAPI app in `api/main.py`.

## What it does

- Validates uploaded `.md` and `.txt` files
- Reads document text and basic file metadata
- Extracts front matter fields such as `author` and `genre`
- Splits text into word chunks using the defaults in `src/doc_processor/config.py`
- Returns JSON containing `metadata` and `chunks`

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

- Supported input files are `.md` and `.txt`.
- Default chunking uses 10 words per chunk with a 2-word overlap.
- The older `main.py` CLI is still present, but the current loader is designed around uploaded files for the API flow.
