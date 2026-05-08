import tkinter as tk
from PIL import Image, ImageTk
from config import get_resource_path


def show_splash(on_done):
    """
    Shows a borderless splash window with the app icon.
    Fades in briefly, holds, then fades out — then calls on_done().
    """
    icon_path = get_resource_path("icon.ico")

    root = tk.Tk()
    root.overrideredirect(True)       # no title bar / borders
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.0)
    root.configure(bg="#000000")

    # ── Load icon image ──────────────────────────────────────────────
    try:
        img_pil = Image.open(icon_path)
        # Use the largest available size (first frame of .ico)
        img_pil = img_pil.convert("RGBA")
        SPLASH_SIZE = 220
        img_pil = img_pil.resize((SPLASH_SIZE, SPLASH_SIZE), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img_pil)
    except Exception:
        # Fallback: tiny blank window so the rest still works
        root.destroy()
        on_done()
        return

    # ── Layout ───────────────────────────────────────────────────────
    PAD = 40
    WIN_SIZE = SPLASH_SIZE + PAD * 2

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w - WIN_SIZE) // 2
    y = (screen_h - WIN_SIZE) // 2
    root.geometry(f"{WIN_SIZE}x{WIN_SIZE}+{x}+{y}")

    canvas = tk.Canvas(
        root,
        width=WIN_SIZE, height=WIN_SIZE,
        bg="#000000", highlightthickness=0,
    )
    canvas.pack()
    canvas.create_image(WIN_SIZE // 2, WIN_SIZE // 2, image=photo, anchor="center")

    # ── Animation ────────────────────────────────────────────────────
    FADE_IN_MS   = 300   # ms to reach full opacity
    HOLD_MS      = 1000  # ms at full opacity
    FADE_OUT_MS  = 300   # ms to fade to zero
    STEP_MS      = 16    # ~60 fps

    steps_in  = max(1, FADE_IN_MS  // STEP_MS)
    steps_out = max(1, FADE_OUT_MS // STEP_MS)

    state = {"phase": "in", "step": 0}

    def tick():
        phase = state["phase"]

        if phase == "in":
            state["step"] += 1
            alpha = state["step"] / steps_in
            root.attributes("-alpha", min(alpha, 1.0))
            if state["step"] >= steps_in:
                state["phase"] = "hold"
                root.after(HOLD_MS, tick)
            else:
                root.after(STEP_MS, tick)

        elif phase == "hold":
            state["phase"] = "out"
            state["step"] = 0
            root.after(STEP_MS, tick)

        elif phase == "out":
            state["step"] += 1
            alpha = 1.0 - state["step"] / steps_out
            root.attributes("-alpha", max(alpha, 0.0))
            if state["step"] >= steps_out:
                root.destroy()
                on_done()
            else:
                root.after(STEP_MS, tick)

    root.after(STEP_MS, tick)
    root.mainloop()
