import datetime
from unittest import TestCase
from app import app, db
from models import StateCasesPerDay
from tests.runner import clear_db


class TestStatesPerDayMethods(TestCase):

    def setUp(self):
        self.app_context = app.test_request_context()
        self.app_context.push()
        app.test_client()
        self.app = app
        db.create_all()
        self.db = db

    def tearDown(self):
        clear_db(self.db)

    def test_if_save_method_saves_states_per_day_on_database(self):
        StateCasesPerDay().save(self.db.session, id=1, date=datetime.date.today(),
                                country='Brasil', state_id=1, newcases=35, totalcases=3)
        self.db.session.commit()
        _model = self.db.session.query(StateCasesPerDay).filter_by(
            state_id=1).first()
        self.assertIsNotNone(_model)