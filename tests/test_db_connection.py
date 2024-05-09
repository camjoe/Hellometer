
import unittest
from postgresql.config import load_config
from postgresql.connect import connect

class TestDbConnection(unittest.TestCase):
 
    def test_connect(self):
        config = load_config()
        conn = connect(config)

        self.assertTrue("user=postgres" in conn.dsn)
        self.assertTrue("dbname=hellometer_db" in conn.dsn)

        # TODO: test error case

    def test_load_config(self):        
        config = load_config()
        
        self.assertEqual(len(config), 4)
        self.assertEqual(config['host'], 'localhost')
        self.assertEqual(config['database'], 'hellometer_db')
        self.assertEqual(config['user'], 'postgres')
        self.assertTrue('password' in config)


        with self.assertRaises(Exception) as ex:
            load_config(filename="database_error.ini")
            self.assertEqual("Section postgresql not found in the database.ini file")

        
if __name__ == '__main__':
    unittest.main()