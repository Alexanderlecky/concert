from models import Band, Venue, Concert, Base
from config import engine, session

# Create tables (only if not already created by migrations)
Base.metadata.create_all(engine)

# Add sample data to the database
def add_sample_data():
    if not session.query(Band).first():
        band = Band(name="The Rolling Stones", hometown="London")
        venue = Venue(title="Madison Square Garden", city="New York")
        concert = Concert(date="2024-09-15", band=band, venue=venue)

        session.add_all([band, venue, concert])
        session.commit()

# Query and print data
def print_data():
    band = session.query(Band).first()
    venue = session.query(Venue).first()
    concert = session.query(Concert).first()

    print(f"Band: {band.name}, Hometown: {band.hometown}")
    print(f"Venue: {venue.title}, City: {venue.city}")
    print(f"Concert Date: {concert.date}, Band: {concert.band.name}, Venue: {concert.venue.title}")

if __name__ == "__main__":
    add_sample_data()
    print_data()
