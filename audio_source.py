from libs.audio.pcm import b64_to_int16
def parse_audio_msg(msg: dict) -> bytes | None:
    if msg.get("type") != "audio": return None
    return b64_to_int16(msg["pcm16_b64"])  # int16 LE
