from fastapi import APIRouter
from SERVER.SQL.models import Applications
from SERVER.resolvers import applications

router = APIRouter(prefix='/Applications', tags=['Applications'])

@router.post('/create')
def create(_Applications: Applications):
    new_id = applications.create(_Applications)
    return new_id

@router.get('/get')
def get(object_id: int) -> Applications | None:
    return applications.get(object_id)

@router.get('/')
def get_all():
    return applications.get_all()

@router.delete('/remove')
def remove(object_id: int) -> None:
    return applications.remove(object_id)


@router.put("/update")
def update(object_id: int, new_data: Applications):
    return applications.update(applications_id=object_id, new_data=new_data)

