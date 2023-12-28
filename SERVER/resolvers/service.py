from SERVER.SQL.models import Service
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/buity.db')

def create(_Service: Service) -> int:
    new_id = dbmanager.execute(
        query="insert into Service(name) values(?)",
        args=(_Service.name,)
    )
    return new_id

def get(Service_id: int) -> Service | None:
    res = dbmanager.execute(
        query='select * from Service where id=(?)',
        args=(Service_id,)
    )

    return None if not res else Service(
	    id=res[0],
        name=res[1]
    )
    
def get_all() -> list[Service]:
    Service_list = dbmanager.execute(query= "select * from Service",many=True)
    res = []
    if Service_list:
        for service in Service_list:
            res.append(Service(
                id=service[0],
                name=service[1]
            ))

    return res

def remove(service_id: int) -> None:
    return dbmanager.execute('delete from Service where id=(?)', args=(service_id,))

def update(service_id: int, new_data: Service) -> None:
    return dbmanager.execute(
        query='update Service set (name) = (?) where id=(?)',
        args=(new_data.name, service_id))
