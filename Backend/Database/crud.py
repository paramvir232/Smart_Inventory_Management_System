from models import db
from sqlalchemy.exc import SQLAlchemyError

class CRUD:
    @staticmethod
    def add_item(model, **kwargs):
        try:
            item = model(**kwargs)
            db.session.add(item)
            db.session.commit()
            return {"message": "Inserted", **kwargs}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": f"Error: {str(e)}"}, 500

    @staticmethod
    def get_item(model, item_id):
        try:
            item = model.query.get(item_id)
            if item is None:
                return {"message": f"Item with ID {item_id} does not exist!"}, 404
            return item.serialize() if hasattr(item, 'serialize') else item.__dict__
        except SQLAlchemyError as e:
            return {"message": f"Error: {str(e)}"}, 500
            
    @staticmethod
    def update_item(model, item_id, **kwargs):
        try:
            item = model.query.get(item_id)
            if item is None:
                return {"message": f"Item with ID {item_id} does not exist!"}, 404
            
            for key, value in kwargs.items():
                setattr(item, key, value)
            
            db.session.commit()
            return {"message": "Updated", **kwargs}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": f"Error: {str(e)}"}, 500
            
    @staticmethod
    def delete_item(model, item_id):
        try:
            item = model.query.get(item_id)
            if item is None:
                return {"message": f"Item with ID {item_id} does not exist!"}, 404
            
            db.session.delete(item)
            db.session.commit()
            return {"message": f"Deleted item with ID {item_id}"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": f"Error: {str(e)}"}, 500

    @staticmethod
    def get_all_items(model):
        try:
            items = model.query.all()
            return [item.serialize() if hasattr(item, 'serialize') else item.__dict__ for item in items]
        except SQLAlchemyError as e:
            return {"message": f"Error: {str(e)}"}, 500
