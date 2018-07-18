from core.exceptions import NotFoundException
from . import DatabaseSession
from dal.entities import MessageTable


class MySqlStore:
    @staticmethod
    def create_object(entity):
        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()
        return entity

    @staticmethod
    def read_object(entity):
        # returned data is a list
        with DatabaseSession() as session:
            data = session.query(entity).all()
            # data = session.query(entity).filter(entity == _id).all()
        return data

    @staticmethod
    def update_object(target, params):
        entity = target.__class__
        with DatabaseSession() as session:
            data = session.query(entity). \
                filter(entity.id == target.id). \
                first()

            if not data:
                # object not found
                raise NotFoundException()

            for k, v in params.items():
                if not hasattr(data, k):
                    raise ValueError("Entity {} has not property `{}`.".format(entity.__class__.__name__, k))
                setattr(data, k, v)

            session.commit()
            return data

    @staticmethod
    def delete_object(_id, entity):
        # TODO fixed  in the future
        with DatabaseSession() as session:
            session.query(entity). \
                filter(entity.id == _id). \
                delete()
            session.commit()
            return True


class MessageStore(MySqlStore):
    # define by yourself
    def __init__(self):
        self.entity = MessageTable

    def _transfer_to_entity(self, message_dic):
        entity = self.entity
        # extract message to entity
        entity = message_dic
        return entity

    def insert_new_message(self, message_dic):
        entity = self._transfer_to_entity(message_dic)
        return self.create_object(entity)
