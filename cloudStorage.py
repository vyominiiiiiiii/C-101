import dropbox
class TransferData():
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        with open(fileFrom,"rb") as f:
            dbx.files_upload(f.read(),fileTo)

def main():
    accessToken="sl.BfJ0XYSXlma5a3vot4euEWIHtqaIEOCWDqxXQXmCnqlHCfB0bcAlDfvV9IDh0677Ht6NDNhqKQzDwnusk676lomlmhjd3s5DcmlwMJgjMcmTLrkz9fhBEYsb7GB2dnq1wz8GGA8"
    transferData=TransferData("accessToken")
    fileFrom=input("Enter the file path to transfer ")
    fileTo=input("Enter the full path to upload to dropbox ")
    transferData.uploadFile(fileFrom,fileTo)
    print("File has been moved")

main()
        
        