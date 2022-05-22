import urllib.request
import urllib.parse
import uuid
import json
from pprint import pprint

class Client:
    def __init__(self, email: str=None):
        self.API_BASE = "https://api.weather.gov"
        self.user_agent = f"python-weather-gov|{str(uuid.uuid4())}|{email}"
        self.alerts = self._Alerts(self)
        self.gridpoints = self._Gridpoints(self)
        self.icons = self._Icons(self)
        self.thumbnails = self._Thumbnails(self)
        self.stations = self._Stations(self)
        self.offices = self._Offices(self)
        self.points = self._Points(self)
        self.radar = self._Radar(self)
        self.products = self._Products(self)
        self.zones = self._Zones(self)
    
    
    def get(self, endpoint: str, params: dict=None, json_response: bool=True) -> dict:
        url = f"{self.API_BASE}/{endpoint}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
            
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                    'User-Agent': self.user_agent
                    }
            )
        with urllib.request.urlopen(req) as response: # ToDo: Handle urllib request errors
            if json_response:
                return json.loads(response.read().decode('utf-8'))
            return response.read().decode('utf-8')
        

    class _Alerts:

        def __init__(self, parent) -> None:
            self.parent = parent
            
        def __call__(self, alertID: str=None, **params):
            """
            Parameters (depreciated but still supported):
            ----------
            active:  boolean
            List only active alerts (use /alerts/active endpoints instead)
            
            start: string
            Start time
            
            end: string
            End time
            
            status: array[string]
            Status (actual, exercise, system, test, draft)
            Available values : actual, exercise, system, test, draft
            
            message_type: array[string]
            Message type (alert, update, cancel)
            Available values : alert, update, cancel
            
            event: array[string]
            Event name
            
            code: array[string]
            Event code
            
            area: array
            State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone
            
            point: string
            Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone
            
            region: array[string]
            Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone
            Available values : AL, AT, GL, GM, PA, PI
            
            region_type: string
            Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone
            Available values : land, marine
            
            zone: array[string]
            Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type
            
            urgency: array[string]
            Urgency (immediate, expected, future, past, unknown)
            Available values : Immediate, Expected, Future, Past, Unknown
            
            severity: array[string]
            Severity (extreme, severe, moderate, minor, unknown)
            Available values : Extreme, Severe, Moderate, Minor, Unknown
            
            certainty: array[string]
            Certainty (observed, likely, possible, unlikely, unknown)
            Available values : Observed, Likely, Possible, Unlikely, Unknown
            
            limit: integer
            Limit
            
            cursor: string
            Pagination cursor
            """
            if alertID:
                return self.parent.get(f"alerts/{id}", params)
            return self.parent.get("alerts", params)
                
        def active(self, **params):
            """
            Parameters:
            ----------
            status: array[string]
            Status (actual, exercise, system, test, draft)
            Available values : actual, exercise, system, test, draft
            
            message_type: array[string]
            Message type (alert, update, cancel)
            Available values : alert, update, cancel
            
            event: array[string]
            Event name
            
            code: array[string]
            Event code
            
            area: array
            State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone
            
            point: string
            Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone
            
            region: array[string]
            Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone
            Available values : AL, AT, GL, GM, PA, PI
            
            region_type: string
            Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone
            Available values : land, marine
            
            zone: array[string]
            Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type
            
            urgency: array[string]
            Urgency (immediate, expected, future, past, unknown)
            Available values : Immediate, Expected, Future, Past, Unknown
            
            severity: array[string]
            Severity (extreme, severe, moderate, minor, unknown)
            Available values : Extreme, Severe, Moderate, Minor, Unknown
            
            certainty: array[string]
            Certainty (observed, likely, possible, unlikely, unknown)
            Available values : Observed, Likely, Possible, Unlikely, Unknown
            
            limit: integer
            Limit
            
            cursor: string
            Pagination cursor
            """
            return self.parent.get("alerts/active", params)
        
        def active_count(self, **params):
            return self.parent.get("alerts/active/count", params)
        
        def active_zone(self, zoneID: str, **params):
            return self.parent.get(f"alerts/active/zone/{zoneID}", params)
    
        def active_area(self, area: str, **params):
            return self.parent.get(f"alerts/active/area/{area}", params)
        
        def active_region(self, region: str, **params):
            return self.parent.get(f"alerts/active/region/{region}", params)
        
        def types(self, **params):
            return self.parent.get("alerts/types", params)

    def glossary(self, **params):
        return self.parent.get("glossary", params)
    
    class _Gridpoints:
        def __init__(self, parent) -> None:
            self.parent = parent
    
    class _Icons:
        def __init__(self, parent) -> None:
            self.parent = parent
    
    class _Thumbnails:
        def __init__(self, parent) -> None:
            self.parent = parent
    
    class _Stations:
        def __init__(self, parent) -> None:
            self.parent = parent
    class _Offices:
        def __init__(self, parent) -> None:
            self.parent = parent
    
    class _Points:
        def __init__(self, parent) -> None:
            self.parent = parent

    class _Radar:
        def __init__(self, parent) -> None:
            self.parent = parent
    
    class _Products:
        def __init__(self, parent) -> None:
            self.parent = parent
            
    class _Zones:
        def __init__(self, parent) -> None:
            self.parent = parent
    
