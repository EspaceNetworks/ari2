
import json
import httplib
import urllib
from base64 import b64encode


class Client(object):
    def __init__(self, host, username="asterisk", password="asterisk", port=8088):
        self._host = host
        self._port = port
        #
        self._username = username
        self._password = password
        #
        self._conn = httplib.HTTPConnection(host=self._host, port=self._port)

    def dipsose(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def _request(self, uri, method="GET", params=None):
        result = None
        userAndPass = b64encode(b"{username}:{password}".format(username=self._username, password=self._password)).decode("ascii")
        headers = {
            "Authorization": "Basic {userAndPass}".format(userAndPass=userAndPass)
        }
        query_params = urllib.urlencode(params)
        request_uri = "{uri}?{query_params}".format(uri=uri, query_params=query_params)
        print(request_uri)
        self._conn.request(method, request_uri, None, headers)
        res = self._conn.getresponse()
        data = res.read()
        result = json.loads(data)
        if res.status in [400]:
            msg = result.get("message", "Unknown Error")
            raise ValueError(msg)
        return result

    def create_channel(self, endpoint, extension, context="default"):
        uri = "/ari/channels"
        params = {
            "endpoint": endpoint,
            "extension": extension,
            "context": context,
        }
        result = self._request(method="POST", uri=uri, params=params)
        print result