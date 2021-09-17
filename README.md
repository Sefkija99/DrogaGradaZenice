# Dutycalls.me SDK

DutyCalls.me SDK for the Python language

---------------------------------------
  * [Installation](#installation)
  * [Client](#client)
    * [New ticket](#new-ticket)
    * [Close tickets](#close-tickets)
    * [Unacknowledge tickets](#unacknowledge-tickets)

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
        "sid": 'XXXXXX...',
        "channel": "my-first-channel"
    },
    {
        "sid": 'YYYYYY...',
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

### Close tickets

Close one or more ticket(s) in DutyCalls.

#### Return value

```python
None
```

#### Example:

```python
# Closes ticket 123 and 456. The comment argument is optional.
await client.close_tickets(123, 456, comment='Closed by the DutyCalls SDK')
```

### Unacknowledge tickets

Un-acknowledge one or more ticket(s) in DutyCalls.

#### Return value

```python
None
```

#### Example:

```python
# Un-acknowledges ticket 123 and 456. The comment argument is optional.
await client.unacknowledge_tickets(123, 456, comment='Unacknowledged by the DutyCalls SDK'))
```
