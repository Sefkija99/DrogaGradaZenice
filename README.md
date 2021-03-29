# Dutycalls.me SDK

DutyCalls.me SDK for the Python language

---------------------------------------
  * [Installation](#installation)
  * [Client](#client)
    * [New ticket](#new-ticket)
    * [Close ticket](#new-ticket)
    * [Unacknowledge ticket](#unacknowledge-ticket)

---------------------------------------


## Installation

The easiest way is to use PyPI:

```
pip install dutycalls_sdk
```

## Client

The DutyCalls.me Client needs to be initialized using a *login* and *password*.
> See [https://docs.dutycalls.me/rest-api/#authentication](https://docs.dutycalls.me/rest-api/#authentication) for instructions on how to get these credentials.

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
        "id": 123,
        "channel": "my-first-channel"
    },
    {
        "id": 456,
        "channel": "my-second-channel"
    }
]
```

#### Example:
```python
# This ticket is based on a default source, you might have to change the
# ticket according your own source mapping.
ticket = {
    'title': 'My Test Ticket',
    'body': 'This is an example',
}

# multiple channels are supported
channels = 'my-first-channel', 'my-second-channel'

await client.new_ticket(ticket=ticket, *channels)
```

### Close ticket

Close a ticket in DutyCalls.

#### Return value

```python
None
```

#### Example:

```python
await client.close_ticket(ticket_id=123)
```

### Unacknowledge ticket

Unacknowledge a ticket in DutyCalls.

#### Return value

```python
None
```

#### Example:

```python
await client.unacknowledge_ticket(ticket_id=123)
```
