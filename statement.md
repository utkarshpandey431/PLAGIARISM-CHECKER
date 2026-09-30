# Project Statement: Plagiarism Checker

## Problem Statement

Manually comparing documents for plagiarism is slow, error-prone, and inconsistent. There is a need for a simple, automated tool that quickly calculates the similarity between two texts without requiring internet access or external services.

## Scope of the Project

This project develops a command-line Python application that accepts two text inputs (typed or from files) and calculates a similarity percentage. The scope is limited to word-set comparison using the Jaccard similarity index. It does not perform semantic analysis, synonym detection, or large-scale database checks.

## Target Users

- Students checking assignments for accidental plagiarism
- Educators performing first-pass screening of submissions
- Writers verifying originality of their work

## High-Level Features

1. Multiple input modes (typed text or files)
2. Text normalization (lowercase, remove non-alphabetic characters)
3. Jaccard similarity calculation
4. Result classification (High / Moderate / Low)
5. File error handling
6. Configurable thresholds via config.json

