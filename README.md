# SBOL-LLM

## Overview

This project was inspired by a desire to create a sequence to sequence model capable of generating high-level circuit designs from natural language descriptions. Given the ability to "reason" and draw on a vast amount of textual knowledge, LLM's present an opportunity to engineer systems that incorporate these vast knowledge bases into their output. This presents an opportunty to leverage knowledge bases for genetic circuit and part design.

Realizing that such a task requires a currently non-existant dataset of circuit-description pairs, we aim to derive standard and complete circuit desciptions from the numerous circuits and parts and their grossly insufficient descriptions. 

This project encompasses several steps, including scraping of parts repositories, integration and implemenation of various curation and analysis tools for extracting attributes and metadata from circuit and sequences, a basic front end for interfacing with the description generating LLM. 

## Project Structure

```plaintext
│   ├── sboll_llm/
|       ├── data/         # for downloading and processing datasets
|       ├── docs/         # general documentation as well as curated knowledge base for LLM
│       ├── repositories/ # for scraping and interacting with parts repos
│       ├── notebooks/    # for experimentation. also contains code to instantiate the front-end chat demo
|       ├── requirements.txt
```

## Goals
Derive circuit descriptions from insufficient and incomplete description and DNA sequences

- Prompt engineering: provide an agent with precise instructions as well as example inputs and ideal completions (descriptions)
- Incorporate knowledge bases, context and background information into model prompts
- Develop a front-end for easily interfacing with LLM
- Integrate curation, annotation and analysis tools to enrich model inputs and provide circuit design context 
- Assemble dataset of circuits using parts repositories such as SynBioHub and iGEM and language modeling techniques
- Validate the ability to model to generate "ideal" desriptions
- Utilize the pipeline to transform ciruit designs
 
## Usage
To create the LLM assistant, use the following notebook:
```
notebooks/agent1.ipynb
```

To instantiate the front-end interface,
```
notebooks/sbol_llm.ipynb
```

______________________________________________________________________________________________________________________

## Usage
Data Preprocessing:

Normalize and standardize genetic circuit data.
Extract descriptions and structure the data for model training.

```
python sboll_llm/data/pipeline.py
```

Model Training:

Train models for genetic circuit design and masked component modeling.
```
python sboll_llm/train/training_circuit_from_description.py
python sboll_llm/train/training_masked_component_modeling.py
```

## Future Work
- Joint embeddings for circuit diagrams (jpgs) and circuit specifications (json)
- Selection of desired pretrained text model
- Join component descriptions with component embeddings
- Simplified json circuit to SBOL
- Integrate additional datasets from other repositories and collections
