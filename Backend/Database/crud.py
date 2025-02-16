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
    
    @staticmethod
    def universal_query(base_model, attributes=None, filters=None, joins=None):
        """attribute=[name,age]\n filters=[age>10]\n joins=[table]"""
        try:
            # Start building the query from the base model
            query = db.session.query(*[getattr(base_model, attr) for attr in attributes]) if attributes else db.session.query(base_model)
            
            # Apply joins if provided
            if joins:
                for join_model in joins:
                    query = query.join(join_model)
            
            # Apply filters if provided
            if filters:
                query = query.filter(*filters)
            
            # Execute the query
            results = query.all()
            
            # Serialize results
            if attributes:
                serialized = [dict(zip(attributes, result)) for result in results]
            else:
                serialized = [item.serialize() for item in results]

            return serialized
        except SQLAlchemyError as e:
            return {"message": f"Database error: {str(e)}"}, 500
        except AttributeError as e:
            return {"message": f"Invalid attribute: {str(e)}"}, 400


            
        
