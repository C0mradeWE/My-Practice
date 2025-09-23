from flask import Flask, jsonify,request
app = Flask(__name__)
#داده های غیر واقعی
Temp_data = {

    "tehran":{"temperature":36, "status":"sunny"},
    "zanjan":{"temperature":21, "status":"cloudy"},
    "rasht":{"temperature":25, "status":"rainy"},
    "ardabil":{"temperature":27, "status":"sunny"}
}

@app.route('/weather')
def get_weather():
    city = request.args.get("city", "Unknown")
    if city.lower() in Temp_data:
        return jsonify({"city":city.lower(), **Temp_data[city.lower()]})
    else:
        return jsonify({"error":"city is not found!"}) ,404
    

if __name__=="__main__":
    app.run(debug=True)



"""اگر اشکالی بود حتما بگید
 
    ممنون
"""
