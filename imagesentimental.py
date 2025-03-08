from deepface import DeepFace


def analyze_image_sentiment(image_path):
    try:
        # Analyze the image using DeepFace for emotion detection
        result = DeepFace.analyze(image_path, actions=['emotion'])

        # Extract the dominant emotion from the result
        dominant_emotion = result[0]['dominant_emotion']

        # Print the dominant emotion
        print(f"The dominant emotion in the image is: {dominant_emotion}")

        # Determine sentiment based on dominant emotion
        if dominant_emotion in ['happy', 'surprise']:
            return "Positive"
        elif dominant_emotion in ['angry', 'sad', 'fear']:
            return "Negative"
        else:
            return "Neutral"

    except Exception as e:
        print(f"Error analyzing image: {e}")
        return "Error"


def main():
    # Provide the path to your image
    image_path = input("Enter the path to the image: ")

    # Analyze the image and get sentiment
    sentiment = analyze_image_sentiment(image_path)
    print(f"The sentiment of the image is: {sentiment}")


if __name__ == "__main__":
    main()
