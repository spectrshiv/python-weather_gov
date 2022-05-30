from weather_gov import validations


class Base_Endpoint:
    def __init__(self, parent) -> None:
        self.parent = parent
        self._wfo = validations.VALID_WFO
        self._region = validations.VALID_REGION
        self._region_type = validations.VALID_REGION_TYPE
        self._urgency = validations.VALID_URGENCY
        self._severity = validations.VALID_SEVERITY
        self._certainty = validations.VALID_CERTAINTY
        self._zone_type = validations.VALID_ZONE_TYPE


class Alerts(Base_Endpoint):
    def __call__(self, alertID: str = None, **params) -> dict:

        if alertID:
            return self.parent.get(f"alerts/{alertID}", params)
        return self.parent.get("alerts", params)

    def active(self, **params) -> dict:

        return self.parent.get("alerts/active", params)
    
    def active_count(self, **params) -> dict:
        return self.parent.get("alerts/active/count", params)
    
    def active_zone(self, zoneID: str, **params) -> dict:
        return self.parent.get(f"alerts/active/zone/{zoneID}", params)

    def active_area(self, area: str, **params) -> dict:
        return self.parent.get(f"alerts/active/area/{area}", params)
    
    def active_region(self, region: str, **params) -> dict:
        
        return self.parent.get(f"alerts/active/region/{region}", params)
    
    def types(self, **params) -> dict:
        return self.parent.get("alerts/types", params)


class Gridpoints(Base_Endpoint):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._features = validations.VALID_GRIDPOINT_FORCAST_FEATURES
    
    def __call__(self, wfo:str, x:int, y:int, **params) -> dict:
        if wfo not in self._wfo:
            raise ValueError(f"{wfo} is not a valid WFO")
        self.parent.get(f"gridpoints/{wfo}/{x}/{y}", params)
        
    def forcast(self, wfo:str, x:int, y:int, features: list = None, **params) -> dict:
        for feature in features:
            if feature not in self._features:
                raise ValueError(f"{feature} is not a valid feature")
        if wfo not in self._wfo:
            raise ValueError(f"{wfo} is not a valid WFO")
        return self.parent.get(f"gridpoints/{wfo}/{x}/{y}/forecast", params, feature_flags=features)
    
    def forecast_hourly(self, wfo:str, x:int, y:int, features: list = None, **params) -> dict:
        for feature in features:
            if feature not in self._features:
                raise ValueError(f"{feature} is not a valid feature")
        if wfo not in self._wfo:
            raise ValueError(f"{wfo} is not a valid WFO")
        return self.parent.get(f"gridpoints/{wfo}/{x}/{y}/forecast/hourly", params, feature_flags=features)

    def stations(self, wfo:str, x:int, y:int, **params) -> dict:
        if wfo not in self._wfo:
            raise ValueError(f"{wfo} is not a valid WFO")
        return self.parent.get(f"gridpoints/{wfo}/{x}/{y}/stations", params)


class Stations:
    def __init__(self, parent) -> None:
        self.parent = parent
        
    def __call__(self, **params) -> dict: 
        return self.parent.get("stations", params)
    
    def id(self, stationID: str, **params) -> dict:
        return self.parent.get(f"stations/{stationID}", params)
    
    def id_observations(self, stationID: str, **params) -> dict:
        return self.parent.get(f"stations/{stationID}/observations", params)
    
    def id_observations_latest(self, stationID: str, **params) -> dict:
        return self.parent.get(f"stations/{stationID}/observations/latest", params)
    
    def id_observations_time(self, stationID: str, time:str,  **params) -> dict:
        return self.parent.get(f"stations/{stationID}/observations/{time}", params)
    
