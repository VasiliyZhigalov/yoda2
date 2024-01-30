import re
from typing import List
from src.schemas.user_query import UserQuerySchemaAdd


def parse_user_query(query: str) -> List[UserQuerySchemaAdd]:
    query_list = query.replace(',', '.').split('\n')
    user_query_list = []
    for q in query_list:
        product = q.split('-')[0].strip()
        right_str = q.split('-')[1].strip()
        quantity = re.findall(r'\d*\.\d+|\d+', right_str)
        if quantity:
            quantity = quantity[0]
            unit = right_str.replace(quantity, '').strip()
            user_query_list.append(UserQuerySchemaAdd(product=product, quantity = quantity, unit = unit))
    return user_query_list