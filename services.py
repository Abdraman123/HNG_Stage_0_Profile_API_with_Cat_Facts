"""
Business logic and external service integrations.

This file contains functions that handle business logic,
separate from the API endpoint definitions.
"""

import httpx
from fastapi import HTTPException
from datetime import datetime, timezone
from typing import Dict, Any
import os


# Configuration constants
CAT_FACT_API = "https://catfact.ninja/fact"
REQUEST_TIMEOUT = 5.0  # 5 seconds


async def fetch_cat_fact() -> str:
    """
    Fetches a random cat fact from the Cat Facts API.
    
    This function handles all the complexity of:
    - Making an HTTP request
    - Handling timeouts
    - Error handling
    - Data extraction
    
    Returns:
        str: A random cat fact
        
    Raises:
        HTTPException: If the API call fails for any reason
        
    Example:
        >>> fact = await fetch_cat_fact()
        >>> print(fact)
        "Cats can rotate their ears 180 degrees."
    """
    try:
        # Create an async HTTP client with timeout
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            # Make GET request to Cat Facts API
            response = await client.get(CAT_FACT_API)
            
            # Raise exception if status code is 4xx or 5xx
            response.raise_for_status()
            
            # Parse JSON response
            data = response.json()
            
            # Extract fact from response, with fallback
            fact = data.get("fact", "Cats are amazing creatures!")
            
            return fact
            
    except httpx.TimeoutException:
        # Handle timeout errors specifically
        raise HTTPException(
            status_code=503,
            detail="Cat Facts API is taking too long to respond. Please try again."
        )
        
    except httpx.HTTPStatusError as e:
        # Handle HTTP errors (4xx, 5xx responses)
        raise HTTPException(
            status_code=503,
            detail=f"Cat Facts API returned an error: {e.response.status_code}"
        )
        
    except httpx.RequestError as e:
        # Handle network errors (connection failed, DNS issues, etc.)
        raise HTTPException(
            status_code=503,
            detail=f"Failed to connect to Cat Facts API: {str(e)}"
        )
        
    except Exception as e:
        # Catch any unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error while fetching cat fact: {str(e)}"
        )


def get_current_timestamp() -> str:
    """
    Gets the current UTC timestamp in ISO 8601 format.
    
    ISO 8601 is the international standard for date/time representation.
    Format: YYYY-MM-DDTHH:MM:SS.mmmmmm+00:00
    
    Returns:
        str: Current UTC timestamp
        
    Example:
        >>> timestamp = get_current_timestamp()
        >>> print(timestamp)
        "2025-10-18T14:30:45.123456+00:00"
    """
    return datetime.now(timezone.utc).isoformat()


def get_user_info() -> Dict[str, str]:
    """
    Retrieves user information from environment variables.
    
    This function reads user data from environment variables,
    making it easy to configure without changing code.
    
    Returns:
        dict: User information (email, name, stack)
        
    Example:
        >>> user = get_user_info()
        >>> print(user["name"])
        "John Doe"
    """
    return {
        "email": os.getenv("USER_EMAIL", "your.email@example.com"),
        "name": os.getenv("USER_NAME", "Your Full Name"),
        "stack": os.getenv("USER_STACK", "Python/FastAPI")
    }


async def build_profile_response() -> Dict[str, Any]:
    """
    Builds the complete profile response with all required data.
    
    This is the main business logic function that:
    1. Fetches a cat fact from external API
    2. Gets current timestamp
    3. Retrieves user info
    4. Assembles everything into response format
    
    Returns:
        dict: Complete profile response data
        
    Raises:
        HTTPException: If fetching cat fact fails
    """
    # Fetch cat fact (this is async, so we await it)
    cat_fact = await fetch_cat_fact()
    
    # Get current timestamp
    timestamp = get_current_timestamp()
    
    # Get user information
    user_info = get_user_info()
    
    # Build and return response
    return {
        "status": "success",
        "user": user_info,
        "timestamp": timestamp,
        "fact": cat_fact
    }