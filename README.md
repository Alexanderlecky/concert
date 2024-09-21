# 🎸 Concerts Project

A concert management system built with **SQLAlchemy** to manage bands, venues, and concerts. This application allows users to explore bands, venues, and concerts, manage bookings, and track the history of performances.

## Table of Contents

1. [Features](#features)
2. [Technologies](#technologies)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Database Models](#database-models)
5. [Usage](#usage)
   - [Object Relationship Methods](#object-relationship-methods)
   - [Aggregate and Relationship Methods](#aggregate-and-relationship-methods)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- Manage and view bands, venues, and concerts.
- Track concerts by date and venue.
- Query band performances and venues efficiently.
- Perform automatic migrations to manage database schema changes.

## Technologies

- **Python 3.8+**
- **SQLAlchemy**
- **Alembic** (for database migrations)
- **SQLite** (as the database)

## Getting Started

### Prerequisites

Before running the project, ensure you have the following tools installed:

- **Python** (version 3.8+)
- **Pipenv** or **virtualenv** for managing the virtual environment
- **SQLite** (if using another database, update the configuration)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Alexanderlecky/concerts.git
    cd concerts_project
    ```

2. **Create a virtual environment**:

    If using `Pipenv`:

    ```bash
    pipenv install
    pipenv shell
    ```

    If using `virtualenv`:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:

    Run migrations to create the necessary tables.

    ```bash
    alembic upgrade head
    ```

5. **Seed the database** (optional):

    Populate the database with sample data for testing.

    ```bash
    python seed.py
    ```

6. **Run the application**:

    The app is managed via `app.py`, where you can interact with the database.

    ```bash
    python app.py
    ```

## Database Models

- **Band**: Represents musical bands with fields like `name` and `hometown`.
- **Venue**: Represents venues where concerts are held, with fields like `title` and `city`.
- **Concert**: Represents individual concerts, including the date, band, and venue.

### Band

| Field    | Type                      |
|----------|---------------------------|
| id       | Integer (Primary Key)      |
| name     | String                     |
| hometown | String                     |

### Venue

| Field  | Type                      |
|--------|---------------------------|
| id     | Integer (Primary Key)      |
| title  | String                     |
| city   | String                     |

### Concert

| Field    | Type                      |
|----------|---------------------------|
| id       | Integer (Primary Key)      |
| band_id  | Foreign Key (Band)         |
| venue_id | Foreign Key (Venue)        |
| date     | Date                       |

## Usage

### Object Relationship Methods

Each model contains specific methods for easy querying:

- **Concert**
  - `concert.band()` → Returns the band associated with the concert.
  - `concert.venue()` → Returns the venue where the concert is held.
  
- **Venue**
  - `venue.concerts()` → Returns all concerts held at the venue.
  - `venue.bands()` → Returns all bands that have performed at the venue.
  
- **Band**
  - `band.concerts()` → Returns all concerts the band has performed in.
  - `band.venues()` → Returns all venues where the band has performed.

### Aggregate and Relationship Methods

- **Concert**
  - `hometown_show()` → Returns `True` if the concert is in the band's hometown.
  - `introduction()` → Returns the introduction for the concert in the format: `"Hello {city}!!!!! We are {band name} and we're from {hometown}"`.
  
- **Band**
  - `play_in_venue(venue, date)` → Books a concert at the given venue on the given date.
  - `all_introductions()` → Returns a list of introductions for every concert the band has played.
  - `most_performances()` → Returns the band that has played the most concerts.
  
- **Venue**
  - `concert_on(date)` → Returns the concert on the given date at the venue.
  - `most_frequent_band()` → Returns the band that has performed the most concerts at the venue.

### Testing the Methods

You can query the data and relationships using SQLAlchemy. For example:

```python
# Get the first band and print the venues they've performed at
band = session.query(Band).first()
print(band.venues())

# Get the first venue and print all concerts held there
venue = session.query(Venue).first()
print(venue.concerts())
