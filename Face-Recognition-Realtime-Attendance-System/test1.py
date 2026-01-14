import cv2
import matplotlib.pyplot as plt

# Load your image using OpenCV
imgBackground = cv2.imread('image.png')

# Display the image using Matplotlib
plt.imshow(cv2.cvtColor(imgBackground, cv2.COLOR_BGR2RGB))
plt.title('Face Attendance')
plt.show()
