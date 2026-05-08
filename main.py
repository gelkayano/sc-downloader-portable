import sys
import os


def main():
    from config import FFMPEG_PATH
    if not os.path.exists(FFMPEG_PATH):
        print(f"WARNING: ffmpeg.exe not found at {FFMPEG_PATH}")
        print("Download it and place in the same folder as this program.")

    from splash import show_splash

    def launch_app():
        from gui import App
        app = App()
        app.mainloop()

    show_splash(on_done=launch_app)


if __name__ == "__main__":
    main()
