[![CI](https://github.com/transceptor-technology/python-dutycalls-sdk/workflows/CI/badge.svg)](https://github.com/transceptor-technology/python-dutycalls-sdk/actions)
[![Release Version](https://img.shields.io/github/release/transceptor-technology/python-dutycalls-sdk)](https://github.com/transceptor-technology/python-dutycalls-sdk/releases)

# DutyCalls SDK

DutyCalls SDK for the Python language.

---

- [Installation](#installation)
- [Client](#client)
  - [New ticket](#new-ticket)
  - [Close tickets](#close-tickets)
  - [Unacknowledge tickets](#unacknowledge-tickets)
  - [Get tickets](#get-tickets)
  - [New ticket hit](#new-ticket-hit)
  - [Get ticket hits](#get-ticket-hits)

---

## Installation

The easiest way is to use PyPI:

```bash
pip install dutycalls_sdk
```

## Client

The DutyCalls Client needs to be initialized using a `login` and `password`.

> See the [documentation](https://docs.dutycalls.me/rest-api/authentication/) for instructions on how to get these credentials.

Example:

```python
from dutycalls import Client

client = Client(login='abcdef123456', password='abcdef123456')
```

### New ticket

Create a new ticket in DutyCalls.

#### Return value

```python
[
    {
        "sid": 'XXXXXX...',
        "channel": "my-first-channel"
    },
    {
        "sid": 'YYYYYY...',
        "channel": "my-second-channel"
    }
]
```

#### Example

```python
# This ticket is based on a default source, you might have to
# change the ticket according your own source mapping.
ticket = {
    'title': 'My Test Ticket',
    'body': 'This is an example'
}

# multiple channels are supported
channels = 'my-first-channel', 'my-second-channel'

await client.new_ticket(ticket=ticket, *channels)
```

### Close tickets

Close one or more ticket(s) in DutyCalls.

#### Return value

```python
None
```

#### Example

```python
# Closes two tickets. The comment argument is optional.
await client.close_tickets(
    'aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIdCxIHY2hhbm5lbBiwhAUMCxIGdGlja2V0GPODDAyiAQpwcm9kdWN0aW9u',
    'aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIbCxIHY2hhbm5lbBiDBwwLEgZ0aWNrZXQYlgoMogEKcGxheWdyb3VuZA',
    comment='Closed by the DutyCalls SDK'
)
```

### Unacknowledge tickets

Un-acknowledge one or more ticket(s) in DutyCalls.

#### Return value

```python
None
```

#### Example

```python
# Un-acknowledges two tickets. The comment argument is optional.
await client.unacknowledge_tickets(
    'aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIdCxIHY2hhbm5lbBiwhAUMCxIGdGlja2V0GPODDAyiAQpwcm9kdWN0aW9u',
    'aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIbCxIHY2hhbm5lbBiDBwwLEgZ0aWNrZXQYlgoMogEKcGxheWdyb3VuZA',
    comment='Unacknowledged by the DutyCalls SDK'
)
```

### Get tickets

Return one or more ticket(s) in DutyCalls.

#### Return value

```python
    [
        {
            "utc_time": 1632724764,
            "utc_received_time": 1632724764,
            "utc_acknowledged_time": null,
            "utc_closed_time": null,
            "title": "This is the title of the ticket.",
            "body": "This is the body of the ticket.",
            "body_type": "markdown",
            "severity": 1.0,
            "sender": "Me",
            "links": [],
            "identifier": null,
            "tags": [
                {
                    "#": 196687
                }
            ],
            "channel": "example-channel",
            "source": "example-source",
            "status": "unacknowledged",
            "assignee": null,
            "sid": "aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIdCxIHY2hhbm5lbBiwhAUMCxIGdGlja2V0GPODDAyiAQpwcm9kdWN0aW9u"
        }
    ]
```

#### Example

```python
# Returns a ticket.
await client.get_tickets(
    'aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIdCxIHY2hhbm5lbBiwhAUMCxIGdGlja2V0GPODDAyiAQpwcm9kdWN0aW9u'
)
```

### New ticket hit

Add a new hit to one or more ticket(s) in DutyCalls.

#### Return value

```python
None
```

#### Example

```python
# Adds a new hit to a ticket.
await client.new_ticket_hit(
    {
        "summary": "The summary.",
        "timestamp": 1621951028,
        "ticketProperties": {
            "links": ["https://some-domain.com"],
            "severity": "high"
        }
    },
    'aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIdCxIHY2hhbm5lbBiwhAUMCxIGdGlja2V0GPODDAyiAQpwcm9kdWN0aW9u'
)
```

### Get ticket hits

Retrieve the hits of a ticket in DutyCalls.

#### Return value

```python
[
    {
        "unix_time": 1633085094,
        "unix_received_time": 1633085094,
        "summary": "This is the summary of the ticket."
    }
]
```

#### Example

```python
# Returns the hits of a given ticket.
await client.get_ticket_hits(
    'aiBzfnJlYWN0LWZpcmViYXNlLWF1dGhlbnRpYy1lNGU3NHIdCxIHY2hhbm5lbBiwhAUMCxIGdGlja2V0GPODDAyiAQpwcm9kdWN0aW9u'
)
```
