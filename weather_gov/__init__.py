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

    def get(self, endpoint: str,
            params: dict = None,
            json_response: bool = True,
            feature_flags: list = None) -> dict:
    
        url = f"{self.API_BASE}/{endpoint}"
        if params: 
            url += "?" + urllib.parse.urlencode(params)
        
        headers = {'User-Agent': self.user_agent}
        
        if feature_flags:
            headers['Feature-Flags'] = feature_flags
        
        req = urllib.request.Request(url, data=None, headers=headers)
        with urllib.request.urlopen(req) as response: # ToDo: Handle urllib request errors
            if json_response:
                return json.loads(response.read().decode('utf-8'))
            return response.read().decode('utf-8')

    def glossary(self, **params) -> dict:
        return self.get("glossary", params)
