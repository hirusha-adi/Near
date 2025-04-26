import typing as t
import yt_dlp
import os
from loguru import logger
from pathlib import Path
from utils import types

# env configs
YTDLP_PROXY_URL = os.getenv("YTDLP_PROXY_URL")
COOKIE_FILE = "cookies.txt"
CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)


def download_video(url: str) -> t.Optional[types.VideoDownloadResult]:
    logger.info(f"Processing YouTube URL: {url}")

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": str(CACHE_DIR / "%(id)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }

    if os.path.exists(COOKIE_FILE):
        ydl_opts["cookiefile"] = COOKIE_FILE

    if YTDLP_PROXY_URL:
        ydl_opts["proxy"] = YTDLP_PROXY_URL

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_id = info["id"]
            title = info.get("title", "Unknown Title")
            uploader = info.get("uploader", "Unknown Uploader")
            thumbnail = info.get("thumbnail", "")
            filename = (CACHE_DIR / f"{video_id}.mp3").resolve()

            if filename.exists():
                logger.info(f"Using cached file for: {title}")
            else:
                logger.info(f"Downloading and converting to MP3: {title}")
                ydl.download([url])

            return {
                "video_id": video_id,
                "title": title,
                "uploader": uploader,
                "file_path": str(filename),  # absolute path
                "thumbnail": thumbnail
            }

    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Download failed: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")

    return None
