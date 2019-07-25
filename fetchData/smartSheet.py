import smartsheet
from credentials import credentials
import globalVars


def downloadSmartsheet():
    downloadDir = globalVars.MAIN_DIR + "/input_files"

    print('Attempting to download Smartsheet as Excel File...')

    # this is the bearer token
    ss_client = smartsheet.Smartsheet(credentials.smartsheet_api_key)
    # content hub library sheet id=7229045214603140
    sheetID = credentials.smartsheet_id
    # sheet = ss_client.Sheets.get_sheet(sheetID)

    ss_client.Sheets.get_sheet_as_excel(
        credentials.smartsheet_id, downloadDir)

    print("Downloaded to " + downloadDir)
