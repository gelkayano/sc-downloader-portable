"""
Генератор иконки — кибернетика / киберпанк / философия / абстракция
Запусти один раз: python create_icon.py
"""

from PIL import Image, ImageDraw
import math
import os


def create_icon():
    sizes = [256, 128, 64, 48, 32, 16]
    images = []

    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        cx, cy = size // 2, size // 2
        s = size  # короткое имя

        # ============================================
        # ФОН — глубокий чёрный с радиальным затуханием
        # ============================================
        max_r = s * 0.48
        for y in range(s):
            for x in range(s):
                dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
                if dist <= max_r:
                    # Центр чуть светлее, края темнее
                    fade = 1.0 - (dist / max_r) * 0.6
                    base = int(8 * fade)
                    img.putpixel((x, y), (base, base, base + 2, 255))

        # ============================================
        # ГЕКСАГОНАЛЬНАЯ РАМКА — кибернетическая форма
        # ============================================
        hex_r = int(s * 0.43)
        hex_width = max(1, int(s * 0.015))
        hex_points = []
        for i in range(6):
            angle = math.pi / 6 + (math.pi / 3) * i  # Плоская сторона сверху
            hx = cx + hex_r * math.cos(angle)
            hy = cy + hex_r * math.sin(angle)
            hex_points.append((hx, hy))

        # Рисуем стороны гексагона с разрывами
        for i in range(6):
            x1, y1 = hex_points[i]
            x2, y2 = hex_points[(i + 1) % 6]

            # Разрыв на каждой второй стороне
            if i % 2 == 0:
                # Полная линия
                draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255, 180), width=hex_width)
            else:
                # Линия с разрывом посередине (две половинки)
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                gap = 0.15
                draw.line(
                    [(x1, y1), (x1 + (mx - x1) * (1 - gap), y1 + (my - y1) * (1 - gap))],
                    fill=(255, 255, 255, 120), width=hex_width,
                )
                draw.line(
                    [(x2 + (mx - x2) * (1 - gap), y2 + (my - y2) * (1 - gap)), (x2, y2)],
                    fill=(255, 255, 255, 120), width=hex_width,
                )

        # Точки на вершинах гексагона
        if s >= 32:
            for px, py in hex_points:
                dot_r = max(1, int(s * 0.015))
                draw.ellipse(
                    [px - dot_r, py - dot_r, px + dot_r, py + dot_r],
                    fill=(255, 255, 255, 200),
                )

        # ============================================
        # ВНУТРЕННИЙ КРУГ — орбита сознания
        # ============================================
        orbit_r = int(s * 0.28)
        orbit_w = max(1, int(s * 0.006))

        if s >= 48:
            # Разорванный круг — три дуги
            for start, end in [(0, 70), (120, 190), (240, 310)]:
                draw.arc(
                    [cx - orbit_r, cy - orbit_r, cx + orbit_r, cy + orbit_r],
                    start=start, end=end,
                    fill=(255, 255, 255, 70),
                    width=orbit_w,
                )
        else:
            draw.ellipse(
                [cx - orbit_r, cy - orbit_r, cx + orbit_r, cy + orbit_r],
                outline=(255, 255, 255, 50),
                width=orbit_w,
            )

        # ============================================
        # ГЛАЗ ПРОВИДЕНИЯ — центральный символ
        # ============================================
        if s >= 24:
            eye_w = int(s * 0.22)
            eye_h = int(s * 0.11)

            # Верхняя дуга глаза
            draw.arc(
                [cx - eye_w, cy - eye_h * 2, cx + eye_w, cy + eye_h],
                start=200, end=340,
                fill=(255, 255, 255, 200),
                width=max(1, int(s * 0.012)),
            )

            # Нижняя дуга глаза
            draw.arc(
                [cx - eye_w, cy - eye_h, cx + eye_w, cy + eye_h * 2],
                start=20, end=160,
                fill=(255, 255, 255, 200),
                width=max(1, int(s * 0.012)),
            )

            # Зрачок — внешний круг
            pupil_r = max(2, int(s * 0.055))
            draw.ellipse(
                [cx - pupil_r, cy - pupil_r, cx + pupil_r, cy + pupil_r],
                outline=(255, 255, 255, 220),
                width=max(1, int(s * 0.01)),
            )

            # Зрачок — внутренняя точка
            inner_r = max(1, int(s * 0.025))
            draw.ellipse(
                [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
                fill=(255, 255, 255, 255),
            )

        # ============================================
        # ВЕРТИКАЛЬНАЯ ЛИНИЯ — ось симметрии / позвоночник
        # ============================================
        if s >= 32:
            line_w = max(1, int(s * 0.008))

            # Верхняя линия (от глаза вверх к гексагону)
            top_start = cy - int(s * 0.15)
            top_end = cy - int(s * 0.35)
            draw.line(
                [(cx, top_start), (cx, top_end)],
                fill=(255, 255, 255, 100),
                width=line_w,
            )

            # Нижняя линия (от глаза вниз к гексагону)
            bot_start = cy + int(s * 0.15)
            bot_end = cy + int(s * 0.35)
            draw.line(
                [(cx, bot_start), (cx, bot_end)],
                fill=(255, 255, 255, 100),
                width=line_w,
            )

        # ============================================
        # ДИАГОНАЛЬНЫЕ ЛУЧИ — нейронные связи
        # ============================================
        if s >= 48:
            ray_len = int(s * 0.12)
            ray_w = max(1, int(s * 0.006))
            ray_start_r = int(s * 0.18)

            angles_rays = [
                math.pi / 4,       # верхний правый
                3 * math.pi / 4,   # верхний левый
                5 * math.pi / 4,   # нижний левый
                7 * math.pi / 4,   # нижний правый
            ]

            for angle in angles_rays:
                rx1 = cx + int(ray_start_r * math.cos(angle))
                ry1 = cy + int(ray_start_r * math.sin(angle))
                rx2 = cx + int((ray_start_r + ray_len) * math.cos(angle))
                ry2 = cy + int((ray_start_r + ray_len) * math.sin(angle))
                draw.line(
                    [(rx1, ry1), (rx2, ry2)],
                    fill=(255, 255, 255, 60),
                    width=ray_w,
                )

                # Маленькая точка на конце
                end_dot = max(1, int(s * 0.01))
                draw.ellipse(
                    [rx2 - end_dot, ry2 - end_dot, rx2 + end_dot, ry2 + end_dot],
                    fill=(255, 255, 255, 100),
                )

        # ============================================
        # ГЛИТЧ-ЛИНИИ — горизонтальные помехи (киберпанк)
        # ============================================
        if s >= 64:
            import random
            random.seed(42)  # Фиксированный seed для воспроизводимости

            glitch_w = max(1, int(s * 0.004))
            num_glitches = 5

            for _ in range(num_glitches):
                gy = random.randint(int(cy - s * 0.35), int(cy + s * 0.35))
                gx_start = random.randint(int(cx - s * 0.3), int(cx - s * 0.05))
                gx_end = gx_start + random.randint(int(s * 0.05), int(s * 0.2))
                alpha = random.randint(20, 50)

                draw.line(
                    [(gx_start, gy), (gx_end, gy)],
                    fill=(255, 255, 255, alpha),
                    width=glitch_w,
                )

        # ============================================
        # ДАННЫЕ / МАТРИЧНЫЕ ТОЧКИ — по краям
        # ============================================
        if s >= 64:
            random.seed(77)
            dot_r_data = max(1, int(s * 0.006))
            num_data = 8

            for _ in range(num_data):
                angle = random.uniform(0, 2 * math.pi)
                dist = random.uniform(s * 0.33, s * 0.42)
                dx = int(cx + dist * math.cos(angle))
                dy = int(cy + dist * math.sin(angle))
                alpha = random.randint(30, 80)

                draw.ellipse(
                    [dx - dot_r_data, dy - dot_r_data, dx + dot_r_data, dy + dot_r_data],
                    fill=(255, 255, 255, alpha),
                )

        # ============================================
        # ТРЕУГОЛЬНИК МУДРОСТИ — вокруг глаза
        # ============================================
        if s >= 48:
            tri_r = int(s * 0.17)
            tri_w = max(1, int(s * 0.008))

            tri_points = []
            for i in range(3):
                angle = -math.pi / 2 + (2 * math.pi / 3) * i
                tx = cx + tri_r * math.cos(angle)
                ty = cy + tri_r * math.sin(angle)
                tri_points.append((tx, ty))

            for i in range(3):
                x1, y1 = tri_points[i]
                x2, y2 = tri_points[(i + 1) % 3]
                draw.line(
                    [(x1, y1), (x2, y2)],
                    fill=(255, 255, 255, 80),
                    width=tri_w,
                )

        images.append(img)

    # ============================================
    # СОХРАНЕНИЕ — только .ico
    # ============================================
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
    images[0].save(
        icon_path,
        format='ICO',
        sizes=[(s, s) for s in sizes],
        append_images=images[1:],
    )
    print(f"✅ Icon created: {icon_path}")


if __name__ == "__main__":
    create_icon()