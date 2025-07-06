from pydantic import BaseModel
from typing import List, Optional
import app.models.DAO as DAO


class shop_data(BaseModel):
    shop_name:str 
    description:str 
    #carrossel_images:List[str]


def get_shop(name:str) -> Optional[shop_data]:
    shop_info = DAO.executar_sql(
        DAO.sql_load_studio,
        params=(name,)
    )    

    if not shop_info:
        return None

    id = shop_info[0]['id']

    return shop_data(
        shop_name  =shop_info[0]['nome'],
        description=shop_info[0]['bio' ],
    )