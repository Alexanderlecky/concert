from models import Band, Venue, Concert
from config import session


def seed_data():
    # bands
    band1 = Band(name="The Rolling Stones", hometown="London")
    band2 = Band(name="Pink Floyd", hometown="Cambridge")
    band3 = Band(name="The Beatles", hometown="Liverpool")

    # venues
    venue1 = Venue(title="Madison Square Garden", city="New York")
    venue2 = Venue(title="Wembley Stadium", city="London")
    venue3 = Venue(title="The O2 Arena", city="London")

    # concerts
    concert1 = Concert(band=band1, venue=venue1, date="2023-05-21")
    concert2 = Concert(band=band2, venue=venue2, date="2023-06-15")
    concert3 = Concert(band=band3, venue=venue3, date="2023-07-10")
    concert4 = Concert(band=band1, venue=venue2, date="2023-08-05")

    # Add instances to the session and commit them to the database
    session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3, concert4])
    session.commit()

    print("Data seeded successfully!")


if __name__ == '__main__':
    seed_data()
