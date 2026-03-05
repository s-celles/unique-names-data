# Contributing to Unique Names Data

Thank you for your interest in contributing! This document outlines the process for adding words, proposing new dictionaries, and reporting inappropriate content.

## Table of Contents

- [Word Curation Policy](#word-curation-policy)
- [Adding New Words](#adding-new-words)
- [Proposing New Dictionaries](#proposing-new-dictionaries)
- [Reporting Inappropriate Content](#reporting-inappropriate-content)
- [Review Process](#review-process)
- [Technical Guidelines](#technical-guidelines)

## Word Curation Policy

### Selection Criteria

Words should be:

1. **Memorable** — Easy to remember and pronounce
2. **Positive or Neutral** — Evokes pleasant or neutral associations
3. **Universal** — Understandable across cultures (primarily English)
4. **Safe** — Free from offensive, discriminatory, or inappropriate connotations
5. **Distinct** — Different enough from other words to avoid confusion

### Exclusion Criteria

Words will be rejected or removed if they:

- Are profane, vulgar, or obscene
- Have sexual connotations
- Are discriminatory (racial, ethnic, gender, religious, etc.)
- Promote violence or harm
- Form offensive phrases when combined with other dictionary words
- Are too similar to existing words (causing confusion)
- Are trademarks or copyrighted terms
- Are ambiguous in problematic ways

## Adding New Words

### Process

1. **Fork** the repository
2. **Edit** the appropriate CSV file in the `data/` directory
3. **Add** your word(s) in alphabetical order
4. **Include** an appropriate category value
5. **Submit** a pull request

### Example

Adding "Majestic" to adjectives:

```csv
word,category
Majestic,personality
```

### Checklist Before Submitting

- [ ] Word is spelled correctly
- [ ] Word fits the dictionary's theme
- [ ] Category is appropriate
- [ ] Word is not already in the list (case-insensitive)
- [ ] Word is not in the blocklist
- [ ] Word doesn't form offensive combinations with other dictionaries

## Proposing New Dictionaries

New dictionaries can be proposed via a GitHub Issue. Include:

1. **Dictionary name** (e.g., `mythology`, `verbs`, `places`)
2. **Description** and use case
3. **Initial word list** with at least 30 entries
4. **Categories** that words would belong to

### Example Proposal

```markdown
## New Dictionary: Mythology

**Description:** Mythological figures, creatures, and concepts from world mythologies.

**Use case:** Themed name generation for fantasy games or creative projects.

**Initial words:**
- Phoenix (creature)
- Atlas (titan)
- Aurora (deity)
- Fenrir (creature)
- Pegasus (creature)
...
```

## Reporting Inappropriate Content

### Content Report Issue

If you find an inappropriate word or combination, please open an issue using the **Content Report** template:

1. Go to **Issues** → **New Issue**
2. Select **Content Report**
3. Fill in the required information

### What to Include

| Field | Required | Description |
|-------|----------|-------------|
| Word(s) | Yes | The problematic word(s) |
| Dictionary | Yes | Which dictionary contains the word |
| Category | Yes | profane, sexual, offensive, discriminatory, violent, ambiguous, other |
| Severity | Yes | 1 (mild), 2 (moderate), 3 (severe) |
| Context | No | Why this is problematic or offensive combinations |

### Issue Template

```markdown
## Content Report

**Word(s):** [word]
**Dictionary:** [adjectives/colors/animals/etc.]
**Category:** [profane/sexual/offensive/discriminatory/violent/ambiguous/other]
**Severity:** [1/2/3]

**Context (optional):**
[Explain why this is problematic, including any offensive combinations it forms]
```

### Response Time

- **Severity 3 (severe):** Addressed within 24 hours, word immediately added to blocklist
- **Severity 2 (moderate):** Addressed within 72 hours
- **Severity 1 (mild):** Addressed within 1 week, may require discussion

## Review Process

### For Word Additions

1. **Automated checks** — CI validates format, uniqueness, and blocklist
2. **Combination check** — CI tests for offensive phrase combinations
3. **Maintainer review** — Manual review of word appropriateness
4. **Merge** — Approved changes are merged

### For Content Reports

1. **Triage** — Maintainer assesses severity and validity
2. **Discussion** — Community input if needed (non-obvious cases)
3. **Action** — Word is either:
   - Removed from dictionary and added to blocklist
   - Kept with documented justification
4. **Update** — Blocklist is updated with details

## Technical Guidelines

### CSV Format

- **Encoding:** UTF-8 without BOM
- **Line endings:** Unix-style (LF only)
- **Quoting:** Only quote fields containing commas
- **Sorting:** Alphabetical by `word` column preferred

### Word Format

- **Capitalization:** Title case (first letter uppercase)
- **Characters:** ASCII letters only (A-Z, a-z)
- **Length:** 2-15 characters recommended
- **No spaces:** Single words only

### Category Values

Use existing category values when possible:

| Dictionary | Categories |
|------------|------------|
| adjectives | personality, physical, abstract |
| colors | [color family: red, blue, green, etc.] |
| animals | mammal, bird, reptile, amphibian, mythical |
| celestial | star, planet, moon, constellation, phenomenon, concept |
| nature | landform, water, weather, biome, flora, mineral |
| science | physics, chemistry, biology, mathematics, computing, symbol |

### Testing Locally

Run the validation script to check your changes:

```bash
# Install dependencies
pip install frictionless

# Validate the package
frictionless validate datapackage.json

# Check for duplicates
python scripts/check_duplicates.py

# Test combinations
python scripts/check_combinations.py
```

## Code of Conduct

All contributors are expected to adhere to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Please be respectful and constructive.


By participating in this project, you agree to maintain a welcoming and inclusive environment. Be respectful and constructive in all interactions.

## Questions?

Open a Discussion or Issue if you have questions about:

- Whether a word is appropriate
- How to categorize a word
- Dictionary boundaries and scope

Thank you for helping make this project better!
