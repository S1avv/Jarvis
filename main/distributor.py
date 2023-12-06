from commands.system.google import open_google, close_google
from commands.system.open_programm import start_process
from main.play_voice_acrive import play, play_mp3
from commands.system.volume import set_volume
import time
def dist_text(text: None):
    text = text.lower()

    if text is None:
        print("None")
        return None

    elif any(i in text for i in ["открыть google", "google откройся", "запусти google", "включи google", "открой гугл"]):
        open_google()
        play()
        return 0

    elif any(i in text for i in ["закрыть google", "google закройся", "отключи google", "закрой google", "закрой гугл"]):
        close_google("chrome.exe")
        play()
        return 0

    elif any(i in text for i in ["спасибо", "молодец", "благодарю", "уважаю"]):
        play_mp3("../voice_acting/Always_at_your_service.wav")
        return 0

    elif any(i in text for i in ["привет", "приветствую", "добрый день", "здравствуйте", "доброе утро"]):
        play_mp3("../voice_acting/hello.wav")
        return 0

    elif any(i in text for i in ["открой"]):
        start_process(text)
        play()
        return 0

    elif any(i in text for i in ["выключи звук", "отключи звук"]):
        play()
        time.sleep(1)
        set_volume(0)
        return 0

    elif any(i in text for i in ["включи звук", "активируй звук"]):
        set_volume(0.2)
        play()
        return 0

    elif text in ["джарвис", "jarvis", ]:
        play_mp3("../voice_acting/request_completed_a.wav")
        return 0

    else:
        print("Ошибка")
        return None

