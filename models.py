"""
Pydantic models for request/response schemas.

These models define the structure of data coming in and going out of our API.
FastAPI uses these for:
- Automatic validation
- API documentation generation
- Type checking
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Literal


class UserInfo(BaseModel):
    """
    User profile information schema.
    
    Attributes:
        email: User's email address
        name: User's full name
        stack: Backend technology stack being used
    """
    email: EmailStr = Field(
        ...,
        description="User's email address",
        example="john.doe@example.com"
    )
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="User's full name",
        example="John Doe"
    )
    stack: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Backend technology stack",
        example="Python/FastAPI"
    )

    class Config:
        # Show example in API docs
        json_schema_extra = {
            "example": {
                "email": "jane.doe@example.com",
                "name": "Jane Doe",
                "stack": "Python/FastAPI"
            }
        }


class ProfileResponse(BaseModel):
    """
    Complete profile endpoint response schema.
    
    This is the exact structure returned by the /me endpoint.
    
    Attributes:
        status: Always "success" for successful requests
        user: User profile information
        timestamp: Current UTC time in ISO 8601 format
        fact: Random cat fact from external API
    """
    status: Literal["success"] = Field(
        ...,
        description="Response status - always 'success' for valid responses"
    )
    user: UserInfo = Field(
        ...,
        description="User profile information"
    )
    timestamp: str = Field(
        ...,
        description="Current UTC timestamp in ISO 8601 format",
        example="2025-10-17T14:30:45.123456+00:00"
    )
    fact: str = Field(
        ...,
        description="Random cat fact fetched from Cat Facts API",
        example="Cats sleep 70% of their lives."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "user": {
                    "email": "john.doe@example.com",
                    "name": "John Doe",
                    "stack": "Python/FastAPI"
                },
                "timestamp": "2025-10-17T14:30:45.123456+00:00",
                "fact": "Cats can rotate their ears 180 degrees."
            }
        }


class HealthResponse(BaseModel):
    """
    Health check endpoint response schema.
    """
    status: Literal["healthy"] = Field(
        ...,
        description="Health status of the API"
    )
    timestamp: str = Field(
        ...,
        description="Current UTC timestamp"
    )


class ErrorResponse(BaseModel):
    """
    Error response schema for failed requests.
    """
    detail: str = Field(
        ...,
        description="Error message describing what went wrong"
    )