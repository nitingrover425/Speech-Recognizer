from flask import Flask, render_template, request, redirect

import speech_recognition as sr

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])

def index():
    transcript = ""
    if request.method == "POST":
        print("Audio File Received.")

        #check if file even exits (i.e. it's not just a "POST request" ping)
        if "file" not in request.files:
            return redirect(request.url)

        #check for blank file
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            
            #using google API
            transcript = recognizer.recognize_google(data, key=None) #use .wav audio samples

    return render_template("index.html", transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
