filename = input('File name:').lower()
match filename[-4:]:
    case '.gif':
        print('image/gif')
    case '.png':
        print('image/png')
    case '.jpg'|'jpeg':
        print('image/jpeg')
    case '.txt':
        print('text/plain')
    case '.pdf':
        print('application/pdf')
    case '.zip':
        print('application/zip')
    case _:
        print('application/octet-stream')
