from fastapi import FastAPI
import random
from typing import Dict, Any, List
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware

app = FastAPI(
    title="Simple Random Jira Task API",
    description="A fast API to fetch random mock Jira tasks.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,       
    allow_methods=["*"],          
    allow_headers=["*"],          
)    


MOCK_JIRA_TASKS: List[Dict[str, Any]] = [
    {
        "id": "10001",
        "key": "PROJ-1",
        "summary": "Implement user authentication module",
        "description": "Develop and integrate user login, registration, and session management using OAuth2.",
        "issue_type": "Story",
        "status": "To Do",
        "priority": "High"
    },
    {
        "id": "10002",
        "key": "BUG-5",
        "summary": "Fix broken search filter on dashboard",
        "description": "The search filter on the main dashboard is not applying correctly, leading to incorrect results.",
        "issue_type": "Bug",
        "status": "In Progress",
        "priority": "Highest"
    },
    {
        "id": "10003",
        "key": "TASK-12",
        "summary": "Update database schema for new features",
        "description": "Add new tables and columns required for the upcoming reporting and analytics features.",
        "issue_type": "Task",
        "status": "Done",
        "priority": "Medium"
    },
    {
        "id": "10004",
        "key": "PROJ-2",
        "summary": "Develop API for product catalog",
        "description": "Create RESTful API endpoints for retrieving, adding, updating, and deleting product information.",
        "issue_type": "Story",
        "status": "To Do",
        "priority": "High"
    },
    {
        "id": "10005",
        "key": "DEV-3",
        "summary": "Optimize image loading performance",
        "description": "Implement lazy loading and responsive image techniques to improve page load times.",
        "issue_type": "Sub-task",
        "status": "In Progress",
        "priority": "Medium"
    },
    {
        "id": "10006",
        "key": "BUG-6",
        "summary": "Error on checkout page after discount code",
        "description": "Users are encountering a server error when applying certain discount codes during checkout.",
        "issue_type": "Bug",
        "status": "To Do",
        "priority": "Highest"
    },
    {
        "id": "10007",
        "key": "TASK-13",
        "summary": "Refactor legacy notification service",
        "description": "Rewrite the existing notification service to use a more modern and scalable architecture.",
        "issue_type": "Task",
        "status": "Backlog",
        "priority": "Low"
    },
    {
        "id": "10008",
        "key": "PROJ-3",
        "summary": "Integrate third-party payment gateway",
        "description": "Connect our e-commerce platform with Stripe for credit card processing.",
        "issue_type": "Story",
        "status": "To Do",
        "priority": "High"
    },
    {
        "id": "10009",
        "key": "DEV-4",
        "summary": "Add unit tests for API endpoints",
        "description": "Write comprehensive unit tests to ensure the reliability and correctness of existing API services.",
        "issue_type": "Sub-task",
        "status": "In Progress",
        "priority": "Medium"
    },
    {
        "id": "10010",
        "key": "BUG-7",
        "summary": "Incorrect data display in analytics report",
        "description": "The monthly sales analytics report is showing discrepancies in total revenue calculations.",
        "issue_type": "Bug",
        "status": "To Do",
        "priority": "High"
    }
]

@app.get("/random_task", response_model=Dict[str, Any])
async def get_random_jira_task():
    if not MOCK_JIRA_TASKS:
        return {}
    
    return random.choice(MOCK_JIRA_TASKS)

@app.get("/all_tasks", response_model=List[Dict[str, Any]])
async def get_all_jira_tasks():
    return MOCK_JIRA_TASKS