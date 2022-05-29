# python-weather_gov

An API wrapper for Weather.gov made in base Python.

## Example

```
import weather_gov


client = weather_gov.Client()

print(client.alerts(limit=1))

```

# Links 

- [National Weather Service web api overview](https://www.weather.gov/documentation/services-web-api#/)
- [OpenAPI Spec](https://api.weather.gov/openapi.json)
- [Weather.gov Github](https://weather-gov.github.io/api/)
