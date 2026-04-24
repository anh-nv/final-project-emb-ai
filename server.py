""" Final project to detect emotion """

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initialize flask instance
app = Flask("Emotion detection")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' this code receive text and analyze its emotion '''
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze != "":
        result = emotion_detector(text_to_analyze)
        if result is not None:
            formatted_result = f"For the given statement, the system response is \
            'anger': {str(result['anger'])}, \
            'disgust': {str(result['disgust'])}, \
            'fear': {str(result['fear'])}, \
            'joy': {str(result['joy'])}, \
             and 'sadness': {str(result['sadness'])}. \
             The dominant emotion is {result['dominant_emotion']}."
        else:
            formatted_result = "Invalid input! Try again"
    else:
        formatted_result = "Nothing was entered! Try again"
    return formatted_result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)
