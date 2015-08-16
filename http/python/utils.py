#!/usr/bin/env python


def encode_multipart_formdata(file_data, mime_type, upload_id):
    boundary = 'DeviceImageUploadFormBoundary84BEAM87huhifeMEucwe87UPugnlopoSCOTTY'
    crlf = '\n'
    line = []
    line.append('--' + boundary)
    line.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file_info', str(upload_id)))
    line.append('Content-Type: %s' % mime_type)
    line.append('')
    line.append(file_data)
    line.append('--%s--' % boundary)
    line.append('')
    body = crlf.join(line)
    content_type = 'multipart/form-data; boundary=%s' % boundary
    return content_type, body
