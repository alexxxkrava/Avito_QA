def create_values(co2_value, energy_value, water_value):
    return {
        "result": {
            "blocks": {
                "personalImpact": {
                    "data": {
                        "co2": co2_value,
                        "energy": energy_value,
                        "materials": 0,
                        "pineYears": 0,
                        "water": water_value
                    }
                }
            },
            "isAuthorized": 'false'
        },
        "status": "ok"
    }


