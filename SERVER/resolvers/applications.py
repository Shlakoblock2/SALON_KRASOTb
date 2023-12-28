from SERVER.SQL.models import Applications
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/buity.db')

def create(_Applications: Applications):
    new_id = dbmanager.execute(
        query="insert into Applications(add_date, serviceID ,comments, date_completion,UserID) values(?, ?, ?, ? , ?)",
        args=(_Applications.add_date, _Applications.serviceID, _Applications.comments, _Applications.date_completion, _Applications.UserID)
    )
    return new_id

def get(Applications_id: int) -> Applications | None:
    res = dbmanager.execute(
        query='select * from Applications where id=(?)',
        args=(Applications_id,)
    )
    return None if not res else Applications(
        id=res[0],
        add_date=res[1],
        UserID=res[2],
        serviceID=res[3],
        comments=res[4],
        date_completion=res[5]
       
    )
def get_all():
    Applications_list = dbmanager.execute(query= "select * from Applications",many=True)
    res = []
    if Applications_list:
        for item in Applications_list:
            res.append(Applications(
                id=item[0],
                add_date=item[1],
                UserID=item[2],
                serviceID=item[3],
                comments=item[4],
                date_completion=item[5]
                
            ))
    return res

def remove(Applications_id: int) -> None:
    return dbmanager.execute('delete from Applications where id=(?)', args=(Applications_id,))

def update(applications_id: int, new_data: Applications) -> None:
    return dbmanager.execute(
        query='update Applications set (add_date, serviceID,comments, date_completion,UserID) = (?, ?, ?, ? , ?) where id=(?)',
        args=(new_data.add_date, new_data.serviceID, new_data.comments,new_data.comments, new_data.date_completion, applications_id))
