# HNG Stage 0 - Profile API with Cat Facts

A RESTful API built with FastAPI that returns profile information along with random cat facts from an external API. This project demonstrates professional backend development practices including modular code organization, async programming, data validation, and production deployment.

## 🚀 Live Demo

**API Endpoint:** https://YOUR-APP.railway.app/me

**Interactive Documentation:** https://YOUR-APP.railway.app/docs

**Health Check:** https://YOUR-APP.railway.app/health

## 📋 Features

- ✅ RESTful GET endpoint at `/me`
- ✅ Dynamic cat facts fetched from Cat Facts API on every request
- ✅ ISO 8601 formatted UTC timestamps that update in real-time
- ✅ Comprehensive error handling with appropriate status codes
- ✅ CORS enabled for frontend integration
- ✅ Auto-generated interactive API documentation (Swagger UI)
- ✅ Health check endpoint for monitoring
- ✅ Modular code structure following best practices
- ✅ Environment-based configuration management
- ✅ Type hints and data validation with Pydantic

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Framework:** FastAPI 0.115.0
- **Server:** Uvicorn (ASGI server)
- **HTTP Client:** HTTPX (async)
- **Data Validation:** Pydantic
- **Configuration:** python-dotenv
- **Deployment:** Railway
- **Version Control:** Git & GitHub

## 📁 Project Structure

```
hng-stage0/profile api with cat facts
│
├── main.py              # FastAPI application and API endpoints
├── models.py            # Pydantic models for request/response schemas
├── services.py          # Business logic and external API integration
├── config.py            # Configuration and settings management
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation (this file)
└── runtime.txt         # Python version for deployment (optional)
```

### File Descriptions

- **main.py**: Entry point of the application. Contains FastAPI app initialization, middleware setup, and all API endpoint definitions.
- **models.py**: Pydantic models that define the structure of request and response data. Used for automatic validation and documentation.
- **services.py**: Business logic layer. Contains functions for fetching cat facts, generating timestamps, and building responses.
- **config.py**: Centralized configuration management. Loads environment variables and provides settings throughout the application.

## 📦 Installation & Local Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git
- A text editor (VS Code, PyCharm, etc.)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/hng-stage0.git
cd hng-stage0
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `httpx` - Async HTTP client
- `python-dotenv` - Environment variable management
- `pydantic[email]` - Data validation with email support

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```env
# User Information (REQUIRED - Replace with your actual info)
USER_EMAIL=your.email@example.com
USER_NAME=Your Full Name
USER_STACK=Python/FastAPI

# Server Configuration (OPTIONAL)
HOST=0.0.0.0
PORT=8000
DEBUG=True
LOG_LEVEL=INFO
```

**⚠️ IMPORTANT:** Replace the placeholder values with your actual information!

### Step 5: Verify Configuration

Run the configuration verification script:

```bash
python verify_config.py
```

You should see:
```
✅ USER_EMAIL: your.email@example.com
✅ USER_NAME: Your Full Name
✅ USER_STACK: Python/FastAPI
✅ ALL CHECKS PASSED!
```

### Step 6: Run the Application

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-restart on code changes (development only).

You should see:
```
🚀 HNG Stage 0 API v1.0.0 starting...
📝 User: Your Full Name
📧 Email: your.email@example.com
🛠️  Stack: Python/FastAPI
📚 Docs: http://0.0.0.0:8000/docs

INFO:     Uvicorn running on http://0.0.0.0:8000
```

The API will be available at:
- **API:** http://127.0.0.1:8000
- **Interactive Docs:** http://127.0.0.1:8000/docs
- **Alternative Docs:** http://127.0.0.1:8000/redoc

## 🔌 API Endpoints

### GET /

Root endpoint providing API information and available routes.

**Response:**
```json
{
  "message": "Welcome to HNG Stage 0 API",
  "version": "1.0.0",
  "endpoints": {
    "/me": "Get profile information with a random cat fact",
    "/health": "Health check endpoint",
    "/docs": "Interactive API documentation (Swagger UI)",
    "/redoc": "Alternative API documentation (ReDoc)"
  },
  "repository": "https://github.com/YOUR-USERNAME/hng-stage0"
}
```

