import unittest

import battleship.controllers.end_game_handeler as end_game_handeler
import battleship.controllers.shot_handeler as shot_handeler
import battleship.controllers.game_creator_handeler as game_creator_handeler


class TestSampleClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_should_fail(self):
        self.fail('You should remove this test')
        

if __name__=="__main__":
    unittest.main()
