from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/api/search')
def search():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400
    stock = yf.Ticker(symbol)
    info = stock.info
    return jsonify({'info': info})

@app.route('/api/quote')
def quote():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'No symbol provided'}), 400
    stock = yf.Ticker(symbol)
    price = stock.history(period='1d')
    return jsonify({'price': price['Close'][-1] if not price.empty else None})

# Add more endpoints for history, indicators, news, etc.

if __name__ == '__main__':
    app.run(debug=True)
