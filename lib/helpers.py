from boot import session


def store_objects(objects):
    for obj in objects:
        store_object(obj)

def store_object(obj):
    try:
        session.add(obj)
        session.commit()
    except Exception as e:
        session.rollback()
