# Data Directory

This directory is intended for storing datasets used in development, testing, and experimentation.  
**Important:** raw data should **not** be committed to version control (Git) — only small sample datasets or metadata should be tracked.

## Recommended Structure

data/
├── raw/ # Original, immutable data (never edited manually)
├── processed/ # Cleaned, transformed, or preprocessed datasets
└── external/ # Data from third-party sources or APIs

## Guidelines

- **Do not commit large files**: use `.gitignore` to exclude raw/processed data.
- If needed, use [Git LFS](https://git-lfs.com/) or external storage (S3, GCS, etc.).
- Provide small, anonymized, or synthetic sample data for testing purposes.
- Document the source and format of each dataset in a `README.md` inside its subdirectory.

## Example

If you had a dataset `users.csv` from a public API:
data/
├── raw/
│ └── users.csv # original download
├── processed/
│ └── users_clean.csv # cleaned version (scripts applied)
└── external/
└── users_schema.json # metadata / schema definition
