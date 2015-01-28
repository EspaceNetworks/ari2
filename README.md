# ari2

Asterisk RESTful Interface - yet another implementation based on httplib

Example:

```python
#!/usr/bin/env python
 
import time

import ari2.manager

 
manager = ari2.manager.Client(host="192.168.0.1", username='asterisk', password='asterisk')

channel1 = manager.create_channel(endpoint="SIP/user0100", extension="0200", context="int")
#channel2 = manager.create_channel(endpoint="SIP/user0200", extension="0200")
```
