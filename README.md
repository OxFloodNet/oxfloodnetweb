# Oxford Flood Network Web Interface

This Flask application provides an interface to show all of the Oxford Flood Network sensors that are active, and their current status.

## Status

Not currently developed - a fork was made from Sushack, but the full IoT stack needs to be re-implemented before this will function. 

## Installation

First clone this repository to your computer somewhere, such as ~/oxfloodnetweb/

```bash
cd ~/oxfloodnetweb
mkvirtualenv oxfloodnet
workon oxfloodnet
pip install -r requirements.txt
```

## Running the application

While working on `oxfloodnet`, run the following from your terminal:

```bash
python server.py
```

Now you can view the web interface by visiting http://localhost:5000.


## Todo:

- Finish the reverse Geo lookup from Postcode stuff
- Get a scalable/sustainable database source
- Add information about each sensor to the display when tapping an icon
