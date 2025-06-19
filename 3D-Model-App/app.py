import pymongo # type: ignore
import plotly.graph_objects as go # type: ignore
import trimesh # type: ignore
import time
import threading
from flask import Flask, render_template, jsonify # type: ignore

app = Flask(__name__)

# MongoDB setup
client = pymongo.MongoClient(
    "mongodb+srv://avinashshan333:weDnc91w3TMWj47p@cluster0.j0igu.mongodb.net/nova?retryWrites=true&w=majority&appName=Cluster0",
    tz_aware=True,
    serverSelectionTimeoutMS=5000
)
db = client["nova"]
collection = db["sensordatas"]

# Load 3D model
mesh_data = trimesh.load_mesh('models/your_model.stl')
vertices = mesh_data.vertices
faces = mesh_data.faces
x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]

# Initial sensor data
sensor_data = {
    "waterLevelPercent": 0,
    "flowRate": 0,
    "undergroundTankFull": False,
    "totalWaterUsed": 0
}

# Update sensor data from MongoDB
def fetch_sensor_data():
    global sensor_data
    while True:
        latest_data = collection.find().sort("timestamp", pymongo.DESCENDING).limit(1)
        if collection.count_documents({}) > 0:
            for sensor in latest_data:
                sensor_data["waterLevelPercent"] = sensor.get("waterLevelPercent", 0)
                sensor_data["flowRate"] = sensor.get("flowRate", 0)
                sensor_data["undergroundTankFull"] = sensor.get("undergroundTankFull", False)
                sensor_data["totalWaterUsed"] = sensor.get("totalWaterUsed", 0)
        time.sleep(5)

# Route to render Plotly graph
@app.route('/')
def index():
    fig = go.Figure()

    # 3D Model
    fig.add_trace(go.Mesh3d(
        x=x, y=y, z=z,
        i=faces[:, 0], j=faces[:, 1], k=faces[:, 2],
        opacity=0.5,
        color='lightgray',
        name="3D Model"
    ))

    # Sensor data points
    fig.add_trace(go.Scatter3d(x=[3.91586], y=[-2.456727], z=[5.052287], 
                               mode='text', text=[f"Water Level: {sensor_data['waterLevelPercent']}%"], 
                               name="Water Level"))
    
    fig.add_trace(go.Scatter3d(x=[4.478922], y=[-3.702904], z=[1.521611], 
                               mode='text', text=[f"Flow Rate: {sensor_data['flowRate']} L/min"], 
                               name="Flow Rate"))
    
    fig.add_trace(go.Scatter3d(x=[4.9], y=[-1.5], z=[-1], 
                               mode='text', text=[f"Underground Tank: {'Full' if sensor_data['undergroundTankFull'] else 'Low'}"], 
                               name="Underground Tank"))
    
    fig.add_trace(go.Scatter3d(x=[4.6], y=[-3.702904], z=[1.2], 
                               mode='text', text=[f"Total Water Used: {sensor_data['totalWaterUsed']} L"], 
                               name="Total Water Used"))

    fig.update_layout(
        scene=dict(
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
            zaxis_title='Z Axis',
            camera=dict(eye=dict(x=2, y=2, z=2))
        ),
        title="Real-Time 3D Model with Sensor Data",
        margin=dict(l=0, r=0, b=0, t=40)
    )

    graph_html = fig.to_html(full_html=False)
    return render_template('index.html', graph=graph_html)

# Real-time data fetch
@app.route('/sensor-data')
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    threading.Thread(target=fetch_sensor_data, daemon=True).start()
    app.run(debug=True)


