from constants import TABLE_SALE
from queries import db_insert


def create_sale(sale_item: dict):
    try:
        return db_insert(table_name=TABLE_SALE, item=sale_item)

    except Exception as e:
        print(f"exception in create_sale => {e}")
        return 500
