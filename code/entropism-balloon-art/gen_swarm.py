"""Generate the balloon-swarm layer for balloon-castle.svg.

The swarm is one continuous flow of hot-air balloons rising from the stripped
ground up to the Great Machine. Crucially, a balloon's SIZE is a function of its
height on the canvas (perspective), not of which stream it belongs to: big and
recognisable near the ground, shrinking to stylised dots of light as they near
the structure. Balloons are gathered into broad 'rivers' feeding the machine's
docks, plus an ambient scatter filling the rest of the sky, so the infrastructure
reads as vast and continuous.

Deterministic (seeded). Injects between the SWARM_START/END markers.
"""
import math
import random
import re

SVG = "/home/act65/Documents/repos/act65.github.io/assets/entropism/balloon-castle.svg"
random.seed(7)

GROUND_Y = 1560.0   # perspective reference: balloons here are largest
DOCK_Y = 500.0      # ...and smallest as they approach the machine underside

# conveyor 'rivers': P0 near ground -> P3 at the machine docks
STREAMS = [
    [(180, 1600), (120, 1150), (360, 760), (445, 522)],
    [(430, 1620), (520, 1200), (560, 780), (565, 520)],
    [(780, 1560), (930, 1180), (720, 800), (650, 524)],   # passes near the foreground balloon
    [(1040, 1600), (1185, 1140), (885, 780), (712, 524)],
    [(600, 1610), (645, 1210), (600, 830), (605, 522)],   # central spine
]


def bez(p, t):
    u = 1 - t
    x = u**3*p[0][0] + 3*u*u*t*p[1][0] + 3*u*t*t*p[2][0] + t**3*p[3][0]
    y = u**3*p[0][1] + 3*u*u*t*p[1][1] + 3*u*t*t*p[2][1] + t**3*p[3][1]
    return x, y


def dbez(p, t):
    u = 1 - t
    x = 3*u*u*(p[1][0]-p[0][0]) + 6*u*t*(p[2][0]-p[1][0]) + 3*t*t*(p[3][0]-p[2][0])
    y = 3*u*u*(p[1][1]-p[0][1]) + 6*u*t*(p[2][1]-p[1][1]) + 3*t*t*(p[3][1]-p[2][1])
    return x, y


def perspective(y):
    """0 at the machine (small) -> 1 at the ground (large)."""
    return max(0.0, min(1.0, (y - DOCK_Y) / (GROUND_Y - DOCK_Y)))


def size_at(y):
    return 1.3 + perspective(y) ** 1.7 * 34.0


def warm_at(y):
    if y > 1160:
        return random.choice(["#ff8a3d", "#ff7a30", "#ffa050", "#ff934a", "#ff8236"])
    if y > 830:
        return random.choice(["#ffb35e", "#ffa952", "#ff9d5a", "#ffc070", "#ffab58"])
    return random.choice(["#ffd9a8", "#ffcf8a", "#ffe3b4", "#ffd89a", "#ffe0aa"])


def opacity_at(y, lo=0.8, hi=1.05):
    f = perspective(y)
    return round(min(0.92, (0.42 + 0.5 * f) * random.uniform(lo, hi)), 2)


def emit(x, y, s, parts, halo=True, op=None):
    """Render one balloon: silhouette if big enough, else a dot of light."""
    c = warm_at(y)
    o = op if op is not None else opacity_at(y)
    if halo and s > 5 and random.random() < 0.13:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{s*1.3:.1f}" fill="{c}" opacity="{o*0.12:.2f}"/>')
    if s > 6:
        parts.append(
            f'<use xlink:href="#minib" transform="translate({x:.1f},{y:.1f}) scale({s/12:.2f})" '
            f'fill="{c}" opacity="{o:.2f}"/>'
        )
    else:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{s/2:.1f}" fill="{c}" opacity="{o:.2f}"/>')


parts = []

# 1) the rivers — sampled so points spread evenly up the flow (less clumping),
#    with wide lateral scatter so individual balloons stay legible
for P in STREAMS:
    for i in range(300):
        t = (i + random.random()) / 300.0
        x, y = bez(P, t)
        dx, dy = dbez(P, t)
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        s = size_at(y) * random.uniform(0.7, 1.15)
        spread = 16 + s * 1.1 + 34 * (1 - t)
        off = random.gauss(0, spread)
        emit(x + nx * off, y + ny * off, s, parts)

# 2) ambient scatter filling the whole sky (balloons not in a defined river)
for _ in range(430):
    y = random.uniform(545, 1560)
    x = random.uniform(50, 1150)
    if perspective(y) < 0.4 and random.random() < 0.5:   # thin the far/high field
        continue
    s = size_at(y) * random.uniform(0.55, 1.0)
    emit(x, y, s * 0.8, parts)

# 3) legible large balloons low in the flow, tying the ground to the midground
for _ in range(55):
    x = random.uniform(70, 1130)
    y = random.uniform(1050, 1520)
    if x > 690 and y > 1040:      # keep clear of the full-size foreground balloon
        continue
    s = size_at(y) * random.uniform(0.8, 1.12)
    emit(x, y, s, parts, halo=False, op=round(random.uniform(0.68, 0.9), 2))

# 4) arrival queue clustered under the machine docks
for _ in range(170):
    x = min(max(random.gauss(590, 150), 360), 850)
    y = random.gauss(545, 24)
    s = random.uniform(1.2, 3.0)
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{s/2:.1f}" fill="{warm_at(y)}" opacity="{opacity_at(y):.2f}"/>')

# 5) a few dark real-balloon silhouettes low in the flow, for variety
for _ in range(8):
    P = random.choice(STREAMS[:4])
    t = random.uniform(0.02, 0.11)
    x, y = bez(P, t)
    x += random.gauss(0, 24)
    sc = random.uniform(0.9, 1.5)
    parts.append(f'<use xlink:href="#medb" transform="translate({x:.1f},{y:.1f}) scale({sc:.2f})"/>')

with open(SVG) as f:
    src = f.read()

block = "<!--SWARM_START-->\n    " + "\n    ".join(parts) + "\n    <!--SWARM_END-->"
out, n = re.subn(r"<!--SWARM_START-->.*?<!--SWARM_END-->", block, src, flags=re.S)
assert n == 1, "markers not found"

with open(SVG, "w") as f:
    f.write(out)

print(f"injected {len(parts)} swarm elements")