### GET /health

Health check endpoint for monitoring and uptime verification.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-10-18T14:30:45.123456+00:00"
}
```

**Status Codes:**
- `200 OK` - Service is healthy

### GET /me

**Main endpoint** - Returns profile information with a random cat fact.

**Response Format:**

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T14:30:45.123456+00:00",
  "fact": "Cats sleep 70% of their lives."
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Always "success" for valid responses |
| `user.email` | string | User's email address (validated format) |
| `user.name` | string | User's full name |
| `user.stack` | string | Backend technology stack |
| `timestamp` | string | Current UTC time in ISO 8601 format |
| `fact` | string | Random cat fact from Cat Facts API |

**Status Codes:**
- `200 OK` - Successful request
- `503 Service Unavailable` - External Cat Facts API is down or timed out
- `500 Internal Server Error` - Unexpected server error

**Important Notes:**
- The timestamp updates dynamically with each request
- A new cat fact is fetched on every request (not cached)
- Response always includes `Content-Type: application/json` header

## 🧪 Testing

### Using curl

```bash
# Test root endpoint
curl http://127.0.0.1:8000/

# Test health check
curl http://127.0.0.1:8000/health

# Test main profile endpoint
curl http://127.0.0.1:8000/me

# Test multiple times to see timestamp and fact changes
curl http://127.0.0.1:8000/me
curl http://127.0.0.1:8000/me
curl http://127.0.0.1:8000/me
```

### Using Python requests

```python
import requests

# Test the /me endpoint
response = requests.get("http://127.0.0.1:8000/me")
print(response.json())

# Verify timestamp updates
import time
response1 = requests.get("http://127.0.0.1:8000/me")
time.sleep(1)
response2 = requests.get("http://127.0.0.1:8000/me")

print("Timestamp 1:", response1.json()["timestamp"])
print("Timestamp 2:", response2.json()["timestamp"])
print("Timestamps different:", response1.json()["timestamp"] != response2.json()["timestamp"])
```

### Using the Interactive Docs

1. Navigate to http://127.0.0.1:8000/docs
2. Click on the `/me` endpoint
3. Click **"Try it out"**
4. Click **"Execute"**
5. View the response and test multiple times

The interactive documentation automatically shows:
- Request/response schemas
- Example responses
- Error responses
- Try-it-out functionality

## 🌐 Deployment

This application is deployed on **Railway**.

### Deployment Steps (Railway)

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Create Railway Account**
   - Go to https://railway.app
   - Sign up/login with GitHub

3. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `hng-stage0` repository

4. **Configure Environment Variables**
   
   In Railway dashboard → Variables tab, add:
   ```
   USER_EMAIL=your.email@example.com
   USER_NAME=Your Full Name
   USER_STACK=Python/FastAPI
   ```

5. **Deploy**
   - Railway automatically detects Python
   - Installs dependencies from requirements.txt
   - Starts the application
   - Generates a public URL

6. **Get Public URL**
   - Settings → Domains
   - Click "Generate Domain"
   - Copy your URL (e.g., `hng-stage0-production.up.railway.app`)

### Environment Variables Required for Deployment

Set these in your deployment platform:

| Variable | Description | Example |
|----------|-------------|---------|
| `USER_EMAIL` | Your email address | john.doe@example.com |
| `USER_NAME` | Your full name | John Doe |
| `USER_STACK` | Your backend stack | Python/FastAPI |

### Testing Deployed API

```bash
# Replace YOUR-APP with your actual Railway URL
curl https://YOUR-APP.railway.app/me
```

## 🔍 Key Implementation Details

### Async Programming

The application uses Python's `async/await` for non-blocking I/O operations:

```python
async def fetch_cat_fact() -> str:
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(CAT_FACT_API)
        return response.json()["fact"]
