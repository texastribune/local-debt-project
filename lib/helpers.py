from boot import session


def store_objects(objects):
    for object in objects:
        try:
          session.add(object)
          session.commit()
        except Exception as e:
          session.rollback()
