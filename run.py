#!/usr/bin/env python3

import json
from docxtpl import DocxTemplate

# Load resume data from JSON file
with open('resume_data.json', 'r') as f:
    resume_data = json.load(f)

# Load the template
template = DocxTemplate('templates/default.docx')

# Render the template with data
template.render(resume_data)

# Save the rendered document
template.save('resumes/resume.docx')
