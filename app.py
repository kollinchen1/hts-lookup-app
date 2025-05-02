from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/lookup", methods=["GET"])
def lookup():
    part = request.args.get("part")
    if not part:
        return jsonify({"error": "Missing part number"}), 400

    base_url = "https://sapapi.advantech.com/api/Materials/GetMaterialImportExportData"
    query_url = f"{base_url}?salesOrg=US01&partNumber={part}"

    try:
        r = requests.get(query_url, timeout=10)
        r.raise_for_status()
        data = r.json()
        first = data[0] if isinstance(data, list) and len(data) > 0 else data
        result = {
            "HTS": first.get("hts"),
            "COO": first.get("coo"),
            "HTSDescription": first.get("htsDescription"),
            "part": part
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
