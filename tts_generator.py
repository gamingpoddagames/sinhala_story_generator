    timport asyncio
import edge_tts

TEXT = "අද ලෝකයෙන් විශේෂ පුවතක්."

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        voice="si-LK-SameeraNeural",
        rate="-10%"
    )

    await communicate.save("/storage/emulated/0/Download/news.mp3")
    print("DONE")

asyncio.run(main())assets
