import click
import os
import sys
import asyncio
import requests
from dotenv import load_dotenv

load_dotenv()

@click.group()
def cli():
    """CLI for managing the Discord bot."""
    pass

@cli.command()
def start():
    """Start the Discord bot."""
    token = os.getenv("BOT_TOKEN")
    if not token:
        click.echo("Error: BOT_TOKEN is not set!", err=True)
        sys.exit(1)

    click.echo("Starting Discord Bot...")
    from nearbot import start_bot
    asyncio.run(start_bot())

@cli.command()
@click.option('--all', is_flag=True, help="Initialize everything.")
@click.option('--ytdlp', type=click.Choice(['win', 'linux']), help="Initialize yt-dlp for Windows or Linux.")
def init(all, ytdlp):
    """Initialize bot dependencies."""

    if not os.path.exists("bin"):
        os.makedirs("bin")

    if all:
        click.echo("Initializing everything...")
        install_ytdlp("win")
        install_ytdlp("linux")
        click.echo("Initialization complete.")
        return

    if ytdlp:
        install_ytdlp(ytdlp)
        click.echo(f"yt-dlp initialized for {ytdlp}.")

def download_file(url, filepath):
    """Download a file using requests and save it."""
    try:
        click.echo(f"Downloading: {url} -> {filepath}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        click.echo(f"Downloaded successfully: {filepath}")
    except requests.exceptions.RequestException as e:
        click.echo(f"Download failed: {e}", err=True)
        sys.exit(1)

def install_ytdlp(os_type):
    """Helper function to install yt-dlp."""
    urls = {
        "win": "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe",
        "linux": "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp"
    }

    filename = "ytdlp.exe" if os_type == "win" else "ytdlp"
    filepath = os.path.join("bin", filename)

    download_file(urls[os_type], filepath)

    if os_type == "linux":
        os.chmod(filepath, 0o755)

if __name__ == "__main__":
    cli()
