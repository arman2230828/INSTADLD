import logging
import asyncio
from datetime import datetime, timezone
import yt_dlp
import instaloader
from app.models.schemas import ProcessResponse, MediaItem

logger = logging.getLogger(__name__)

class MediaService:
    """
    Service for media processing using yt-dlp to support multiple platforms.
    """

    @staticmethod
    def _extract_info_sync(url: str) -> dict:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
            'noplaylist': True,
            'extract_flat': 'in_playlist',
            'socket_timeout': 10,
            # Use best to get either video or image depending on what's available
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)

    @staticmethod
    async def process_url(url: str, mode: str = "reel") -> ProcessResponse:
        logger.info(f"Processing URL {url} in mode: {mode}")
        
        try:
            items = []
            
            # Use yt-dlp to extract data
            info_dict = await asyncio.to_thread(MediaService._extract_info_sync, url)
            
            media_title = info_dict.get('title', 'Unknown Title')
            thumbnail_url = info_dict.get('thumbnail', '')
            action_url = info_dict.get('url')
            
            # If the post is a carousel/playlist, extract all entries
            if 'entries' in info_dict and info_dict['entries']:
                for entry in info_dict['entries']:
                    entry_thumb = entry.get('thumbnail', '')
                    entry_url = entry.get('url')
                    if not entry_url and 'formats' in entry and entry['formats']:
                        entry_url = entry['formats'][-1].get('url', '#')
                    
                    # Determine if it's a video based on vcodec or ext
                    is_vid = entry.get('vcodec') != 'none' or (entry.get('ext') in ['mp4', 'webm'])
                    items.append(MediaItem(thumbnail_url=entry_thumb, action_url=entry_url, is_video=is_vid))
                    
                # Set the main thumbnail and url to the first item for fallback compatibility
                if items:
                    thumbnail_url = thumbnail_url or items[0].thumbnail_url
                    action_url = action_url or items[0].action_url
            else:
                if not action_url and 'formats' in info_dict and info_dict['formats']:
                    action_url = info_dict['formats'][-1].get('url', '#')
                elif not action_url:
                    action_url = '#'
                is_vid = info_dict.get('vcodec') != 'none' or (info_dict.get('ext') in ['mp4', 'webm'])
                items.append(MediaItem(thumbnail_url=thumbnail_url, action_url=action_url, is_video=is_vid))
                
            timestamp_str = datetime.now(timezone.utc).isoformat()
                
            return ProcessResponse(
                success=True,
                message="Process completed successfully.",
                media_title=media_title,
                thumbnail_url=thumbnail_url,
                action_url=action_url,
                items=items,
                timestamp=timestamp_str
            )
        except Exception as e:
            err_msg = str(e).lower()
            logger.error(f"Failed to process {mode} for {url}: {e}")
            
            user_msg = "Failed to process. Make sure the profile is public or the URL is correct."
            if "empty media response" in err_msg or "not exists" in err_msg or "403" in err_msg or "blocked" in err_msg:
                user_msg = "Instagram blocked the request or the account is private. (Try again later, or your server IP is rate-limited)."
                
            return ProcessResponse(
                success=False,
                message=user_msg
            )
