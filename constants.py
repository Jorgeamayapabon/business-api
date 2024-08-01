import os

TABLE_USER = os.environ["table_user"]
TABLE_CLIENT = os.environ["table_client"]
TABLE_SALE = os.environ["table_sale"]

MESSAGE_404_STR: str = "Page Not Found"
MESSAGE_404_USER_STR: str = "User not found"
MESSAGE_404_CLIENT_STR: str = "Client not found"
MESSAGE_404_SALE_STR: str = "Sale not found"
MESSAGE_FAIL_CREATE_STR: str = "Failed to create record in DynamoDB"
MESSAGE_FAIL_UPDATE_STR: str = "Failed to update record in DynamoDB"
MESSAGE_FAIL_DELETE_STR: str = "Failed to delete record in DynamoDB"

PATTERN_USERS_ID_R_STR = r"/users/\d+"
PATTERN_CLIENT_ID_R_STR = r"/clients/\d+"
PATTERN_SALE_ID_R_STR = r"/sales/\d+"

PATTERN_USERS_R_STR = r"/users"
PATTERN_CLIENTS_R_STR = r"/clients"
PATTERN_SALES_R_STR = r"/sales"