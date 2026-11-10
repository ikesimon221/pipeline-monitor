from app.database import SessionLocal
from app.models.segment import Segment

# Fictional pipeline segments for the simulator.
# Pressure is in bar, temperature in degrees Celsius, flow in cubic metres per hour.
SEGMENTS = [
    {
        "name": "Segment A - Bonny Terminal",
        "pressure_min": 55, "pressure_max": 70,
        "temperature_min": 30, "temperature_max": 50,
        "flow_min": 800, "flow_max": 1200,
    },
    {
        "name": "Segment B - Forcados Pump Station",
        "pressure_min": 60, "pressure_max": 80,
        "temperature_min": 35, "temperature_max": 55,
        "flow_min": 900, "flow_max": 1300,
    },
    {
        "name": "Segment C - Escravos Junction",
        "pressure_min": 45, "pressure_max": 65,
        "temperature_min": 28, "temperature_max": 48,
        "flow_min": 600, "flow_max": 1000,
    },
    {
        "name": "Segment D - Port Harcourt Refinery Inlet",
        "pressure_min": 40, "pressure_max": 60,
        "temperature_min": 25, "temperature_max": 45,
        "flow_min": 700, "flow_max": 1100,
    },
]

def seed():
    db = SessionLocal()
    try:
        for data in SEGMENTS:
            # Only add a segment if one with this name isn't already there
            existing = db.query(Segment).filter(Segment.name == data["name"]).first()
            if not existing:
                db.add(Segment(**data))
        db.commit()
        print("Seeding done. Segments in database:", db.query(Segment).count())
    finally:
        db.close()

if __name__ == "__main__":
    seed() 