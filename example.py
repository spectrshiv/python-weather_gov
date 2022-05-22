import weather_gov


client = weather_gov.Client()

print(client.alerts(limit=1))