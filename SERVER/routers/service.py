from fastapi import APIRouter
from SERVER.SQL.models import Service
from SERVER.resolvers import service

router = APIRouter(prefix='/Service', tags=['Service'])

@router.post('/create')
def create(_Service: Service) -> int:
    new_id = service.create(_Service)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get')
def get(object_id: int) -> Service | None:
    return service.get(object_id)

@router.get('/')
def get_all() -> list[Service] | None:
    return service.get_all()

@router.delete('/remove')
def remove(object_id: int) -> None:
    return service.remove(object_id)


@router.put("/update")
def update(object_id: int, new_data: Service):
    return service.update(service_id=object_id, new_data=new_data)

