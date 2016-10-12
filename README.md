# Ninjalog.py

ninjalog is a secure, open source web service for centralized logging. Checkout [ninjalog.io](http://www.ninjalog.io) to create a free account. This package includes a python logging handler class, allowing your log data to be sent directly to the cloud instead of to disk.

ninjalog.io uses [jwt](http://jwt.io) authentication with rails 5 websockets for live log tailing. Data is persisted via redis and can be downloaded to disk.

## Installation

Add this line to your application's requirements.txt:

```python
ninjalog
```

And then execute:

    $ pip install -r requirements.txt

Or install it yourself as:

    $ pip install ninjalog

## Usage

Create a new python logger and add a NinjaLogger handler to it. Your ninjalog.io email account and generated client_id and client_secret will be required to initialize the NinjaLogger.

```python
from ninjalog import NinjaLogger
import logging

logger = logging.getLogger('ninjalog')
logger.setLevel(logging.DEBUG)
logger.addHandler(NinjaLogger(email, client_id, client_secret))

logger.info('Logging to the cloud. weeee')
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/tysonholub/ninjalog.py. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
