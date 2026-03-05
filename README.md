# Unique Names Data

A [Frictionless Data Package](https://datapackage.org/) containing curated word lists for generating unique, memorable names.

## Overview

This repository provides language-agnostic word lists that can be consumed by any name generator implementation (Julia, JavaScript, Python, etc.). The data is organized according to the Frictionless Data Package v2 specification.

## Dictionaries

| Resource | File | Min. Entries | Description | Examples |
|----------|------|--------------|-------------|----------|
| `adjectives` | [data/adjectives.csv](data/adjectives.csv) | 120 | General adjectives (traits, qualities) | Swift, Gentle, Bold, Quantum |
| `colors` | [data/colors.csv](data/colors.csv) | 50 | Color names | Crimson, Azure, Emerald, Golden |
| `animals` | [data/animals.csv](data/animals.csv) | 100 | Animal species | Falcon, Otter, Lynx, Pangolin |
| `celestial` | [data/celestial.csv](data/celestial.csv) | 50 | Space and astronomy terms | Nebula, Pulsar, Comet, Quasar |
| `nature` | [data/nature.csv](data/nature.csv) | 50 | Natural elements and phenomena | Glacier, Ember, Cascade, Fjord |
| `science` | [data/science.csv](data/science.csv) | 50 | Scientific terms | Photon, Prism, Quark, Helix |
| `numbers` | [data/numbers.csv](data/numbers.csv) | 100 | Numeric strings (0-99) | 0, 1, 42, 99 |

## Default Name Grammar

The recommended default grammar for generating names is `[adjectives, colors, animals]`, producing names like:

- **Bold Crimson Falcon**
- **Gentle Azure Otter**
- **Swift Golden Eagle**

This is a suggested configuration for consuming applications—the data package itself is grammar-agnostic.

## Usage

### Direct CSV Access

Each word list is a simple CSV file with a `word` column and an optional `category` column:

```csv
word,category
Swift,physical
Gentle,personality
Bold,personality
```

### Using the Data Package Descriptor

The `datapackage.json` file describes all resources and their schemas:

```python
# Python example using frictionless-py
from frictionless import Package

package = Package("datapackage.json")
adjectives = package.get_resource("adjectives")
for row in adjectives.read_rows():
    print(row["word"])
```

```julia
# Julia example using CSV.jl and JSON3.jl
using JSON3, CSV, DataFrames

pkg = JSON3.read(read("datapackage.json", String))
adjectives_path = pkg.resources[1].path
df = CSV.read(adjectives_path, DataFrame)
```

```javascript
// JavaScript example
import { readFileSync } from 'fs';
import { parse } from 'csv-parse/sync';

const pkg = JSON.parse(readFileSync('datapackage.json', 'utf-8'));
const adjectivesResource = pkg.resources.find(r => r.name === 'adjectives');
const csv = readFileSync(adjectivesResource.path, 'utf-8');
const records = parse(csv, { columns: true });
```

## File Format

All CSV files follow these conventions:

- **Encoding:** UTF-8 without BOM
- **Header:** First row contains column names
- **Columns:** `word` (required), `category` (optional)
- **Line endings:** Unix-style (LF)

## Content Moderation

This repository maintains a blocklist (`data/blocklist.csv`) of words that have been excluded due to inappropriate content. The CI validates that:

1. No blocklisted words appear in any dictionary
2. Generated name combinations don't form offensive phrases
3. Words are checked against external profanity reference lists

See [CONTRIBUTING.md](CONTRIBUTING.md) for the word curation policy and how to report inappropriate content.

## Versioning

This data package follows [Semantic Versioning](https://semver.org/):

- **MAJOR:** Breaking changes to schema or removal of dictionaries
- **MINOR:** New dictionaries or significant word additions
- **PATCH:** Word corrections, small additions, or metadata updates

## Release Workflow

This repository uses GitHub Actions to automate the release process. A new release is created automatically when a commit on the `main` branch includes a specific message format.

To trigger a new release:

1.  **Update Version:** Increment the `version` property in the `datapackage.json` file according to Semantic Versioning rules.
2.  **Commit Changes:** Commit the updated `datapackage.json` with a commit message containing `chore(release):`.

    ```bash
    git commit -m "chore(release): bump version to X.Y.Z"
    ```

This will trigger a workflow that:
- Creates a Git tag corresponding to the new version.
- Publishes a GitHub Release with the tag.
- Attaches a `unique-names-data.zip` archive containing the full data package as a release asset.

## License

This work is dedicated to the public domain under [CC0 1.0 Universal](LICENSE).

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Adding new words
- Proposing new dictionaries
- Reporting inappropriate content
- The review process

## Related Projects

- [unique-names-generator](https://github.com/andreasonny83/unique-names-generator) - JavaScript name generator (npm)
- [Issue #82](https://github.com/andreasonny83/unique-names-generator/issues/82) - Proposal to split data from code
- [Issue #66](https://github.com/andreasonny83/unique-names-generator/issues/66) - Content moderation discussion

## Acknowledgments

This data package is designed to serve as a canonical data source for name generation across multiple ecosystems, addressing the need for language-agnostic, well-curated word lists with proper content moderation.
