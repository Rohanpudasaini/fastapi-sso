# Google SSO FastAPI Login

A FastAPI-based Single Sign-On (SSO) authentication system that implements Google OAuth 2.0 authentication.

## Features

- Google SSO integration
- Clean UI

## Prerequisites

- Python 3.7+
- FastAPI
- FastAPI-SSO
- Jinja2 (for templating)
- Uvicorn (for running the server)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Rohanpudasaini/fastapi-sso.git
cd fastapi-sso
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Google OAuth credentials:
```bash
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```
To get the `client_id` and `client_secret` please follow this [tutorial](https://itnext.io/fastapi-google-single-sign-on-sso-47454e2e2859)

## Project Structure

```
sso-fastapi/
├── main.py              # Main application file
├── template/            # HTML templates
│   ├── login.html      # Login page template
│   └── index.html      # Dashboard template
├── static/             # Static files
│   ├── css/           # CSS stylesheets
│   └── images/        # Images and icons
└── .env               # Environment variables
```

## Usage

1. Start the server:
```bash
python main.py
```

2. Access the application at `http://localhost:8000`

3. Click the Google login button to authenticate using your Google account

## API Endpoints

- `GET /` - Login page
- `GET /google/login` - Initiate Google SSO
- `GET /google/callback` - Google OAuth callback

## Security Notes

- The application uses secure session management
- OAuth tokens are handled securely
- HTTPS is recommended for production use
- Development mode allows insecure HTTP for testing


## Extras
You can see the request we get from google as callback in the `google_response.py` file.


## Refrence
Most of the code are taken refrence from this medium article [article](https://itnext.io/fastapi-google-single-sign-on-sso-47454e2e2859). Thank you [Chris Karvouniaris](https://github.com/chrisK824)


