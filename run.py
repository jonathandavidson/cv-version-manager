#!/usr/bin/env python3

import json
import sys
from docxtpl import DocxTemplate

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Check if a JSON file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python run.py <path_to_json_file>")
    sys.exit(1)

# Load resume data from JSON file
json_file_path = sys.argv[1]
with open(json_file_path, 'r') as f:
    resume_data = json.load(f)

# Load the template
template = DocxTemplate('templates/default.docx')

# Render the template with data
template.render(resume_data)

# Save the rendered document
output_file_path = json_file_path.replace('.json', '.docx')
template.save(f'{config["output_directory"]}{output_file_path.split("/")[-1]}')
