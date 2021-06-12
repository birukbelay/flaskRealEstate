from unittest import TestCase

from flask import current_app

from app import app
class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.server.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        # self.assertTrue(
        #     app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///C:\class\5k\4th1\2webProg\assignments\projet2\api\sqldb.db'
        # )