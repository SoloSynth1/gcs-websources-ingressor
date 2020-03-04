import io


def byte2buffer(byte_stream):
    buffer = io.BytesIO(byte_stream)
    return buffer
