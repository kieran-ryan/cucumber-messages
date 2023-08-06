import uuid as unique_id

counter = 0


def uuid():
    return unique_id.uuid4()


def incrementing():
    global counter
    counter += 1
    return str(counter)
