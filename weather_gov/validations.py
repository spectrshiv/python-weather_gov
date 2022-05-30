""" Validation constants. Not completely implemented for custom parameters."""

VALID_WFO = ["AKQ", "ALY", "BGM", "BOX", "BTV", "BUF", "CAE",
            "CAR", "CHS", "CLE", "CTP", "GSP", "GYX", "ILM",
            "ILN", "LWX", "MHX", "OKX", "PBZ", "PHI", "RAH",
            "RLX", "RNK", "ABQ", "AMA", "BMX", "BRO", "CRP",
            "EPZ", "EWX", "FFC", "FWD", "HGX", "HUN", "JAN",
            "JAX", "KEY", "LCH", "LIX", "LUB", "LZK", "MAF",
            "MEG", "MFL", "MLB", "MOB", "MRX", "OHX", "OUN",
            "SHV", "SJT", "SJU", "TAE", "TBW", "TSA", "ABR",
            "APX", "ARX", "BIS", "BOU", "CYS", "DDC", "DLH",
            "DMX", "DTX", "DVN", "EAX", "FGF", "FSD", "GID",
            "GJT", "GLD", "GRB", "GRR", "ICT", "ILX", "IND",
            "IWX", "JKL", "LBF", "LMK", "LOT", "LSX", "MKX",
            "MPX", "MQT", "OAX", "PAH", "PUB", "RIW", "SGF",
            "TOP", "UNR", "BOI", "BYZ", "EKA", "FGZ", "GGW",
            "HNX", "LKN", "LOX", "MFR", "MSO", "MTR", "OTX",
            "PDT", "PIH", "PQR", "PSR", "REV", "SEW", "SGX",
            "SLC", "STO", "TFX", "TWC", "VEF", "AER", "AFC",
            "AFG", "AJK", "ALU", "GUM", "HPA", "HFO", "PPG",
            "STU", "NH1", "NH2", "ONA", "ONP"]

# States
VALID_STATE = ["AL", "AK", "AS", "AR", "AZ", "CA", "CO", "CT",
                   "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL",
                   "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA",
                   "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
                   "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",
                   "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT",
                   "VT", "VI", "VA", "WA", "WV", "WI", "WY"]

# Marine area codes (NWS Directive 10-302)
VALID_MARINE_AREA_CODE = ["AM", "AN", "GM", "LC", "LE", "LH", "LM",
                           "LO","LS", "PH", "PK", "PM", "PS", "PZ", "SL"]

VALID_MARINE_REGION_CODE = ["AL", "AT", "GL", "GM", "PA", "PI"]

VALID_LAND_REGION_CODE = ["AR", "CR", "ER", "PR", "SR", "WR"]

VALID_AREA_CODE = VALID_STATE + VALID_MARINE_AREA_CODE

VALID_REGION = ["AL", "AT", "GL", "GM", "PA", "PI"]

VALID_REGION_TYPE = ["land", "marine"]

VALID_URGENCY = ["Immediate", "Expected", "Future", "Past", "Unknown"]

VALID_SEVERITY = ["Extreme", "Severe", "Moderate", "Minor", "Unknown"]

VALID_CERTAINTY = ["Observed", "Likely", "Possible", "Unlikely", "Unknown"]

VALID_UNITS = ["us","si"]

VALID_GRIDPOINT_FORCAST_FEATURES = ["forecast_temperature_qv", "forecast_wind_speed_qv"]

VALID_ALERT_STATUS = ["Actual", "Exercise", "System", "Test", "Draft"]

VALID_ALERT_MESSAGE_TYPE = ["Alert", "Update", "Cancel", "Ack", "Error"]

VALID_ALERT_CATEGORY = ["Met", "Geo", "Safety", "Security", "Rescue", "Fire",
                        "Health", "Env", "Transport", "Infra", "CBRNE", "Other"]

VALID_ALERT_SEVERITY = VALID_SEVERITY

VALID_ALERT_CERTAINTY = VALID_CERTAINTY

VALID_ALERT_URGENCY = VALID_URGENCY

VALID_ALERT_RESPONSE = ["Shelter", "Evacuate", "Prepare", "Execute",
                        "Avoid", "Monitor", "Assess", "AllClear", "None"]

VALID_ZONE_TYPE = [ "land", "marine", "forecast", "public", "coastal",
                   "offshore", "fire", "county"]
