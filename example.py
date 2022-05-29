import weather_gov
from pprint import pprint


client = weather_gov.Client()

pprint(client.alerts(limit=5, urgency="Immediate"))