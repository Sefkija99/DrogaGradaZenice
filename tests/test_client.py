"""
"""

import unittest
import logging
import asyncio
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from dutycalls import Client  # nopep8
from dutycalls.errors import DutyCallsAuthError, DutyCallsRequestError  # nopep8


# Credentials are required
_LOGIN = os.environ.get('DUTYCALLS_LOGIN')
_PASSWORD = os.environ.get('DUTYCALLS_PASSWORD')

# Ticket SID for testing unacknowledge
_UNACK_TICKET_SID = int(os.environ.get('DUTYCALLS_TICKET_SID', 0))


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
        tickets = self.loop.run_until_complete(client.new_ticket({
            'title': 'This is a test',
            'body': 'Just some plain text...',
            'dateTime': int(time.time()),
            'severity': 'low',
            'sender': 'DutyCalls SDK Test',
        }, 'Test'))
        self.assertEqual(len(tickets), 1)
        ticket = tickets[0]
        self.assertIsInstance(ticket, dict)
        ticket_sid = ticket['sid']
        self.assertIsInstance(ticket_sid, str)
        self.assertEqual(ticket['channel'], 'Test')
        try:
            self.loop.run_until_complete(client.close_tickets(ticket_sid))
        except Exception:
            pass

    def test_multi_channel(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        tickets = self.loop.run_until_complete(client.new_ticket({
            'title': 'This is a test',
            'body': 'Just some plain text...',
            'dateTime': int(time.time()),
            'severity': 'low',
            'sender': 'DutyCalls SDK Test',
        }, 'Test', 'xxx'))
        self.assertEqual(len(tickets), 2)
        ticket_sids = (ticket['sid'] for ticket in tickets)
        try:
            self.loop.run_until_complete(client.close_ticket(*ticket_sids))
        except Exception:
            pass

    def test_close_ticket(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        tickets = self.loop.run_until_complete(client.new_ticket({
            'title': 'This is a test to close a ticket',
            'body': 'Just some plain text in a ticket which will be closed...',
            'dateTime': int(time.time()),
            'severity': 'low',
            'sender': 'DutyCalls SDK Test',
        }, 'Test'))
        ticket = tickets[0]
        ticket_sid = ticket['sid']
        res = self.loop.run_until_complete(client.close_tickets(
            ticket_sid, comment="closed using the DutyCalls SDK"))
        self.assertIs(res, None)

    def test_unacknowledge_ticket(self):
        if not _UNACK_TICKET_SID:
            return
        client = Client(login=_LOGIN, password=_PASSWORD)
        res = self.loop.run_until_complete(client.unacknowledge_ticket(
            _UNACK_TICKET_SID,
            comment='unacknowledged using the DutyCalls SDK'))

    def test_invalid_channel(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        with self.assertRaisesRegex(
                DutyCallsRequestError,
                r'The channel with the name: Fake, does not exist '
                r'or is not linked to the current source.'):
            res = self.loop.run_until_complete(client.new_ticket({
                'title': 'This is a test',
                'body': 'Just some plain text...',
                'dateTime': int(time.time()),
                'severity': 'low',
                'sender': 'DutyCalls SDK Test',
            }, 'Fake'))

    def test_invalid_api_key(self):
        client = Client(login='Fake', password='Fake')
        with self.assertRaisesRegex(
                DutyCallsAuthError,
                r'Invalid API key provided.'):
            self.loop.run_until_complete(client.new_ticket({
                'title': 'This is a test',
                'body': 'Just some plain text...',
                'dateTime': int(time.time()),
                'severity': 'low',
                'sender': 'DutyCalls SDK Test',
            }, 'Test'))

    def test_invalid_ticket(self):
        client = Client(login=_LOGIN, password=_PASSWORD)
        with self.assertRaisesRegex(
                DutyCallsRequestError,
                r'Invalid \'dateTime\' provided.'):
            self.loop.run_until_complete(client.new_ticket({
                'title': 'This is a test',
                'body': 'Just some plain text...',
                'dateTime': '2020-10-01',
                'severity': 'low',
                'sender': 'DutyCalls SDK Test',
            }, 'Test'))
