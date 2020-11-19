import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AlBE2neemhUiuyi01BClDnW0rCFRi-ie9FH8k38qsBRQB4t4fdzwzRL8sni90eD2vfJk9QqIeDxVdNCwjzzyHs9vSrLDfSe-M8dQmcZVYY9KDzV0fMAh29JtK1tmK0Pfe7OGcys'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  

   
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
