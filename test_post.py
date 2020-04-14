import unittest
from post_youdao import *
from unittest import mock


class PostyoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        #import  time
        #t=time.time()
        #ts=str(int(round(t * 1000)))
        #print(ts)
        get_ts=mock.Mock(return_value='1584686566650')
        self.assertEqual('1584686566650',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15846865666505')
        self.assertEqual('15846865666505',get_salt())

    def test_get_sign(self):
        get_sign=mock.Mock(return_value='ebbca201bf1eaa2797175df91e7dc725')
        self.assertEqual('ebbca201bf1eaa2797175df91e7dc725',get_sign())


if __name__ == '__main__':
    unittest.main()
