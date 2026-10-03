from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "ok": True,
        "service": "Code2APK Cloud",
        "version": "1.0"
    })


@app.get("/health")
def health():
    return jsonify({
        "ok": True,
        "service": "Code2APK Cloud"
    })


@app.post("/create-project")
def create_project():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "ok": False,
            "error": "No JSON data received"
        }), 400

    app_name = data.get("app_name", "").strip()
    package_id = data.get("package_id", "").strip()
    project_name = data.get("project_name", "").strip()

    if not app_name:
        return jsonify({
            "ok": False,
            "error": "app_name is required"
        }), 400

    if not package_id:
        return jsonify({
            "ok": False,
            "error": "package_id is required"
        }), 400

    if not project_name:
        return jsonify({
            "ok": False,
            "error": "project_name is required"
        }), 400

    return jsonify({
        "ok": True,
        "message": "Project received",
        "project": {
            "app_name": app_name,
            "package_id": package_id,
            "project_name": project_name
        }
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
