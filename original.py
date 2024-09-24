import yt_dlp, json


CHANNEL_URL = 'https://www.youtube.com/@tezkabar1/videos'

def get_recent_videos(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',
        'playlist_items': '1-50',
        'skip_download': True,
        'force_generic_extractor': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(channel_url, download=False)

    for entry in info_dict.get('entries', []):
        video_url = entry.get('url')
        video_title = entry.get('title')
        video_date = entry.get('upload_date')
        video_description = entry.get('description')
        video_image = entry.get('thumbnails')
        video_view_count = entry.get('view_count')
        data = [{   
            "Название": f"{video_title}",
            "URL": f"{video_url}",
            "Описание" : f"{video_description}",
            "Дата публикации": f"{video_date}",
            "Фото превью" : f"{video_image[2]['url']}",
            "Просмотры": f"{video_view_count}",
        }]
        print(json.dumps(data, indent=4, ensure_ascii=False))
    return data
print(get_recent_videos(CHANNEL_URL))
