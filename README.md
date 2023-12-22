# API Amateur Project

## Background Context

In the evolving field of system administration, scripting skills have expanded beyond traditional Bash scripting. Modern System Reliability Engineers (SREs) integrate more sophisticated programming languages like Python for more efficient system management. This project focuses on utilizing Python scripts to interact with and manipulate data through an API, a task not well-suited for Bash scripting.

## Learning Objectives

- Understanding the limitations of Bash scripting
- Comprehending the basics of APIs and REST APIs
- Exploring microservices
- Familiarity with CSV and JSON data formats
- Adhering to Pythonic naming conventions and style guide

## General Requirements

- Preferred editors: vi, vim, emacs
- All files should be executed on Ubuntu 20.04 LTS using Python 3.8.X
- Files must end with a new line
- The first line of all files must be `#!/usr/bin/python3`
- Adherence to `pycodestyle` style guide
- All files must be executable
- Proper documentation for all modules
- Usage of `get` for dictionary value access
- Code should not execute when imported

## Tasks

### 0. Gather data from an API

Write a Python script that extracts TODO list progress for a given employee ID using a REST API. The output format and requirements are detailed in the project instructions.

File: `0-gather_data_from_an_API.py`

### 1. Export to CSV

Extend the previous script to export the data into CSV format.

File: `1-export_to_CSV.py`

### 2. Export to JSON

Modify the script to export the data into JSON format.

File: `2-export_to_JSON.py`

### 3. Dictionary of list of dictionaries

Enhance the script to record all tasks from all employees in JSON format.

File: `3-dictionary_of_list_of_dictionaries.py`

## Resources

- [Friends don’t let friends program in shell script](#)
- [What is an API?](#)
- [PEP8 Python style guide](#)

## Repository

- GitHub repository: holbertonschool-back-end
- Directory: api
