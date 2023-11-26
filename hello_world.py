from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def convert_temperature(celsius="0"):
    try:
        return f"{celsius} degree Celsius is equal to {convert_c_to_f(float(celsius))} degree Fahrenheit."
    except ValueError:
        return f"Please enter a valid celsius value in the URL."


def convert_c_to_f(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
