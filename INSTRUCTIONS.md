### To Run:

- Activate the virtual environment: `. venv/bin/activate`
- Run the program with gunicorn: `gunicorn run:app`
- In a new terminal, fire up ngrok tunnel using the same port: `./ngrok http 8000`
- Copy the tunnel's IP address, and apply it to tradingview's alerts

