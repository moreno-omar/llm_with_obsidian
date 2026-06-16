# llm_with_obsidian

## Goals
- to have LLM refer to my notes for simple prompts
- to give recommendations on how to improve my notes

## To run 
- `cd` into `app/`
- run `embedding.py` once. Needed to build vectordb
- run `ollama_connect.py` to interact with llm and Retrieval-Augmented Generation
  - model used: phi-4-mini-3_8B:latest
  - assumes user is running model with ollama.

## What the Project won't do
- include instruction sets (1 instruction set is fine)
- include preference sets (same as above)
- require login (runs locally)
- diy embedding
- diy model and weights

## Later
- tests 
  - tests will be created when app already working and refactoring in process.
- browser for chat
  - `input()` is fine for simple testing
  - GUI will offer more benefits for chat.
- CI/CD
  - will be more effective during refactoring.

## Prerequisites
**Python**: `Python 3.13.12`
