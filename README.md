<div align="center">
<img width="128" height="128" alt="27ef7465-6bf8-46c6-94a7-f2ddc6979259-4" src="https://github.com/user-attachments/assets/2f87aac6-f2cd-4615-b24c-912e7cc9485d" />


# SoundCloud Downloader

**Download tracks from SoundCloud, YouTube, and YouTube Music directly to your desktop.**

![Platform](https://img.shields.io/badge/platform-Windows-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)

</div>

---

## Features

**Download** — paste a track link from SoundCloud, YouTube, or YouTube Music, hit Download. That's it.

**Monitor** — add artists to a watchlist, click Check — the app finds their new tracks from the last N days and downloads them automatically. Already downloaded tracks are skipped via an archive file.

**Clipboard detection** — copy a link in your browser, switch to the app — the URL is already filled in.

**OAuth token** — if SoundCloud starts rate-limiting requests, set your personal token for stable operation.

Output format: **MP3** with embedded cover art and metadata (artist, title, date).

---

## Screenshots
<img width="370" height="338" alt="Screenshot_1" src="https://github.com/user-attachments/assets/cd36894d-ab2b-4d5d-82e6-c951b1881f81" /><img width="369" height="337" alt="Screenshot_2" src="https://github.com/user-attachments/assets/bf1be00b-a04e-47b4-9679-034ed9db64ee" /><img width="370" height="338" alt="Screenshot_3" src="https://github.com/user-attachments/assets/63fee8ea-7399-4c43-b4cc-ec0a3cbf6452" />



---

## Installation

1. Download the archive from [Releases](../../releases/latest)
2. Extract to any folder
3. Run `SoundCloud Downloader.exe`

> **ffmpeg is already bundled** — no additional setup required.

---

## Folder structure after first run

```
SoundCloud Downloader/
├── SoundCloud Downloader.exe
├── ffmpeg.exe                  ← bundled
├── Downloads/                  ← tracks saved here
│   └── ArtistName/
│       └── 20250501 - Track Title.mp3
├── artists.txt                 ← artist watchlist for Monitor
├── downloaded.txt              ← archive log (do not delete)
└── oauth.txt                   ← token (created when saved)
```

---

## Monitor — how to use

1. Open the **Monitor** tab
2. Paste an artist page URL (`https://soundcloud.com/artist-name`)
3. Click **Add** — the artist is added to the list
4. Click **Check All** — the app checks all artists and downloads new tracks

Tracks are saved to `Downloads/<artist name>/` with the release date in the filename.

---

## OAuth Token (optional)

Needed if SoundCloud starts returning 403 errors. The token is tied to your account.

**How to get it:**

1. Open [soundcloud.com](https://soundcloud.com) and log in
2. Press `F12` → **Network** tab
3. Type `api-v2` in the filter box
4. Press Play on any track
5. Click any request → **Headers** tab → find:
   ```
   Authorization: OAuth 2-294412-987654321-AbCdEfGhIjKlMn
   ```
6. Copy only the part after `OAuth ` (without the word itself)
7. Paste it in **Settings** → OAuth Token field → click **Save Token**

---

## Supported sources

| Source | Single track | Artist monitor |
|---|---|---|
| SoundCloud | ✅ | ✅ |
| YouTube | ✅ | ❌ |
| YouTube Music | ✅ | ❌ |

---

The built executable will appear in `dist\SoundCloud Downloader\`.

---

## Dependencies

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — track downloading
- [ffmpeg](https://ffmpeg.org) — MP3 conversion
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) — UI
- [Pillow](https://python-pillow.org) — icon generation
