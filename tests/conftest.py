import pytest
from sqlalchemy import create_engine, orm

@pytest.fixture( scope = 'session' )
def engine():
    engine = create_engine( 'mysql+pymysql://root:1234@localhost:3308/gsheet?charset=utf8' )
    return engine

@pytest.fixture(scope = 'session')
def session(engine):
    Session = orm.sessionmaker(bind=engine)
    return Session()

@pytest.fixture(scope = 'session')
def metric_data():
    yield dict(
        version_id = '19',
        group_order_1 = '1',
        group_order_2= '1',
        metric_order= '1',
        group_1= 'Touchpoint',
        group_2= 'Touchpoint',
        metric_key= 'touchpoints_impression_click',
        metric_name= 'Touchpoints (Impression+click)',
        metric_name_kr= 'Touchpoints (Impression+click)',
        metric_value= '{\n        "type": "filtered",\n        "filter": {\n          "type": "and",\n          "fields": [\n            {\n              "type": "in",\n              "dimension": "data__eventdata__category",\n              "values": ["9110","9212","9214","9215","9216"]\n            }\n           ]\n        },\n        "aggregator": {\n          "type": "longSum",\n          "fieldName": "EventCount"\n        }\n}',
        description= 'Sum of impressions and clicks',
        description_kr= 'Impression 수와 Click 수의 합',
        data_source= 'airbridge-actual-report',
        result_type= 'int',
        facebook_masking_condition = '',
        subspec_trend_report= '1'
    )

@pytest.fixture(scope = 'session') #
def post_data():
    yield dict (
        id = '467',
        title = 'mock test'
    )

@pytest.fixture(scope = 'session')
def integrity_error_post_data():
    yield dict (
        id = '1234',
        title = 'mock test_02'
    )

@pytest.fixture(scope = 'session')
def programing_error_post_data():
    yield dict (
        id = '12345',
        title = 'mock test_02',
        code = 'error'
    )