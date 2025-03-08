from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/biodata', methods=['GET'])
def get_biodata():
    return jsonify({
        "name": "Alpin Lubis",
        "education": "Mahasiswa",
        "major": "Teknik Informatika",
        "contact": "Tangerang-Indonesia",
        "music": "Musik"
    })

if __name__ == '__main__':
    app.run(debug=True)
