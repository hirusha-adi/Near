import typing as t
import yt_dlp, os, re
from loguru import logger

YTDLP_PROXY_URL: str = os.getenv("YTDLP_PROXY_URL")

def extract_video_id(url) -> t.Optional[str]:
    """Extracts the YouTube video ID from various YouTube URL formats."""
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

def download_video(url: str) -> t.Optional[t.Tuple[str, str]]:
    logger.debug(f"Downloading: {url}")
    video_id = extract_video_id(url)
    logger.debug(f"Video ID: {video_id}")

    if not video_id:
        logger.error("Invalid YouTube URL")
        return None

    file_name = f"cache/{video_id}.mp3"

    if os.path.exists(file_name):
        logger.debug(f"File already exists: {file_name}")
        return (video_id, file_name)  # Return cached file

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": "cache/%(id)s.%(ext)s",
        "noplaylist": True,
        "cookiefile": "cookies.txt",
        "proxy": YTDLP_PROXY_URL,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Download if not cached

    logger.debug(f"Downloaded: {file_name}")
    return (video_id, file_name)

