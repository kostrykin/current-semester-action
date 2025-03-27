import datetime
import unittest

import semester


class semester_Test(unittest.TestCase):

    def test_current(self):
        fixtures = [
            (
                dict(
                    today=datetime.datetime(2025, 1, 15),
                    which='current',
                    floor='',
                ),
                {
                    'name': 'ws24',
                    'description': 'WS 24/25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 3, 15),
                    which='current',
                    floor='',
                ),
                {
                    'name': 'ws24',
                    'description': 'WS 24/25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 4, 15),
                    which='current',
                    floor='',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 9, 15),
                    which='current',
                    floor='',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 10, 15),
                    which='current',
                    floor='',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 12, 15),
                    which='current',
                    floor='',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
        ]
        for kwargs, expected in fixtures:
            with self.subTest(**kwargs):
                actual = semester.expand(**kwargs)
                self.assertEqual(actual, expected)

    def test_next(self):
        fixtures = [
            (
                dict(
                    today=datetime.datetime(2025, 1, 15),
                    which='next',
                    floor='',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 3, 15),
                    which='next',
                    floor='',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 4, 15),
                    which='next',
                    floor='',
                ),
                {
                    'name': 'ss26',
                    'description': 'SS 26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 9, 15),
                    which='next',
                    floor='',
                ),
                {
                    'name': 'ss26',
                    'description': 'SS 26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 10, 15),
                    which='next',
                    floor='',
                ),
                {
                    'name': 'ws26',
                    'description': 'WS 26/27',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 12, 15),
                    which='next',
                    floor='',
                ),
                {
                    'name': 'ws26',
                    'description': 'WS 26/27',
                }
            ),
        ]
        for kwargs, expected in fixtures:
            with self.subTest(**kwargs):
                actual = semester.expand(**kwargs)
                self.assertEqual(actual, expected)

    def test_current_floor_ws(self):
        fixtures = [
            (
                dict(
                    today=datetime.datetime(2025, 1, 15),
                    which='current',
                    floor='ws',
                ),
                {
                    'name': 'ws24',
                    'description': 'WS 24/25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 3, 15),
                    which='current',
                    floor='ws',
                ),
                {
                    'name': 'ws24',
                    'description': 'WS 24/25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 4, 15),
                    which='current',
                    floor='ws',
                ),
                {
                    'name': 'ws24',
                    'description': 'WS 24/25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 9, 15),
                    which='current',
                    floor='ws',
                ),
                {
                    'name': 'ws24',
                    'description': 'WS 24/25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 10, 15),
                    which='current',
                    floor='ws',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 12, 15),
                    which='current',
                    floor='ws',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
        ]
        for kwargs, expected in fixtures:
            with self.subTest(**kwargs):
                actual = semester.expand(**kwargs)
                self.assertEqual(actual, expected)

    def test_next_floor_ws(self):
        fixtures = [
            (
                dict(
                    today=datetime.datetime(2025, 1, 15),
                    which='next',
                    floor='ws',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 3, 15),
                    which='next',
                    floor='ws',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 4, 15),
                    which='next',
                    floor='ws',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 9, 15),
                    which='next',
                    floor='ws',
                ),
                {
                    'name': 'ws25',
                    'description': 'WS 25/26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 10, 15),
                    which='next',
                    floor='ws',
                ),
                {
                    'name': 'ws26',
                    'description': 'WS 26/27',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 12, 15),
                    which='next',
                    floor='ws',
                ),
                {
                    'name': 'ws26',
                    'description': 'WS 26/27',
                }
            ),
        ]
        for kwargs, expected in fixtures:
            with self.subTest(**kwargs):
                actual = semester.expand(**kwargs)
                self.assertEqual(actual, expected)

    def test_current_floor_ss(self):
        fixtures = [
            (
                dict(
                    today=datetime.datetime(2025, 1, 15),
                    which='current',
                    floor='ss',
                ),
                {
                    'name': 'ss24',
                    'description': 'SS 24',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 3, 15),
                    which='current',
                    floor='ss',
                ),
                {
                    'name': 'ss24',
                    'description': 'SS 24',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 4, 15),
                    which='current',
                    floor='ss',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 9, 15),
                    which='current',
                    floor='ss',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 10, 15),
                    which='current',
                    floor='ss',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 12, 15),
                    which='current',
                    floor='ss',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
        ]
        for kwargs, expected in fixtures:
            with self.subTest(**kwargs):
                actual = semester.expand(**kwargs)
                self.assertEqual(actual, expected)

    def test_next_floor_ss(self):
        fixtures = [
            (
                dict(
                    today=datetime.datetime(2025, 1, 15),
                    which='next',
                    floor='ss',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 3, 15),
                    which='next',
                    floor='ss',
                ),
                {
                    'name': 'ss25',
                    'description': 'SS 25',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 4, 15),
                    which='next',
                    floor='ss',
                ),
                {
                    'name': 'ss26',
                    'description': 'SS 26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 9, 15),
                    which='next',
                    floor='ss',
                ),
                {
                    'name': 'ss26',
                    'description': 'SS 26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 10, 15),
                    which='next',
                    floor='ss',
                ),
                {
                    'name': 'ss26',
                    'description': 'SS 26',
                }
            ),
            (
                dict(
                    today=datetime.datetime(2025, 12, 15),
                    which='next',
                    floor='ss',
                ),
                {
                    'name': 'ss26',
                    'description': 'SS 26',
                }
            ),
        ]
        for kwargs, expected in fixtures:
            with self.subTest(**kwargs):
                actual = semester.expand(**kwargs)
                self.assertEqual(actual, expected)