import subprocess
import whisper

model = whisper.load_model("small")

subprocess.run(["ffmpeg","-i","input.mp4","OUTPUT.mp3"])

result = model.transcribe("OUTPUT.mp3")
print("video to text\n :",result["text"])