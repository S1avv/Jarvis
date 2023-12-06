from run import record_audio, recognize_speech
from plyer import notification
import time

if __name__ == "__main__":
    def send_notification(title, message, app_name):
        notification.notify(
            title=title,
            message=message,
            app_name=app_name,
            app_icon=None,
            timeout=10,
        )

    send_notification("JARVIS", "Джарвис внимательно вас слушает...", "JARVIS")

    audio_data = record_audio()
    recognize_speech(audio_data)