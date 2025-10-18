"""
Main FastAPI application for HNG Stage 0.

This is the entry point of the application. It:
- Initializes the FastAPI app
- Sets up middleware (CORS)
- Defines API endpoints
- Delegates business logic to services module
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Import our custom modules
from models import ProfileResponse, HealthResponse
from services import build_profile_response, get_current_timestamp
from config import settings


# Initialize FastAPI app with metadata from config
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc UI
)


# Add CORS middleware
# CORS = Cross-Origin Resource Sharing
# This allows frontends from different domains to access your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint - provides API information.
    
    This is what users see when they visit your API's base URL.
    It serves as a welcome page and quick reference.
    """
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "endpoints": {
            "/me": "Get profile information with a random cat fact",
            "/health": "Health check endpoint",
            "/docs": "Interactive API documentation (Swagger UI)",
            "/redoc": "Alternative API documentation (ReDoc)"
        },
        "repository": "Add your GitHub repo URL here"
    }


@app.get("/health", response_model=HealthResponse, tags=["Monitoring"])
async def health_check():
    """
    Health check endpoint.
    
    Used for monitoring and ensuring the API is running.
    Many deployment platforms automatically ping this endpoint.
    
    Returns:
        HealthResponse: Status and timestamp
    """
    return {
        "status": "healthy",
        "timestamp": get_current_timestamp()
    }


@app.get("/me", response_model=ProfileResponse, tags=["Profile"])
async def get_profile():
    """
    Returns profile information along with a random cat fact.
    
    **This is the main endpoint for Stage 0.**
    
    Features:
    - Returns your personal information (email, name, stack)
    - Fetches a fresh cat fact from an external API on every request
    - Includes the current UTC timestamp
    - Updates dynamically with each request
    
    Returns:
        ProfileResponse: Complete profile data with cat fact
        
    Raises:
        HTTPException: 
            - 503 if Cat Facts API is unavailable
            - 500 for unexpected errors
    
    Example Response:
        ```json
        {
          "status": "success",
          "user": {
            "email": "john@example.com",
            "name": "John Doe",
            "stack": "Python/FastAPI"
          },
          "timestamp": "2025-10-17T14:30:45.123456+00:00",
          "fact": "Cats sleep 70% of their lives."
        }
        ```
    """
    try:
        # Delegate business logic to services module
        # This keeps our endpoint clean and focused
        response_data = await build_profile_response()
        
        # Return JSON response with explicit content type
        return JSONResponse(
            content=response_data,
            status_code=200,
            headers={"Content-Type": "application/json"}
        )
        
    except HTTPException:
        # Re-raise HTTP exceptions from services
        # (e.g., when Cat Facts API fails)
        raise
        
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


# Startup event - runs when the application starts
@app.on_event("startup")
async def startup_event():
    """
    Runs when the application starts.
    
    Good place to:
    - Initialize database connections
    - Load ML models
    - Run configuration checks
    - Log startup information
    """
    print(f"\n🚀 {settings.APP_NAME} v{settings.APP_VERSION} starting...")
    print(f"📝 User: {settings.USER_NAME}")
    print(f"📧 Email: {settings.USER_EMAIL}")
    print(f"🛠️  Stack: {settings.USER_STACK}")
    print(f"📚 Docs: http://{settings.HOST}:{settings.PORT}/docs\n")


# Shutdown event - runs when the application stops
@app.on_event("shutdown")
async def shutdown_event():
    """
    Runs when the application shuts down.
    
    Good place to:
    - Close database connections
    - Clean up resources
    - Save state
    """
    print(f"\n👋 {settings.APP_NAME} shutting down...\n")


# Run the application
# This block only executes when running the file directly
# (not when imported as a module)
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG  # Auto-reload on code changes in debug mode
    )