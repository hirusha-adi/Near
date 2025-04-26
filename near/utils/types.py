import typing as t

class VideoDownloadResult(t.TypedDict):
    video_id: str
    title: str
    uploader: str
    file_path: str
    thumbnail: str
