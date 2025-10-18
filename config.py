"""
Configuration settings for the application.

This file centralizes all configuration, making it easy to:
- Change settings without touching business logic
- Use different settings for dev/staging/production
- Keep sensitive data in environment variables
"""

import os
from dotenv import load_dotenv
from typing import List

# Load environment variables from .env file
load_dotenv()


class Settings:
    """
    Application configuration settings.
    
    All settings are loaded from environment variables with sensible defaults.
    """
    
    # API Metadata
    APP_NAME: str = "PROFILE API WITH CAT FACTS"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Profile endpoint with dynamic cat facts"
    
    # Server Settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # User Information (from environment variables)
    # ⚠️ IMPORTANT: Replace these in your .env file!
    USER_EMAIL: str = os.getenv("USER_EMAIL", "your.email@example.com")
    USER_NAME: str = os.getenv("USER_NAME", "Your Full Name")
    USER_STACK: str = os.getenv("USER_STACK", "JavaScript/Nodejs")
    
    # External API Settings
    CAT_FACT_API_URL: str = "https://catfact.ninja/fact"
    API_TIMEOUT: float = 5.0  # seconds
    
    # CORS Settings
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # React default
        "http://localhost:8080",  # Vue default
        "*"  # Allow all (only for development/testing)
    ]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


# Create a global settings instance
settings = Settings()


# Validation: Check if required environment variables are set
def validate_settings():
    """
    Validates that all required settings are properly configured.
    
    Raises a warning if using default values that should be customized.
    """
    warnings = []
    
    if settings.USER_EMAIL == "your.email@example.com":
        warnings.append("⚠️  USER_EMAIL is using default value. Set it in .env file.")
    
    if settings.USER_NAME == "Your Full Name":
        warnings.append("⚠️  USER_NAME is using default value. Set it in .env file.")
    
    if settings.USER_STACK == "JavaScript/Nodejs":
        warnings.append("⚠️  USER_STACK is using default value. You may want to customize it.")
    
    if warnings:
        print("\n" + "="*60)
        print("⚠️  CONFIGURATION WARNINGS:")
        print("="*60)
        for warning in warnings:
            print(f"  {warning}")
        print("\nPlease update your .env file with your actual information!")
        print("="*60 + "\n")


# Run validation when module is imported
validate_settings()