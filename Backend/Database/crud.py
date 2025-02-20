import os
from dotenv import load_dotenv
from .models import db
import dropbox
from dropbox.files import WriteMode
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import SQLAlchemyError
load_dotenv()
import cloudinary.uploader

dbx = dropbox.Dropbox(os.getenv('DROPBOX_TOKEN'))
class CRUD:
    @staticmethod
    def add_item(model, **kwargs):
        """add_item( table_name, {'id':3})"""
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
        """get_item( table_name , id)"""
        try:
            item = model.query.get(item_id)
            if item is None:
                return {"message": f"Item with ID {item_id} does not exist!"}, 404
            return item.serialize() if hasattr(item, 'serialize') else item.__dict__
        except SQLAlchemyError as e:
            return {"message": f"Error: {str(e)}"}, 500
            
    @staticmethod
    def update_item(model, item_id, **kwargs):
        """update_item( table_name, id, **{'name':'prince'})"""
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
    def universal_query(base_model, attributes=None, filters=None, joins=None):
        """ 
        Universal query method that:
        - Selects specified attributes, defaults to all attributes from the base model.
        - Dynamically joins tables and allows selecting attributes from them.
        - Filters data based on conditions.
        """
        try:
            query = db.session.query(base_model)  # Start with base model
            
            # Ensure attributes are properly structured
            if attributes is None:
                attributes = {base_model.__tablename__: [column.name for column in base_model.__table__.columns]}

            # Normalize table names to lowercase to avoid case-sensitivity issues
            all_models = {base_model.__tablename__.lower(): base_model}  # Include base model
            if joins:
                all_models.update({m.__tablename__.lower(): m for m, _ in joins})  # Include joined models

            # Apply joins if provided
            if joins:
                for join_model, condition in joins:
                    query = query.join(join_model, condition)

            # Validate and get the selected columns from base and joined tables
            selected_columns = []
            for table_name, cols in attributes.items():
                table_name = table_name.lower()  # Convert to lowercase for lookup
                model = all_models.get(table_name)
                if not model:
                    raise ValueError(f"Table '{table_name}' not found in joins: {list(all_models.keys())}")

                for col in cols:
                    if not hasattr(model, col):
                        raise ValueError(f"Column '{col}' not found in '{table_name}'")
                    selected_columns.append(getattr(model, col))

            # Apply selected columns to the query
            query = query.with_entities(*selected_columns)

            # Apply filters if provided
            if filters:
                query = query.filter(*filters)

            # Fetch results
            results = query.all()

            # Serialize results
            serialized = [dict(zip([col.name for col in selected_columns], row)) for row in results]

            return serialized

        except SQLAlchemyError as e:
            return {"message": f"Database error: {str(e)}"}, 500
        except AttributeError as e:
            return {"message": f"Invalid attribute: {str(e)}"}, 400
        except ValueError as e:
            return {"message": f"Query error: {str(e)}"}, 400
        
