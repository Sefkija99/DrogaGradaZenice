"""
"""

import unittest
import logging
import asyncio
import time
import sys
from dutycalls import Client
from dutycalls.errors import DutyCallsAuthError, DutyCallsRequestError

# Credentials are required
_LOGIN = os.environ.get('DUTYCALLS_LOGIN')
_PASSWORD = os.environ.get('DUTYCALLS_PASSWORD')

# Ticket ID for testing unacknowledge
_UNACK_TICKET_ID = int(os.environ.get('DUTYCALLS_TICKET_ID', 0))


class TestClient(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.loop = asyncio.get_event_loop()
        Client.BASE_URL = 'https://playground.dutycalls.me/api'

    def test_client_init(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        self.assertIsInstance(client, Client)

    def test_new_ticket(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        res = self.loop.run_until_complete(client.new_ticket('Test', {
            'title': 'This is a test',
            'body': 'Just some plain text...',
            'dateTime': int(time.time()),
            'severity': 'low',
            'sender': 'DutyCalls SDK Test',
        }))
        self.assertIsInstance(res, dict)
        self.assertIn('tickets', res)
        ticket = res['tickets'][0]
        ticket_id = ticket['id']
        self.assertIsInstance(ticket_id, int)
        self.assertEqual(ticket['channel'], 'Test')
        try:
            self.loop.run_until_complete(client.close_ticket(ticket_id))
        except Exception:
            pass

    def test_close_ticket(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        res = self.loop.run_until_complete(client.new_ticket('Test', {
            'title': 'This is a test to close a ticket',
            'body': 'Just some plain text in a ticket which will be closed...',
            'dateTime': int(time.time()),
            'severity': 'low',
            'sender': 'DutyCalls SDK Test',
        }))

        ticket_id = res['tickets'][0]['id']
        res = self.loop.run_until_complete(client.close_ticket(
            ticket_id, "closed using the DutyCalls SDK"))
        self.assertIs(res, None)

    def test_unacknowledge_ticket(self):
        if not _UNACK_TICKET_ID:
            return
        client = Client(login=_LOGIN, password=_PASSWORD)
        res = self.loop.run_until_complete(client.unacknowledge_ticket(
            _UNACK_TICKET_ID, 'unacknowledged using the DutyCalls SDK'))

    def test_invalid_channel(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        with self.assertRaisesRegex(
                DutyCallsRequestError,
                r'The channel with the name: Fake, does not exist '
                r'or is not linked to the current source.'):
            res = self.loop.run_until_complete(client.new_ticket('Fake', {
                'title': 'This is a test',
                'body': 'Just some plain text...',
                'dateTime': int(time.time()),
                'severity': 'low',
                'sender': 'DutyCalls SDK Test',
            }))

    def test_invalid_api_key(self):
        client = Client(login='Fake', password='Fake')
        with self.assertRaisesRegex(
                DutyCallsAuthError,
                r'Invalid API key provided.'):
            res = self.loop.run_until_complete(client.new_ticket('Test', {
                'title': 'This is a test',
                'body': 'Just some plain text...',
                'dateTime': int(time.time()),
                'severity': 'low',
                'sender': 'DutyCalls SDK Test',
            }))

    def test_invalid_ticket(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        with self.assertRaisesRegex(
                DutyCallsRequestError,
                r'Invalid \'dateTime\' provided.'):
            res = self.loop.run_until_complete(client.new_ticket('Test', {
                'title': 'This is a test',
                'body': 'Just some plain text...',
                'dateTime': '2020-10-01',
                'severity': 'low',
                'sender': 'DutyCalls SDK Test',
            }))

