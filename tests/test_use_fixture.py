import pytest
from sqlalchemy import (
    MetaData,
    Table,
    insert,
    delete,
    orm,
    exc
)

def test_db( engine, session, post_data ):
    table = Table( 'POST', MetaData(), autoload = True, autoload_with = engine )
    bulk_up_query = insert( table ).values( post_data )
    session.execute( bulk_up_query, post_data )
    session.commit()
    session.close()
    delete_query = delete(table)
    session.execute(delete_query)
    session.commit()

def test_valid_db( engine, session, programing_error_post_data ):
    Session = orm.sessionmaker( bind = engine )
    session = Session()
    table = Table( 'POST', MetaData(), autoload = True, autoload_with = engine )
    bulk_up_query = insert( table ).values( programing_error_post_data )

    with pytest.raises(expected_exception = exc.CompileError):
        session.execute( bulk_up_query, programing_error_post_data )