```

**Benefits:**
- Server can handle multiple requests simultaneously
- Doesn't block while waiting for external API
- Better performance under load

### Data Validation

Pydantic models automatically validate all data:

```python
class UserInfo(BaseModel):
    email: EmailStr  # Validates email format
    name: str = Field(min_length=2, max_length=100)
    stack: str
```

Invalid data is rejected automatically with clear error messages.

### Error Handling

Comprehensive error handling for external API calls:

- **Timeout errors** → 503 Service Unavailable
- **Network errors** → 503 Service Unavailable  
- **HTTP errors** → 503 Service Unavailable
- **Unexpected errors** → 500 Internal Server Error

### Timestamp Format

Uses ISO 8601 format with UTC timezone:

```python
datetime.now(timezone.utc).isoformat()
# Output: "2025-10-18T14:30:45.123456+00:00"
```

**Why UTC?**
- Universal - no timezone confusion
- International standard
- Easy for clients to convert to local time

### Modular Architecture

Code is organized into logical modules:

- **Separation of concerns** - Each file has one responsibility
- **Reusability** - Functions can be used across endpoints
- **Testability** - Easy to test individual components
- **Scalability** - Easy to add new features

## 📚 Dependencies

```
fastapi==0.115.0           # Modern web framework
uvicorn[standard]==0.30.6  # ASGI server
httpx==0.27.2              # Async HTTP client
python-dotenv==1.0.1       # Environment variables
pydantic[email]==2.5.0     # Data validation with email support
```

### Why These Dependencies?

- **FastAPI**: Modern, fast, auto-generates documentation
- **Uvicorn**: Production-ready ASGI server
- **HTTPX**: Async HTTP client (better than `requests` for async)
- **python-dotenv**: Loads environment variables from `.env`
- **Pydantic**: Powerful data validation and serialization

## 🛡️ Security Considerations

- ✅ Environment variables for sensitive data
- ✅ `.env` file excluded from version control
- ✅ Input validation on all endpoints
- ✅ Appropriate error messages (no sensitive info leaked)
- ✅ CORS configured properly
- ✅ Timeout on external API calls

## 🐛 Troubleshooting

### Issue: ModuleNotFoundError

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Issue: Environment Variables Not Loading

**Error:** API returns default values instead of your info

**Solution:**
1. Verify `.env` file exists in project root
2. Check `.env` format (no quotes around values)
3. Ensure `python-dotenv` is installed
4. Run `python verify_config.py` to check

### Issue: Import Errors

**Error:** `ImportError: cannot import name 'settings' from 'config'`

**Solution:**
1. Ensure all files (`main.py`, `models.py`, `services.py`, `config.py`) are in the same directory
2. Check for syntax errors in the files
3. Verify you're running uvicorn from the correct directory

### Issue: Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Kill process on port 8000
# Mac/Linux:
lsof -ti:8000 | xargs kill -9

# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use a different port:
uvicorn main:app --reload --port 8001
```

### Issue: Cat Facts API Timeout

**Error:** 503 errors when testing `/me` endpoint

**Solution:**
- Check if https://catfact.ninja/fact is accessible
- Verify timeout is set to 5 seconds
- Check your internet connection
- Error handling should return appropriate message

## 🤝 Contributing

This is a task submission for HNG Internship Stage 0. However, suggestions and feedback are welcome!

## 📝 License

This project is created for the HNG Internship program.

## 👤 Author

**Your Name**
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourusername)

## 🙏 Acknowledgments

- [HNG Internship](https://hng.tech/internship) for the practical challenge
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent framework
- [Cat Facts API](https://catfact.ninja/) for providing the cat facts

## 🔗 Important Links

- **HNG Internship:** https://hng.tech/internship
- **Hire Python Developers:** https://hng.tech/hire/python-developers
- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **Pydantic Documentation:** https://docs.pydantic.dev/

## 📊 Project Stats

- **Lines of Code:** ~300
- **Files:** 8
- **Dependencies:** 5
- **Endpoints:** 3
- **Response Time:** <100ms (local), <500ms (deployed)

---

**Built with ❤️ for HNG Internship Stage 0**

*If you found this helpful, please star ⭐ the repository!*
