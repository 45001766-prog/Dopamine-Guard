import cv2
import mediapipe as mp
import socket
import os

SOCKET_PATH = "/tmp/dopamine_guard.sock"

if os.path.exists(SOCKET_PATH): os.remove(SOCKET_PATH)
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(SOCKET_PATH)
sock.listen(1)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
cap = cv2.VideoCapture(0)

print("IA en attente de connexion...")
conn, _ = sock.accept()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    
    # Données biométriques simulées transmises via Socket
    data = "EAR:0.31|POSTURE:0.12" 
    conn.send(data.encode())
    
    if cv2.waitKey(5) & 0xFF == 27: break

conn.close()
cap.release()