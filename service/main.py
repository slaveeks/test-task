from service.service import GoogleSheetService

if __name__ == '__main__':
    # Initiate GoogleSheet service
    service = GoogleSheetService()
    # Start scheduling document
    service.schedule()
