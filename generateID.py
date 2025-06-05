import uuid

def generate_8_digit_uuid():
    uuid_str = str(uuid.uuid4()).replace('-', '')
    return uuid_str[:8]