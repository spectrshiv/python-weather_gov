import urllib.request
import urllib.parse
import json
from weather_gov import endpoints


class Client:
    def __init__(self, email: str = None) -> None:
        self.API_BASE = "https://api.weather.gov"
        self.user_agent = f"python-weather-gov|{email}"
        self.alerts = endpoints.Alerts(self)
        self.gridpoints = endpoints.Gridpoints(self)
        self.stations = endpoints.Stations(self)
        self.offices = endpoints.Offices(self)
        self.points = endpoints.Points(self)
        self.radar = endpoints.Radar(self)
        self.products = endpoints.Products(self)
        self.zones = endpoints.Zones(self)

    def get(
        self,
        endpoint: str,
        params: dict = None,
        json_response: bool = True,
        feature_flags: list = None,
    ) -> dict:

        url = f"{self.API_BASE}/{endpoint}"
        if params:
            url += "?" + urllib.parse.urlencode(params)

        headers = {"User-Agent": self.user_agent}

        ## XXX: Including these headers breaks retreival?
        if False and feature_flags:
            headers["Feature-Flags"] = feature_flags

        req = urllib.request.Request(url, data=None, headers=headers)

        response = None

        try:
            response = urllib.request.urlopen(req)

        except urllib.error.HTTPError as exc:
            print("HTTP error {}: {} ({})".format(exc.code, exc.reason, url))
            sys.exit(1)

        except urllib.error.URLError as exc:
            print("urllib get failed: {}".format(exc.reason))
            sys.exit(1)

        except Exception as exc:
            print("Unhandled exception on [{}]: {}, {}".format(url, exc, exc.reason))
            sys.exit(1)

        if response:
            if json_response:
                return json.loads(response.read().decode("utf-8"))
            return response.read().decode("utf-8")

    def glossary(self, **params) -> dict:
        return self.get("glossary", params)
