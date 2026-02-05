# Django Project Setup Guide

## Prerequisites

Make sure you have the following installed:

- **Python**
- **pip**
- **Git**

## Setup Instructions
1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create and Activate a Virtual Environment

Windows
```bash
python -m venv myenv
myenv\Scripts\activate
```

macOS / Linux
```bash
python3 -m venv myenv
source myenv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the Development Server
```bash
python mysite/manage.py runserver
```

### Notes

The .env file is already tracked in this repository since this is a Django demonstration project.

No additional environment configuration is required.