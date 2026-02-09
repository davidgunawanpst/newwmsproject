from src.auth import get_sheets_service
from src.constants import SHEET_ID

def load_data(dataset_name: str):
    service = get_sheets_service()

    result = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=SHEET_ID,
            range="Sheet1!A1:C10"
        )
        .execute()
    )

    values = result.get("values", [])

    return {
        "dataset": dataset_name,
        "rows_returned": len(values),
        "data": values
    }