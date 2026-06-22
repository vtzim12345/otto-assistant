from fastapi import APIRouter, Depends, HTTPException
from src.models.schemas import ProjectCreate
from src.config.firebase_config import get_db
from src.api.routes.auth import verify_token
from datetime import datetime

router = APIRouter()

@router.post("/")
async def create_project(project_data: ProjectCreate, user_id: str = Depends(verify_token)):
    """Create a new project"""
    try:
        db = get_db()
        
        project = {
            'user_id': user_id,
            'name': project_data.name,
            'icon': project_data.icon,
            'color': project_data.color,
            'description': project_data.description,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        
        doc_ref = db.collection('projects').add(project)
        
        return {
            'id': doc_ref[1].id,
            **project
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def get_projects(user_id: str = Depends(verify_token)):
    """Get all projects for user"""
    try:
        db = get_db()
        
        projects = db.collection('projects')\
            .where('user_id', '==', user_id)\
            .stream()
        
        result = []
        for proj in projects:
            result.append({
                'id': proj.id,
                **proj.to_dict()
            })
        
        return {'projects': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
