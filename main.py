# # This is a sample Python script.
#
# # Press ?R to execute it or replace it with your code.
# # Press Double ? to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ?F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('Zach')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from flask import Flask, jsonify
import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=4RY54UYZY5AGHQE7'

r = requests.get(url)
data = r.json()

app = Flask(__name__)

@app.route("/stockData", methods=['GET', 'POST'])
def running():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# is this gonna show up