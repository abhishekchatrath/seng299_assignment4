
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
	
	def test_basic_mother_connection(self):
		mother = MotherShipServer()
		
		self.assertIsNotNone(mother)										# Check that server has been created
		self.assertEqual(mother.sock.getsockname(), ('127.0.0.1', 8080))	# Check that server is connected to default settings
		mother.close()
