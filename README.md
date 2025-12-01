
# Intranet management

API created to connect the STAFFBASE platform endpoints, responsible for creating and structuring intranets. According to the documentation, two types of functions were created using the admin token: SEARCH for users and DEACTIVATE, applied to employees who have left the company, and, for employees who had not yet accessed the platform for the first time, removal of the invitation, terminating their registration.

## Additional information

This repository corresponds to part of a larger project in which I am participating on GitHub.

## Authors

- [@matiasmov](https://github.com/matiasmov)

## Environment variables

To run this project, you will need to add the following environment variables to your .env file

`TOKEN` -> staffbase platform administrative token

`BASE_URL` -> URL where the company intranet is located

`API_KEY` -> API password

## Technologies

**Back-end:** Python

**DB:** Supabase

## Used by (Companies)

This project is used by the following companies:

- Cladtek

## Deploy

To deploy this project run

```PowerShell
  uv run uvicorn app.main:app 
  OR
  uv run uvicorn app.main:app --reload
```

## Dependencies

```python

[project]
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]>=0.121.2",
    "python-dotenv>=1.2.1",
    "requests>=2.32.5",
    "uvicorn>=0.38.0",
]

```

## Documentation

[STAFFBASE](https://developers.staffbase.com/)
