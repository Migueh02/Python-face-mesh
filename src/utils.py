import cv2
import mediapipe as mp

# inicializar los modulos de MediaPipe

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# configuracion del modelo de malla facial
def init_camera(width=640, height=480):
    """ Inicializa la camara con dimensiones personalizadas."""
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    
    return cap

# Funcion del rostro de malla facial
def draw_face_mesh(frame, results):
    """Dibuja la malla facial (color verde) sobre el frame"""
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                # draw small green landmarks and connections
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1)
            )
    
    return frame
        