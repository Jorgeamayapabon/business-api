from constants import TABLE_SALE
from queries import db_insert


def create_sale(sale_item: dict):
    """
    Creates a sale record in the DynamoDB table.

    This function attempts to insert a sale item into the DynamoDB table specified by the `TABLE_SALE`
    constant. It uses the `db_insert` function to perform the insertion and handles any exceptions that may
    occur during the process.

    Parameters:
        sale_item (dict): The sale record to be inserted into the DynamoDB table. The item should conform
                          to the schema expected by the table.

    Returns:
        int: The HTTP status code resulting from the insertion. Returns the status code returned by `db_insert`
             if successful, otherwise returns 500 if an exception occurs.

    Example:
        >>> create_sale({"sale_id": "123", "user_id": "user1", "client_id": "client1", "value": 100})
        200
    """
    try:
        return db_insert(table_name=TABLE_SALE, item=sale_item)

    except Exception as e:
        print(f"exception in create_sale => {e}")
        return 500
