# CV Version Manager

A tool for generating professional resumes from structured data using Microsoft Word templates.

## Overview

The CV Version Manager allows you to create polished, consistent resumes by combining structured JSON data with customizable Word document templates. It's designed to help professionals maintain multiple versions of their resume quickly and efficiently.

## Features

- Generate resumes in DOCX format from JSON data
- Support for common resume sections: personal info, summary, skills, experiences, education, certifications, and websites
- Template-based system using `docxtpl` for Word document generation
- Easy to extend with new sections or formatting

## Requirements

- Python 3.x
- Required Python packages (see `requirements.txt`)

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Prepare your resume data in JSON format (see `source/example_data.json` for structure).

3. Run the generator with your data file:
   ```bash
   python run.py source/example_data.json
   ```

4. Find the generated DOCX file in the `generated/` directory.

## Directory Structure

```
.
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── run.py                    # Main script to generate resumes
├── source/
│   └── example_data.json     # Example resume data
├── templates/
│   └── default.docx          # Resume template
└── generated/                # Output directory for generated resumes
```

## Customization

To customize the resume format:

1. Modify `templates/default.docx` to change the layout and styling.
2. Update `run.py` if you need to add new data fields or processing logic.

## Example Data Format

The input JSON should follow this structure:
- `name`: Full name
- `email`: Email address
- `phone`: Phone number
- `address`: Mailing address
- `websites`: List of websites with name and URL
- `professional_summary`: Summary statement
- `skills`: List of skill categories with names
- `certifications`: List of certifications with name and date
- `experiences`: List of work experiences
- `educations`: List of educational backgrounds

## License

This project is open source and available under the MIT License.
