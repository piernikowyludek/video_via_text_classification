from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

segments, _ = model.transcribe("audio.mp3", 
                               vad_filter=True)
transcript = []
for segment in segments:
    transcript.append(segment.text)
transcript_str = ' '.join(transcript)