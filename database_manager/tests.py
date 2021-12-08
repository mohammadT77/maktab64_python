from unittest import TestCase

from database_manager.manager import DBManager
from database_manager.models import Patient


class DBManagerTest(TestCase):

    def setUp(self):
        self.db_manager = DBManager('laboratory')

    def test_create_success(self):
        self.p1 = Patient('Reza', 'Moosavi', '0911111212', '1224456786', age=20)
        res = self.db_manager.create(self.p1)

        self.assertIsInstance(res, int)
        self.assertEqual(self.p1.id, res)

    def test_read_success(self):
        if not hasattr(self, 'p1'):
            self.test_create_success()
        p = self.db_manager.read(Patient, self.p1.id)

        self.assertEqual(vars(p), vars(self.p1))

    def test_upgrade_success(self):
        if not hasattr(self, 'p1'):
            self.test_create_success()
        new_first_name = 'Akbar'
        self.p1.first_name = new_first_name
        self.db_manager.update(self.p1)

        read_p = self.db_manager.read(Patient, self.p1.id)
        self.assertEqual(read_p.first_name, new_first_name)

    def test_delete_success(self):
        if not hasattr(self, 'p1'):
            self.test_create_success()
        id = self.p1.id

        self.db_manager.delete(self.p1)
        self.assertFalse(hasattr(self.p1, 'id'))
        self.assertRaises(Exception, self.db_manager.read, Patient, id)


    def tearDown(self) -> None:
        try:
            self.db_manager.delete(self.p1)
        except:
            pass
        del self.db_manager