class Offices(Base_Endpoint):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
    def __call__(self, **params) -> dict:
        return self.parent.get("offices", params)
    
    def id(self, officeID: str, **params) -> dict:
        if officeID not in self._wfo:
            raise ValueError(f"{officeID} is not a valid WFO")
        return self.parent.get(f"offices/{officeID}", params)
    
    def headlines(self, officeID: str, **params) -> dict:
        if officeID not in self._wfo:
            raise ValueError(f"{officeID} is not a valid WFO")
        return self.parent.get(f"offices/{officeID}/headlines", params)

    def headline_id(self, officeID: str, headlineID: str, **params) -> dict:
        if officeID not in self._wfo:
            raise ValueError(f"{officeID} is not a valid WFO")
        return self.parent.get(f"offices/{officeID}/headlines/{headlineID}", params)


class Points:
    def __init__(self, parent) -> None:
        self.parent = parent

    def __call__(self) -> dict:
        raise NotImplementedError("Points() method is not implemented")

    def id(self, pointID: str, **params) -> dict:
        return self.parent.get(f"points/{pointID}", params)
        
        
class Radar(Base_Endpoint):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
    def __call__(self) -> dict:
        raise NotImplementedError("Radar() method is not implemented")

    def servers(self, **params) -> dict:
        return self.parent.get("radar/servers", params)

    def server_id(self, serverID: str, **params) -> dict:
        return self.parent.get(f"radar/servers/{serverID}", params)

    def stations(self, **params) -> dict:
        return self.parent.get("radar/stations", params)

    def station_id(self, stationID: str, **params) -> dict:
        return self.parent.get(f"radar/stations/{stationID}", params)

    def station_id_alarms(self, stationID: str, **params) -> dict:
        return self.parent.get(f"radar/stations/{stationID}/alarms", params)

    def queues(self, host:str, **params) -> dict:
        return self.parent.get(f"radar/queues/{host}", params)


class Products:
    def __init__(self, parent) -> None:
        self.parent = parent

    def __call__(self, **params) -> dict:
        return self.parent.get("products", params)

    def locations(self, **params) -> dict:
        return self.parent.get("products/locations", params)

    def types(self, **params) -> dict:
        return self.parent.get("products/types", params)

    def id(self, productID: str, **params) -> dict:
        return self.parent.get(f"products/{productID}", params)

    def type_id(self, typeID: str, **params) -> dict:
        return self.parent.get(f"products/types/{typeID}", params)

    def type_id_locations(self, typeID: str, **params) -> dict:
        return self.parent.get(f"products/types/{typeID}/locations", params)

    def location_id_types(self, locationID: str, **params) -> dict:
        return self.parent.get(f"products/locations/{locationID}/types", params)

    def type_id_location_id(self, typeID: str, locationID: str, **params) -> dict:
        return self.parent.get(f"products/types/{typeID}/locations/{locationID}", params)


class Zones(Base_Endpoint):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def __call__(self, **params) -> dict:
        self.parent.get("zones", params)

    def type(self, zoneType: str, **params) -> dict:
        if zoneType not in self._zone_type:
            raise ValueError(f"{zoneType} is not a valid zone type")
        return self.parent.get(f"zones/types/{zoneType}", params)

    def type_zone_id(self, zoneType: str, zoneID: str, **params) -> dict:
        if zoneType not in self._zone_type:
            raise ValueError(f"{zoneType} is not a valid zone type")
        return self.parent.get(f"zones/types/{zoneType}/{zoneID}", params)

    def type_zone_id_forecast(self, zoneType: str, zoneID: str, **params) -> dict:
        if zoneType not in self._zone_type:
            raise ValueError(f"{zoneType} is not a valid zone type")
        return self.parent.get(f"zones/types/{zoneType}/{zoneID}/forecast", params)

    def forecast_id_observations(self, zoneID: str, **params) -> dict:
        return self.parent.get(f"zones/forecasts/{zoneID}/observations", params)

    def forecast_id_stations(self, zoneID: str, **params) -> dict:
        return self.parent.get(f"zones/forecasts/{zoneID}/stations", params)
