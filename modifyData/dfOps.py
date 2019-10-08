import pandas as pd


def excelToDataFrame(excelFile):
    # bring in excel file, will have to change to other dir.
    excelData = pd.read_excel(excelFile)

    #### FUNCTIONS ####

    def pastDate(d):
        if datetime.datetime.now() > d:
            return True
        else:
            return False

    #### INIT OBJECT ####
    articleData = {}

    #### MAIN ####
    for index, row in excelData.iterrows():
        if pastDate(row['Published Date']) and row['Episerver ID'] and row['Live Article URL']:
            try:
                articleData[int(row['Episerver ID'])] = {'epiID': int(row['Episerver ID']), 'pubDate': row['Published Date'], 'liveURL': row['Live Article URL'], 'relatedCatStatus': bool(
                    row["Related Categories Status"]), 'pubTitle': row["Published Article Title"]}
            except:
                pass

    return(articleData)
