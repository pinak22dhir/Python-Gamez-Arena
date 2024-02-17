import mediapipe as mp
import cv2
import random

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
score = 0

x_coord = random.randint(50, 600)
y_coord = random.randint(50, 400)

def CreateCaptureCircle(image):
    global x_coord, y_coord
    cv2.circle(image, (x_coord, y_coord), 25, (0, 200, 0), 5)

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        image_height, image_width, _ = image.shape
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 255)
        text = cv2.putText(image, "Score", (480, 30), font, 1, color, 4, cv2.LINE_AA)
        text = cv2.putText(image, str(score), (590, 30), font, 1, color, 4, cv2.LINE_AA)

        CreateCaptureCircle(image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))

                if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]:
                    finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    pixel_x, pixel_y = int(finger_tip.x * image_width), int(finger_tip.y * image_height)
                    cv2.circle(image, (pixel_x, pixel_y), 25, (0, 0, 255), 5)

                    if abs(pixel_x - x_coord) <= 25 and abs(pixel_y - y_coord) <= 25:
                        print("Collision detected!")
                        x_coord = random.randint(50, 600)
                        y_coord = random.randint(50, 400)
                        score += 1

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print(score)
            break

video.release()
cv2.destroyAllWindows()