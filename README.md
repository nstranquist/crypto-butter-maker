# Trading Program for TradingView Signals and Kucoin

To the moon...!

### Setup

- Make sure you have python3 and pip3 installed
- Make sure you have installed ngrok

### Getting Started

1. Create a `.env` file in root of the project and add the contents:
  - API_KEY="YOUR-API-KEY"
  - API_SECRET="YOUR-API-SECRET-KEY"
  - API_PASSPHRASE="YOUR-API-PASSPHRASE"

2. If desired, modify the `.flaskenv` file to your liking. This will affect the port and some metadata about the flask app

3. To conduct tests, check out scripts in the `/tests` directory

### To Run the Program

1. Create the python virtual environment if it hasn't already been created
  - `python3 -m venv venv`

2. Activate the virtual environment
  - `. venv/bin/activate`

3. Install python modules if its your first time running the program
  - `pip install`

4. Run the app with Gunicorn
  - `gunicorn run:app`

5. In a new terminal window, run the ngrok instance
  - If locally: `./ngrok http 8000`
  - If to uri: `./ngrok tcp --remote-addr=your-address 8000`

6. If logs are shown, the program should be running. It will log when new trades come in