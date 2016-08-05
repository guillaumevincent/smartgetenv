import os
import unittest
from testfixtures import log_capture

from smartgetenv import get_env, get_bool, get_list, get_float, get_int


class GetEnvTestCases(unittest.TestCase):
    def test_get_env(self):
        os.environ['NAME'] = 'Vador'
        self.assertEqual('Vador', get_env('NAME', 'Dark'))

    def test_get_env_default_value(self):
        self.assertEqual('Dark', get_env('NAME2', 'Dark'))

    @log_capture()
    def test_get_env_default_value_different_log_warning(self, log):
        os.environ['LOG_ENABLE'] = 'False'
        get_env('LOG_ENABLE', True)
        self.assertTrue('smartgetenv WARNING' in str(log))
        self.assertTrue('use smartgetenv.get_bool' in str(log))


class GetBoolTestCases(unittest.TestCase):
    def test_get_bool(self):
        os.environ['ZERO'] = '0'
        self.assertFalse(get_bool('ZERO'))
        os.environ['NO'] = 'no'
        self.assertFalse(get_bool('NO'))
        os.environ['False'] = 'False'
        self.assertFalse(get_bool('False'))
        os.environ['false'] = 'false'
        self.assertFalse(get_bool('false'))

        os.environ['ONE'] = '1'
        self.assertTrue(get_bool('ONE'))
        os.environ['YES'] = 'yes'
        self.assertTrue(get_bool('YES'))
        os.environ['True'] = 'True'
        self.assertTrue(get_bool('True'))
        os.environ['true'] = 'true'
        self.assertTrue(get_bool('true'))

    def test_get_bool_type(self):
        os.environ['A'] = 'True'
        self.assertTrue(isinstance(get_bool('A'), bool))
        self.assertTrue(isinstance(get_bool('B', False), bool))

    def test_get_bool_type_default_value(self):
        self.assertTrue(get_bool('C', True))
        self.assertFalse(get_bool('D', False))


class GetArrayTestCases(unittest.TestCase):
    def test_get_array(self):
        os.environ['LIST'] = 'a;b'
        self.assertListEqual(['a', 'b'], get_list('LIST'))

    def test_get_array_with_custom_separator(self):
        os.environ['LIST2'] = 'a,b,c'
        self.assertListEqual(['a', 'b', 'c'], get_list('LIST2', separator=','))
        os.environ['LIST3'] = 'a/b/c'
        self.assertListEqual(['a', 'b', 'c'], get_list('LIST3', [], '/'))

    def test_get_array_with_default_value(self):
        self.assertListEqual([], get_list('LIST4', []))


class GetFloatTestCases(unittest.TestCase):
    def test_get_float(self):
        os.environ['FLOAT'] = '9.99'
        self.assertEqual(9.99, get_float('FLOAT'))

    def test_get_float_with_default_value(self):
        self.assertEqual(19.99, get_float('FLOAT2', 19.99))


class GetIntTestCases(unittest.TestCase):
    def test_get_int(self):
        os.environ['INT'] = '9'
        self.assertEqual(9, get_int('INT'))

    def test_get_int_with_default_value(self):
        self.assertEqual(19, get_int('INT2', 19))


if __name__ == '__main__':
    unittest.main()
