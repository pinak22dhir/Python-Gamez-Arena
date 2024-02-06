import cv2
import mediapipe as mp
import pygame

pygame.mixer.init()

# Dictionary mapping finger counts to corresponding sound files
sounds_mapping={
    1: "sounds/kick-bass.mp3",
    2: "sounds/crash.mp3",
    3: "sounds/snare.mp3",
    4: "sounds/tom-1.mp3",
    5: "sounds/tom-2.mp3",
    6: "sounds/tom-3.mp3",
    7: "sounds/cr78-Cymbal.mp3",
    8: "sounds/cr78-Guiro 1.mp3",
    9: "sounds/tempest-HiHat Metal.mp3",
    10: "sounds/cr78-Bongo High.mp3"
}

# MediaPipe setup for hand tracking
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_hands=mp.solutions.hands
# Open the camera capture
cap=cv2.VideoCapture(0)

# Initialize the hand tracking module from MediaPipe
with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    # Loop for processing video frames
    while cap.isOpened():
        # Capture a frame from the camera
        success, image=cap.read()
        # Check for an empty frame
        if not success:
            print("Ignoring empty camera frame.")
            continue
        # Convert BGR image to RGB for MediaPipe processing
        image.flags.writeable=False
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Process hand landmarks using MediaPipe
        results=hands.process(image)
        # Convert back to BGR for displaying
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        fingerCount=0
        
        if results.multi_hand_landmarks:
            # Loop over detected hands
            for hand_landmarks in results.multi_hand_landmarks:
                handIndex=results.multi_hand_landmarks.index(hand_landmarks)
                handLabel=results.multi_handedness[handIndex].classification[0].label
                handLandmarks=[]

                # Extract hand landmarks
                for landmark in hand_landmarks.landmark:
                    handLandmarks.append([landmark.x, landmark.y])
                # Count extended fingers based on hand landmarks
                if handLabel=="Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    fingerCount+=1
                elif handLabel=="Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    fingerCount+=1

                if handLandmarks[8][1] < handLandmarks[6][1]:
                    fingerCount+=1
                if handLandmarks[12][1] < handLandmarks[10][1]:
                    fingerCount+=1
                if handLandmarks[16][1] < handLandmarks[14][1]:
                    fingerCount+=1
                if handLandmarks[20][1] < handLandmarks[18][1]:
                    fingerCount+=1

                # Draw hand landmarks and connections on the frame
                mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # Play corresponding sound based on finger count
        if fingerCount in sounds_mapping:
            sound_file=sounds_mapping[fingerCount]
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # Add delay for a better audio experience
            if fingerCount <=5:
                pygame.time.delay(100)
            elif 5 < fingerCount <=9:
                pygame.time.delay(100)
                pygame.mixer.music.play()

            pygame.mixer.music.stop()

        # Display the finger count on the frame
        cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)
        cv2.imshow('MediaPipe Hands', image)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
            
cap.release()
cv2.destroyAllWindows()
