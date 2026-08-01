#!/usr/bin/env python3
"""Generate static SVG hex-grid diagrams for the 'chords are shapes' post.

No runtime JS — the interactive version is the hexboard app itself. This just
draws crisp SVGs of the isomorphic grid with chord shapes / axes highlighted.

Output: assets/hexboard-theory/*.svg   (run from anywhere)
"""
import math, os

NOTE = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B']
def nm(pc): return NOTE[pc % 12]
def nm_oct(note): return NOTE[note % 12] + str(note // 12 - 1)

STEP_NAME = {1: 'semitone', 2: 'whole tone', 3: 'minor 3rd', 4: 'major 3rd', 5: 'fourth',
             6: 'tritone', 7: 'fifth', 8: 'minor 6th', 9: 'major 6th', 10: 'minor 7th', 11: 'major 7th'}

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                   'assets', 'hexboard-theory')

# palette (works on a light page)
GRID_FILL = '#efeae1'
GRID_STROKE = '#d6cfc0'
INK = '#3b342b'
MUTED = '#9c9384'
ACCENT = '#c8683c'   # terracotta  (primary shape)
ACCENT2 = '#5f7d4f'  # olive       (reflected / second shape)
BLUE = '#3f6f97'     # ↗ direction  (fifth)
GOLD = '#c99a2e'     # ↖ direction  (fourth / minor 3rd)
GREEN = '#4a8a5f'    # → direction  (whole tone / major 3rd)


class Board:
    """A finite isomorphic hex grid. right/upRight are the two basis intervals."""
    def __init__(self, right, upRight, cols, rows, base=48, s=34):
        self.right, self.upRight = right, upRight
        self.cols, self.rows, self.base, self.s = cols, rows, base, s
        self.w = math.sqrt(3) * s
        self.vert = 1.5 * s
        self.pad = s + 8
        self.cells = {}
        for row in range(rows):
            for col in range(cols):
                cx = self.pad + col * self.w + row * (self.w / 2)
                cy = self.pad + row * self.vert
                note = base + col * right + (rows - 1 - row) * (upRight - right)
                self.cells[(col, row)] = {'cx': cx, 'cy': cy, 'note': note}
        self.width = max(c['cx'] for c in self.cells.values()) + self.pad
        self.height = max(c['cy'] for c in self.cells.values()) + self.pad

    def step_legend(self):
        e = STEP_NAME.get(self.right % 12, f'{self.right} st')
        ne = STEP_NAME.get(self.upRight % 12, f'{self.upRight} st')
        nw = STEP_NAME.get((self.upRight - self.right) % 12, '')
        return e, ne, nw

    def hexpts(self, cx, cy, shrink=1.0):
        r = self.s * shrink
        return [(cx + r * math.cos(math.radians(60 * i - 90)),
                 cy + r * math.sin(math.radians(60 * i - 90))) for i in range(6)]

    def cell_for_note(self, target, ref):
        rc = self.cells[ref]
        best, bd = None, 1e18
        for k, c in self.cells.items():
            if c['note'] == target:
                d = (c['cx'] - rc['cx']) ** 2 + (c['cy'] - rc['cy']) ** 2
                if d < bd:
                    bd, best = d, k
        return best

    def offsets(self, intervals):
        """(dcol, drow) lattice offsets for each interval — compact, near a central
        reference root. Applying the SAME offsets at any root gives an identical shape."""
        ref = (self.cols // 2, self.rows // 2)
        rn = self.cells[ref]['note']
        offs = []
        for iv in intervals:
            k = self.cell_for_note(rn + iv, ref)
            offs.append((k[0] - ref[0], k[1] - ref[1]))
        return offs

    def place(self, root_cell, offsets):
        rc, rr = root_cell
        out = []
        for dc, dr in offsets:
            k = (rc + dc, rr + dr)
            if k in self.cells:
                out.append(k)
        return out

    def chord(self, root_cell, intervals):
        return self.place(root_cell, self.offsets(intervals))


def poly(pts, fill, stroke, sw=2):
    p = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def text(x, y, s, fill=INK, size=15, weight='600', anchor='middle'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" '
            f'font-family="Georgia, serif" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" dominant-baseline="central">{s}</text>')

def line(x1, y1, x2, y2, stroke, sw=3, dash=None, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    a = ' marker-end="url(#arrow)"' if arrow else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}"{d}{a}/>'


def hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 2:
        return pts
    def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def _legend(board, x, y):
    """A one-line 'steps:' key so each figure declares what its directions mean."""
    e, ne, nw = board.step_legend()
    s = f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="start" font-family="Georgia, serif" ' \
        f'font-size="14" dominant-baseline="central">'
    s += f'<tspan fill="{MUTED}">steps:  </tspan>'
    s += f'<tspan fill="{GREEN}" font-weight="700">→ {e}</tspan>'
    s += f'<tspan fill="{MUTED}">    </tspan><tspan fill="{BLUE}" font-weight="700">↗ {ne}</tspan>'
    s += f'<tspan fill="{MUTED}">    </tspan><tspan fill="{GOLD}" font-weight="700">↖ {nw}</tspan>'
    s += '</text>'
    return s


def svg(board, groups, extras='', label_all=False, legend=False):
    """groups: {cells, fill, labels:'note'|None, outline:color|None}."""
    top = 40 if legend else 0
    W, H = board.width, board.height + top
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" '
             f'font-family="Georgia, serif" role="img">',
             '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
             '<path d="M0,0 L9,4.5 L0,9 z" fill="#333"/></marker></defs>']
    if legend:
        parts.append(_legend(board, board.pad, 20))
        parts.append(f'<g transform="translate(0,{top})">')
    for k, c in board.cells.items():
        parts.append(poly(board.hexpts(c['cx'], c['cy'], 0.94), GRID_FILL, GRID_STROKE, 1.5))
        if label_all:
            parts.append(text(c['cx'], c['cy'], nm(c['note']), MUTED, 12, '500'))
    for g in groups:
        # connective outline first (under the hexes' labels)
        if g.get('outline'):
            centres = [(board.cells[k]['cx'], board.cells[k]['cy']) for k in g['cells']]
            h = hull(centres)
            if len(h) >= 2:
                d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in h)
                closed = ' Z' if len(h) >= 3 else ''
                parts.append(f'<polyline points="{d}" fill="none" stroke="{g["outline"]}" '
                             f'stroke-width="7" stroke-linejoin="round" stroke-linecap="round" opacity="0.28"/>')
        for k in g['cells']:
            c = board.cells[k]
            parts.append(poly(board.hexpts(c['cx'], c['cy'], 0.94), g['fill'], g.get('stroke', '#00000022'), 2))
            lc = g.get('labelcolor', '#fff')
            if g.get('labels') == 'note':
                parts.append(text(c['cx'], c['cy'], nm(c['note']), lc, 15, '700'))
            elif g.get('labels') == 'noteoct':
                parts.append(text(c['cx'], c['cy'], nm_oct(c['note']), lc, 13, '700'))
    parts.append(extras)
    if legend:
        parts.append('</g>')
    parts.append('</svg>')
    return '\n'.join(parts)


def write(name, s):
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, name), 'w').write(s)
    print('wrote', name)


# Wicki-Hayden: E=+2 (whole tone), NE=+7 (fifth), NW=+5 (fourth)
def wicki(cols=8, rows=5, base=47, s=34):
    return Board(2, 7, cols, rows, base, s)

# Tonnetz / Harmonic-table: E=+4 (major 3rd), NE=+7 (fifth), NW=+3 (minor 3rd)
def tonnetz(cols=7, rows=5, base=48, s=34):
    return Board(4, 7, cols, rows, base, s)


def d_chord_is_a_shape():
    """A major triad is the SAME shape wherever you put it (label-less / monochrome)."""
    b = wicki(cols=9, rows=5, base=45)
    offs = b.offsets([0, 4, 7])
    roots = [(1, 3), (5, 1)]
    fills = [ACCENT, ACCENT2]
    groups, extras = [], ''
    for rc, fill in zip(roots, fills):
        cells = b.place(rc, offs)
        groups.append({'cells': cells, 'fill': fill, 'outline': fill, 'labels': None})
        c = b.cells[rc]
        extras += text(c['cx'] + b.s * 0.9, c['cy'] + b.s * 1.55,
                       nm(b.cells[rc]['note']) + ' major', INK, 14, '700')
    write('chord-is-a-shape.svg', svg(b, groups, extras, legend=True))


def d_axes():
    """The two diagonals: up-right = fifths (bright), up-left = fourths (dark)."""
    b = wicki(cols=8, rows=5, base=47)
    root = b.cell_for_note(60, (3, 3))
    # fifth axis (up-right): +7 each step
    fifths = [root]
    for _ in range(4):
        nxt = b.cell_for_note(b.cells[fifths[-1]]['note'] + 7, fifths[-1])
        if nxt and nxt != fifths[-1]:
            fifths.append(nxt)
    fourths = [root]
    for _ in range(4):
        nxt = b.cell_for_note(b.cells[fourths[-1]]['note'] + 5, fourths[-1])
        if nxt and nxt != fourths[-1]:
            fourths.append(nxt)
    g5 = {'cells': fifths, 'fill': BLUE, 'labels': 'note'}
    g4 = {'cells': fourths, 'fill': GOLD, 'labels': 'note'}
    gr = {'cells': [root], 'fill': INK, 'labels': 'note'}
    # labels beyond the top of each arm, clear of the cells
    c0 = b.cells[fifths[-1]]     # top fifth (A)
    c1 = b.cells[fourths[-1]]    # top fourth (E♭)
    extras = (text(c0['cx'] + b.s * 1.15, c0['cy'], 'brighter ↗', BLUE, 13, '700', anchor='start')
              + text(c1['cx'] - b.s * 1.15, c1['cy'], '↖ darker', GOLD, 13, '700', anchor='end'))
    write('axes-fifths-fourths.svg', svg(b, [g5, g4, gr], extras, legend=True))


def d_scale_modes():
    """The major scale is 7 notes in a straight line of fifths; modes slide it."""
    b = wicki(cols=8, rows=7, base=53, s=30)
    # C major = F C G D A E B : start at F (bottom-left) and climb 6 fifths (up-right)
    start = (0, 6)
    line_cells = [start]
    for _ in range(6):
        nxt = b.cell_for_note(b.cells[line_cells[-1]]['note'] + 7, line_cells[-1])
        if nxt and nxt not in line_cells:
            line_cells.append(nxt)
    g = {'cells': line_cells, 'fill': ACCENT, 'labels': 'note', 'outline': ACCENT}
    write('scale-line.svg', svg(b, [g], legend=True))


def _tri(b, a, c, d, col):
    px = lambda k: (b.cells[k]['cx'], b.cells[k]['cy'])
    (ax, ay), (bx, by), (cx, cy) = px(a), px(c), px(d)
    return (line(ax, ay, bx, by, col, 4) + line(bx, by, cx, cy, col, 4) + line(cx, cy, ax, ay, col, 4))

def _neg_reflect(b, cells, ref):
    """Negative harmony on the 2D grid is a 180° POINT reflection about the centre between
    C and G (note 3.5 above the tonic — the E♭/E point), NOT a line reflection: the mirror
    pairs run in different directions, so no single axis bisects them all. Maps cells
    exactly to cells and realises n -> (tonic+dominant) - n. Returns cells + centre."""
    c = b.cell_for_note(60, ref); g = b.cell_for_note(67, ref)
    Px = (b.cells[c]['cx'] + b.cells[g]['cx']) / 2
    Py = (b.cells[c]['cy'] + b.cells[g]['cy']) / 2
    out = []
    for cell in cells:
        rx, ry = 2 * Px - b.cells[cell]['cx'], 2 * Py - b.cells[cell]['cy']
        best, bd = None, 1e18
        for k, cc in b.cells.items():
            dd = (cc['cx'] - rx) ** 2 + (cc['cy'] - ry) ** 2
            if dd < bd:
                bd, best = dd, k
        out.append(best)
    return out, (Px, Py)


def _centre(Px, Py, pairs, b):
    """The reflection centre + dashed connectors putting each note opposite its mirror."""
    s = ''
    for o, r in pairs:
        s += line(b.cells[o]['cx'], b.cells[o]['cy'], b.cells[r]['cx'], b.cells[r]['cy'], '#8a8a8a', 1.5, dash='2 4')
    s += (f'<circle cx="{Px:.1f}" cy="{Py:.1f}" r="10.5" fill="#fff" stroke="#333" stroke-width="1.5"/>'
          f'<line x1="{Px - 6.5:.1f}" y1="{Py:.1f}" x2="{Px + 6.5:.1f}" y2="{Py:.1f}" stroke="#333" stroke-width="2"/>'
          f'<line x1="{Px:.1f}" y1="{Py - 6.5:.1f}" x2="{Px:.1f}" y2="{Py + 6.5:.1f}" stroke="#333" stroke-width="2"/>')
    return s

def d_negative_harmony():
    """Negative harmony as a 180° flip about the centre between E♭ and E. C major and C
    minor are point-reflections of each other, sharing the C–G edge; the 3rd flips."""
    b = wicki(cols=9, rows=6, base=47)
    ref = b.cell_for_note(60, (3, 3))
    C, E, G = b.cell_for_note(60, ref), b.cell_for_note(64, ref), b.cell_for_note(67, ref)
    refl, (Px, Py) = _neg_reflect(b, [C, E, G], ref)   # -> G, E♭, C
    Eb = refl[1]
    extras = _tri(b, C, E, G, ACCENT + 'cc') + _tri(b, C, Eb, G, ACCENT2 + 'cc')
    extras += _centre(Px, Py, [(E, Eb)], b)            # E and E♭ sit opposite through the centre (⊕)
    groups = [
        {'cells': [C, G], 'fill': '#6b7280', 'labels': 'note'},   # shared root & fifth
        {'cells': [E], 'fill': ACCENT, 'labels': 'note'},          # major 3rd
        {'cells': [Eb], 'fill': ACCENT2, 'labels': 'note'},        # minor 3rd
    ]
    write('negative-harmony.svg', svg(b, groups, extras, legend=True))


def d_negative_harmony_inv():
    """The SAME flip about the SAME centre works on any voicing. C major, first inversion
    (E4–G4–C5) point-reflected onto a C-minor voicing (G3–C4–E♭4)."""
    b = wicki(cols=9, rows=6, base=47)
    ref = b.cell_for_note(60, (3, 3))                  # anchor on C4 -> identical centre
    orig = [b.cell_for_note(64, ref), b.cell_for_note(67, ref), b.cell_for_note(72, ref)]  # E4 G4 C5
    refl, (Px, Py) = _neg_reflect(b, orig, ref)        # E♭4 C4 G3
    extras = _tri(b, orig[0], orig[1], orig[2], ACCENT + 'cc') + _tri(b, refl[0], refl[1], refl[2], ACCENT2 + 'cc')
    extras += _centre(Px, Py, list(zip(orig, refl)), b)
    groups = [
        {'cells': orig, 'fill': ACCENT, 'labels': 'noteoct'},
        {'cells': refl, 'fill': ACCENT2, 'labels': 'noteoct'},
    ]
    write('negative-harmony-inv.svg', svg(b, groups, extras, legend=True))


def d_circle_of_fifths():
    """The circle of fifths, with the C-major window highlighted as one 7-note arc.
    Clockwise = sharpward (the grid's ↗ diagonal), counter-clockwise = flatward (↖).
    The fifths diagonal on the hex grid is this circle unrolled into a line."""
    W = H = 560
    CX, CY, R = W / 2, H / 2 + 6, 158
    NR = 22                                   # node radius
    pos = {}                                  # i (circle slot) -> (x, y, angle°)
    for i in range(12):
        a = math.radians(-90 + 30 * i)        # C at 12 o'clock, clockwise by fifths
        pos[i] = (CX + R * math.cos(a), CY + R * math.sin(a), -90 + 30 * i)
    pc_at = lambda i: (7 * i) % 12            # slot -> pitch class
    window = [11, 0, 1, 2, 3, 4, 5]           # F C G D A E B = C major

    def arc(radius, a1, a2, sweep):
        x1, y1 = CX + radius * math.cos(math.radians(a1)), CY + radius * math.sin(math.radians(a1))
        x2, y2 = CX + radius * math.cos(math.radians(a2)), CY + radius * math.sin(math.radians(a2))
        return f'M {x1:.1f} {y1:.1f} A {radius:.1f} {radius:.1f} 0 0 {sweep} {x2:.1f} {y2:.1f}'

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
             f'font-family="Georgia, serif" role="img">',
             f'<defs>'
             f'<marker id="ab" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
             f'<path d="M0,0 L9,4.5 L0,9 z" fill="{BLUE}"/></marker>'
             f'<marker id="ag" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
             f'<path d="M0,0 L9,4.5 L0,9 z" fill="{GOLD}"/></marker>'
             f'</defs>']
    # faint full ring, then the C-major window as a soft band (F round to B, clockwise)
    parts.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{GRID_STROKE}" stroke-width="2"/>')
    parts.append(f'<path d="{arc(R, 240, 60, 1)}" fill="none" stroke="#8a9a6a" stroke-width="{NR * 2.4:.0f}" '
                 f'stroke-linecap="round" opacity="0.30"/>')
    # direction arrows: clockwise = sharpward (blue, matches ↗), ccw = flatward (gold, ↖)
    parts.append(f'<path d="{arc(R + 52, -70, -20, 1)}" fill="none" stroke="{BLUE}" stroke-width="3" marker-end="url(#ab)"/>')
    parts.append(f'<path d="{arc(R + 52, 250, 200, 0)}" fill="none" stroke="{GOLD}" stroke-width="3" marker-end="url(#ag)"/>')
    parts.append(text(CX + (R + 98) * math.cos(math.radians(-45)),
                      CY + (R + 98) * math.sin(math.radians(-45)), 'sharpward · brighter', BLUE, 14, '700'))
    parts.append(text(CX + (R + 98) * math.cos(math.radians(225)),
                      CY + (R + 98) * math.sin(math.radians(225)), 'flatward · darker', GOLD, 14, '700'))
    # nodes
    for i in range(12):
        x, y, _ = pos[i]
        pc = pc_at(i)
        if pc == 0:
            fill, tcol = ACCENT, '#fff'
        elif i in window:
            fill, tcol = '#6b7280', '#fff'
        else:
            fill, tcol = GRID_FILL, MUTED
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NR}" fill="{fill}" stroke="{GRID_STROKE}" stroke-width="1.5"/>')
        parts.append(text(x, y, nm(pc), tcol, 15, '700'))
    # centre annotation: the window IS the major scale
    parts.append(text(CX, CY - 12, 'C major', ACCENT, 19, '800'))
    parts.append(text(CX, CY + 14, 'seven consecutive fifths', MUTED, 13, '600'))
    parts.append('</svg>')
    write('circle-of-fifths.svg', '\n'.join(parts))


def _check_negative(b, orig, refl):
    """Every reflected cell must hold exactly (tonic+dominant)-note = 127 - note (about C4–G4)."""
    for o, r in zip(orig, refl):
        want = 127 - b.cells[o]['note']
        got = b.cells[r]['note']
        assert got == want, f'reflection landed on {got}, wanted {want}'


def d_negative_harmony_7ths():
    """The half-turn on seventh chords. (1) maj7 is a palindromic stack (M3–m3–M3), so it
    turns over onto another maj7: Cmaj7 -> A♭maj7. (2) dom7 (M3–m3–m3) turns over onto a
    half-diminished (m3–m3–M3): G7 -> Dm7♭5 — the ii and V of a ii–V are each other's
    negatives."""
    # -- Cmaj7 -> A♭maj7 (shares C and G with its negative, like the triad did) --
    b = wicki(cols=9, rows=6, base=47)
    ref = b.cell_for_note(60, (3, 3))
    orig = [b.cell_for_note(n, ref) for n in [60, 64, 67, 71]]      # C4 E4 G4 B4
    refl, (Px, Py) = _neg_reflect(b, orig, ref)                     # G4 E♭4 C4 A♭3
    _check_negative(b, orig, refl)
    C, E, G, B = orig
    Eb, Ab = refl[1], refl[3]
    extras = _centre(Px, Py, [(E, Eb), (B, Ab)], b)
    extras += text(b.cells[B]['cx'] + b.s * 1.2, b.cells[B]['cy'] - b.s * 0.9, 'C maj7', ACCENT, 14, '800')
    extras += text(b.cells[Ab]['cx'] - b.s * 1.2, b.cells[Ab]['cy'] + b.s * 0.95, 'A♭ maj7', ACCENT2, 14, '800')
    groups = [
        # soft hull bands first (drawn under the labelled cells)
        {'cells': orig, 'fill': 'none', 'stroke': 'none', 'outline': ACCENT},
        {'cells': refl, 'fill': 'none', 'stroke': 'none', 'outline': ACCENT2},
        {'cells': [C, G], 'fill': '#6b7280', 'labels': 'note'},     # shared by both chords
        {'cells': [E, B], 'fill': ACCENT, 'labels': 'note'},        # C maj7 only
        {'cells': [Eb, Ab], 'fill': ACCENT2, 'labels': 'note'},     # A♭ maj7 only
    ]
    write('negative-harmony-maj7.svg', svg(b, groups, extras, legend=True))

    # -- G7 -> Dm7♭5 (no shared notes; the ii–V pair) --
    b = wicki(cols=9, rows=6, base=47)
    ref = b.cell_for_note(60, (3, 3))
    orig = [b.cell_for_note(n, ref) for n in [67, 71, 74, 65]]      # G4 B4 D5 F4
    refl, (Px, Py) = _neg_reflect(b, orig, ref)                     # C4 A♭3 F3 D4
    _check_negative(b, orig, refl)
    extras = _centre(Px, Py, list(zip(orig, refl)), b)
    top = max(orig, key=lambda k: -b.cells[k]['cy'])
    bot = max(refl, key=lambda k: b.cells[k]['cy'])
    extras += text(b.cells[top]['cx'] + b.s * 1.3, b.cells[top]['cy'] - b.s * 0.8, 'G7', ACCENT, 14, '800')
    extras += text(b.cells[bot]['cx'] - b.s * 1.3, b.cells[bot]['cy'] + b.s * 0.9, 'Dm7♭5', ACCENT2, 14, '800')
    groups = [
        {'cells': orig, 'fill': ACCENT, 'labels': 'note', 'outline': ACCENT},
        {'cells': refl, 'fill': ACCENT2, 'labels': 'note', 'outline': ACCENT2},
    ]
    write('negative-harmony-dom7.svg', svg(b, groups, extras, legend=True))


def d_symmetric():
    """Symmetric chords on the Tonnetz: augmented (stacked M3), diminished-7 (stacked m3)."""
    b = tonnetz(cols=6, rows=6, base=48)
    aug = b.place((0, 1), b.offsets([0, 4, 8]))     # C E G#  — horizontal (stacked M3)
    dim = b.place((3, 5), b.offsets([0, 3, 6, 9]))  # C E♭ G♭ A — vertical (stacked m3)
    g1 = {'cells': aug, 'fill': ACCENT, 'labels': 'note', 'outline': ACCENT}
    g2 = {'cells': dim, 'fill': ACCENT2, 'labels': 'note', 'outline': ACCENT2}
    write('symmetric-aug.svg', svg(b, [g1], legend=True))
    write('symmetric-dim.svg', svg(b, [g2], legend=True))


def d_tonnetz_plr():
    """On the Tonnetz a triad is a triangle; P/L/R flip it across its three edges.
    Built by adjacency so the neighbours share an edge with the C-major triangle."""
    b = tonnetz(cols=8, rows=6, base=46, s=36)
    root = (2, 3)                                      # C, central (room for all edges)
    add = lambda cell, o: (cell[0] + o[0], cell[1] + o[1])
    o4 = b.offsets([4])[0]   # +M3  (east)
    o7 = b.offsets([7])[0]   # +P5  (up-right)
    o3 = b.offsets([3])[0]   # +m3  (up)
    om3 = b.offsets([-3])[0] # -m3  (down)
    C = root; E = add(C, o4); G = add(C, o7)
    Eb = add(C, o3); B = add(E, o7); A = add(C, om3)
    cmaj = [C, E, G]
    P, L, R = [C, Eb, G], [E, G, B], [C, E, A]         # edge-flips
    groups = [
        {'cells': P, 'fill': '#bcd3c8', 'labels': None},
        {'cells': L, 'fill': '#d0c2e2', 'labels': None},
        {'cells': R, 'fill': '#e6d3a2', 'labels': None},
        {'cells': cmaj, 'fill': ACCENT, 'labels': 'note', 'outline': ACCENT},
    ]
    extras = ''
    for cell, lab, col, dy in [(Eb, 'P · C minor', '#3f7a5f', -b.s * 1.35),
                               (B, 'L · E minor', '#6b5b95', -b.s * 1.35),
                               (A, 'R · A minor', '#a07d17', b.s * 1.4)]:
        c = b.cells[cell]
        extras += text(c['cx'], c['cy'] + dy, lab, col, 13, '700')
    write('tonnetz-plr.svg', svg(b, groups, extras, legend=True))


def d_tonnetz_intro():
    """Introduce the Tonnetz: the three directions ARE the three notes of a triad, so a
    triad is a triangle. Label each edge of a C-major triangle with its interval."""
    b = tonnetz(cols=7, rows=5, base=46, s=40)
    root = (2, 2)
    add = lambda cell, o: (cell[0] + o[0], cell[1] + o[1])
    o4 = b.offsets([4])[0]; o7 = b.offsets([7])[0]
    C = root; E = add(C, o4); G = add(C, o7)
    px = lambda k: (b.cells[k]['cx'], b.cells[k]['cy'])
    (cx, cy), (ex, ey), (gx, gy) = px(C), px(E), px(G)
    ctr = ((cx + ex + gx) / 3, (cy + ey + gy) / 3)
    # each edge coloured to match its interval label (and the step-legend arrows)
    extras = (line(cx, cy, ex, ey, GREEN, 5) + line(cx, cy, gx, gy, BLUE, 5) + line(ex, ey, gx, gy, GOLD, 5))

    def edge_label(p1, p2, txt, col):
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        dx, dy = mx - ctr[0], my - ctr[1]           # push outward, away from the triangle
        L = math.hypot(dx, dy) or 1
        off = 52
        return text(mx + dx / L * off, my + dy / L * off, txt, col, 13, '700')
    extras += edge_label((cx, cy), (ex, ey), 'major 3rd', GREEN)     # C–E  (→)
    extras += edge_label((cx, cy), (gx, gy), 'fifth', BLUE)          # C–G  (↗)
    extras += edge_label((ex, ey), (gx, gy), 'minor 3rd', GOLD)      # E–G  (↖)
    groups = [{'cells': [C, E, G], 'fill': ACCENT, 'labels': 'note'}]
    write('tonnetz-intro.svg', svg(b, groups, extras, legend=True))


def d_piano():
    """Contrast: on a piano, C major and F♯ major are different-looking key patterns."""
    ww, wh, bw, bh = 30, 128, 19, 80
    x0, y0, octaves = 12, 14, 2
    whites = [0, 2, 4, 5, 7, 9, 11]       # semitone of each white key in an octave
    # semitone -> (x centre) mapping across the drawn range
    xc = {}
    wx = x0
    for o in range(octaves + 1):
        for i, semi in enumerate(whites):
            pc = semi + 12 * o
            xc[pc] = ('w', wx)
            wx += ww
        if o == octaves:
            break
    # black keys sit between certain whites
    black_after = {0: 1, 2: 3, 5: 6, 7: 8, 9: 10}  # white semitone -> black semitone
    W = wx + x0
    H = y0 + wh + 34
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" font-family="Georgia, serif">']
    hl = {0: ACCENT, 4: ACCENT, 7: ACCENT,             # C major (octave 0)
          14: ACCENT2, 18: ACCENT2, 21: ACCENT2}       # D major — D A white, F♯ black (octave 1)
    # white keys
    wx = x0
    for o in range(octaves):
        for semi in whites:
            pc = semi + 12 * o
            fill = hl.get(pc, '#fdfbf6')
            parts.append(f'<rect x="{wx}" y="{y0}" width="{ww}" height="{wh}" rx="3" fill="{fill}" stroke="#b9b2a4" stroke-width="1.5"/>')
            wx += ww
    # black keys (drawn after, on top)
    wx = x0
    for o in range(octaves):
        for i, semi in enumerate(whites):
            pc = semi + 12 * o
            if semi in black_after:
                bpc = black_after[semi] + 12 * o
                bx = wx + ww - bw / 2
                fill = hl.get(bpc, '#2b2b2b')
                parts.append(f'<rect x="{bx:.1f}" y="{y0}" width="{bw}" height="{bh}" rx="2.5" fill="{fill}" stroke="#000" stroke-width="1"/>')
            wx += ww
    parts.append(text(x0 + 2 * ww, y0 + wh + 20, 'C major', ACCENT, 15, '700', anchor='middle'))
    parts.append(text(x0 + 10 * ww, y0 + wh + 20, 'D major', ACCENT2, 15, '700', anchor='middle'))
    parts.append('</svg>')
    write('piano-contrast.svg', '\n'.join(parts))


def _outline(b, cells, col):
    centres = [(b.cells[k]['cx'], b.cells[k]['cy']) for k in cells]
    h = hull(centres)
    if len(h) < 2:
        return ''
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in h)
    return f'<polygon points="{d}" fill="none" stroke="{col}" stroke-width="3.5"/>'


def d_tritone_sub():
    """Tritone substitution: G7 and D♭7 share the tritone B–F (their 3rd & 7th) and sit a
    tritone apart, so either resolves to C. Shown as two roots hanging off one shared edge."""
    b = wicki(cols=9, rows=6, base=47)
    ref = b.cell_for_note(65, (4, 3))
    cell = lambda n: b.cell_for_note(n, ref)
    F, B = cell(65), cell(71)           # shared tritone (guide tones)
    G, Db = cell(67), cell(73)          # G4 and D♭5 — a tritone apart, opposite sides
    px = lambda k: (b.cells[k]['cx'], b.cells[k]['cy'])
    extras = ''
    for r, col in [(G, ACCENT), (Db, ACCENT2)]:        # each root joins both guide tones
        for t in (F, B):
            extras += line(px(r)[0], px(r)[1], px(t)[0], px(t)[1], col + '88', 2)
    extras += line(px(F)[0], px(F)[1], px(B)[0], px(B)[1], '#333', 3.5, dash='4 4')   # the tritone
    extras += text(px(G)[0], px(G)[1] - b.s * 1.35, 'G7', ACCENT, 14, '800')
    extras += text(px(Db)[0], px(Db)[1] - b.s * 1.35, 'D♭7', ACCENT2, 14, '800')
    extras += text((px(F)[0] + px(B)[0]) / 2, (px(F)[1] + px(B)[1]) / 2 + b.s * 1.15, 'shared tritone', '#555', 12, '700')
    groups = [
        {'cells': [F, B], 'fill': '#6b7280', 'labels': 'note'},   # shared tritone
        {'cells': [G], 'fill': ACCENT, 'labels': 'note'},          # G7 root
        {'cells': [Db], 'fill': ACCENT2, 'labels': 'note'},        # D♭7 root
    ]
    write('tritone-sub.svg', svg(b, groups, extras, legend=True))


def d_extended():
    """Extended chords are stacks of thirds — on the Tonnetz a taller chord is a longer
    staircase. C E G B D F A = triad, 7th, 9th, 11th, 13th."""
    b = tonnetz(cols=8, rows=6, base=44, s=34)
    C = b.cell_for_note(60, (1, 5))
    oM3 = b.offsets([4])[0]   # east
    om3 = b.offsets([3])[0]   # up
    steps = [oM3, om3, oM3, om3, om3, oM3]   # C->E->G->B->D->F->A
    cells = [C]
    for st in steps:
        nx = (cells[-1][0] + st[0], cells[-1][1] + st[1])
        cells.append(nx)
    roles = ['R', '3', '5', '7', '9', '11', '13']
    triad = cells[:3]
    groups = [{'cells': triad, 'fill': ACCENT, 'labels': 'note'},
              {'cells': cells[3:], 'fill': BLUE, 'labels': 'note'}]
    extras = _outline(b, cells, '#8888')
    for cell, role in zip(cells, roles):
        c = b.cells[cell]
        extras += text(c['cx'] + b.s * 1.0, c['cy'], role, INK, 13, '800', anchor='start')
    write('extended-thirds.svg', svg(b, groups, extras, legend=True))


def d_key_distance():
    """Neighbouring keys share almost everything: C major and G major overlap in six notes;
    their fifths-lines differ only at the ends (F vs F♯). Modulation = slide the line one."""
    b = wicki(cols=8, rows=8, base=53, s=28)
    cells = [(i, 7 - i) for i in range(8)]    # F C G D A E B F♯ along the fifths line
    cells = [c for c in cells if c in b.cells]
    shared = cells[1:7]                        # C G D A E B  (in both keys)
    g0, g7 = b.cells[cells[0]], b.cells[cells[-1]]
    extras = (text(g0['cx'] - b.s * 1.2, g0['cy'], 'C major', ACCENT, 13, '800', anchor='end')
              + text(g7['cx'] + b.s * 1.2, g7['cy'], 'G major', ACCENT2, 13, '800', anchor='start'))
    groups = [{'cells': shared, 'fill': '#6b7280', 'labels': 'note'},
              {'cells': [cells[0]], 'fill': ACCENT, 'labels': 'note'},   # F  — C major only
              {'cells': [cells[-1]], 'fill': ACCENT2, 'labels': 'note'}]  # F♯ — G major only
    write('key-distance.svg', svg(b, groups, extras, legend=True))


def d_key_region():
    """A key is a compact region: the seven notes of C major cluster on the Tonnetz, and
    the tonic triad is one triangle inside it."""
    b = tonnetz(cols=7, rows=6, base=47, s=34)
    C = b.cell_for_note(60, (2, 3))
    one = lambda iv: b.cell_for_note(60 + iv, C)
    scale = [one(i) for i in [0, 2, 4, 5, 7, 9, 11]]   # C D E F G A B
    E, G = one(4), one(7)
    extras = _outline(b, scale, ACCENT2 + '99')
    extras += _tri(b, C, E, G, ACCENT)                 # tonic triad triangle inside
    groups = [{'cells': scale, 'fill': '#8a9a6a', 'labels': 'note'},
              {'cells': [C, E, G], 'fill': ACCENT, 'labels': 'note'}]
    write('key-region.svg', svg(b, groups, extras, legend=True))


def d_progression():
    """Root motion by fifths — the engine of tonal harmony — is a straight line. A
    vi–ii–V–I turnaround (Am→Dm→G→C) walks down the up-right (fifths) axis onto the
    tonic: one colour per CHORD (full triads), with the note each pair of neighbouring
    chords shares drawn as a split-coloured hex."""
    b = wicki(cols=8, rows=6, base=48, s=32)
    minor3, major3 = b.offsets([0, 3, 7]), b.offsets([0, 4, 7])
    rA = b.cell_for_note(69, (3, 2))
    rD = b.cell_for_note(62, rA)
    rG = b.cell_for_note(55, rD)
    rC = b.cell_for_note(48, rG)
    chords = [('vi', 'Am', rA, minor3, GOLD),
              ('ii', 'Dm', rD, minor3, GREEN),
              ('V',  'G',  rG, major3, BLUE),
              ('I',  'C',  rC, major3, ACCENT)]
    stamps = [b.place(r, off) for _, _, r, off, _ in chords]
    # consecutive chords share exactly one cell — the common tone handed along
    shared = {}
    for i in range(len(stamps) - 1):
        common = set(stamps[i]) & set(stamps[i + 1])
        assert len(common) == 1, (i, sorted(common))
        shared[common.pop()] = (chords[i][4], chords[i + 1][4])
    groups, extras = [], ''
    for (_, _, _, _, col), cells in zip(chords, stamps):
        groups.append({'cells': [k for k in cells if k not in shared],
                       'fill': col, 'labels': 'note'})
    for i, (cell, (c_prev, c_next)) in enumerate(shared.items()):
        # hard vertical split: earlier (upper-right) chord's colour on the right
        extras += (f'<defs><linearGradient id="gsh{i}" x1="0" y1="0" x2="1" y2="0">'
                   f'<stop offset="0.5" stop-color="{c_next}"/>'
                   f'<stop offset="0.5" stop-color="{c_prev}"/></linearGradient></defs>')
        groups.append({'cells': [cell], 'fill': f'url(#gsh{i})', 'labels': 'note'})
    for (_, _, _, _, col), cells in zip(chords, stamps):
        extras += _blob(b, cells, col)
    for (rom, name, _, _, col), cells in zip(chords, stamps):
        mc = b.cells[max(cells, key=lambda k: b.cells[k]['cx'])]
        extras += text(mc['cx'] + b.s * 1.3, mc['cy'], f'{rom} · {name}',
                       col, 13.5, '800', anchor='start')
    # step order along the bottom so the walk reads at a glance
    o = b.cells[rC]
    x0, y0 = o['cx'] - b.s * 1.6, o['cy'] + b.s * 2.2
    for j, (tok, col) in enumerate([('vi', GOLD), ('→', INK), ('ii', GREEN), ('→', INK),
                                    ('V', BLUE), ('→', INK), ('I', ACCENT)]):
        extras += text(x0 + j * 26, y0, tok, col, 13.5, '800')
    write('progression-fifths.svg', svg(b, groups, extras, legend=True))


# ---------------------------------------------------------------------------
# Post-1 additions: rows, pentatonic, third-side, sequences, chromatic path
# ---------------------------------------------------------------------------

def d_wholetone_rows():
    """Every row IS a whole-tone scale; the two collections alternate rows. Bonus:
    the augmented triad is every-other-button in a row, the tritone is 3 steps."""
    b = wicki(cols=9, rows=5, base=47, s=32)
    TINT_A, TINT_B = '#e4e8d4', '#dde1eb'      # the two whole-tone collections
    LAB_A, LAB_B = '#77824f', '#5f6b8c'
    groups = []
    for r in range(b.rows):
        cells = [(c, r) for c in range(b.cols)]
        even = (b.cells[(0, r)]['note'] % 2 == 0)
        groups.append({'cells': cells, 'fill': TINT_A if even else TINT_B, 'stroke': GRID_STROKE})
    # feature row: the even collection row holding C4 (52 + 2c)
    frow = next(r for r in range(b.rows) if b.cells[(0, r)]['note'] == 52)
    aug = [(4, frow), (6, frow), (8, frow)]    # C E G# — every other button
    groups.append({'cells': aug, 'fill': ACCENT, 'labels': 'note'})
    extras = ''
    for c in range(b.cols):                    # ink labels for the feature row
        if (c, frow) in [tuple(a) for a in aug]:
            continue
        cc = b.cells[(c, frow)]
        extras += text(cc['cx'], cc['cy'], nm(cc['note']), '#6d6455', 13, '600')
    # tritone arc: C (col 4) to F# (col 7) = 3 steps
    cC, cF = b.cells[(4, frow)], b.cells[(7, frow)]
    y0 = cC['cy'] - b.s * 1.0
    extras += (f'<path d="M {cC["cx"]:.1f} {y0:.1f} Q {(cC["cx"] + cF["cx"]) / 2:.1f} '
               f'{y0 - 46:.1f} {cF["cx"]:.1f} {y0:.1f}" fill="none" stroke="#333" '
               f'stroke-width="2.5" marker-end="url(#arrow)"/>')
    extras += text((cC['cx'] + cF['cx']) / 2, y0 - 40, 'tritone = 3 steps', INK, 12.5, '700')
    augc = b.cells[aug[1]]
    extras += text(augc['cx'], augc['cy'] + b.s * 1.35, 'augmented triad = every other button', ACCENT, 12.5, '700')
    # collection tags at row ends
    for r in range(b.rows):
        cc = b.cells[(b.cols - 1, r)]
        even = (b.cells[(0, r)]['note'] % 2 == 0)
        extras += text(cc['cx'] + b.s * 1.5, cc['cy'], 'A' if even else 'B',
                       LAB_A if even else LAB_B, 13, '800', anchor='start')
    write('wholetone-rows.svg', svg(b, groups, extras, legend=True))


def d_french_sixth():
    """The French sixth (A♭ C D F♯) lies in ONE row and maps onto itself under a
    3-step (tritone) shift — it is literally its own tritone substitution."""
    b = wicki(cols=9, rows=5, base=47, s=34)
    frow = next(r for r in range(b.rows) if b.cells[(0, r)]['note'] == 52)
    row_cells = [(c, frow) for c in range(b.cols)]
    fr6 = [(2, frow), (4, frow), (5, frow), (7, frow)]     # A♭ C D F♯
    groups = [
        {'cells': row_cells, 'fill': '#e4e8d4', 'stroke': GRID_STROKE},
        {'cells': fr6, 'fill': ACCENT, 'labels': 'note'},
    ]
    extras = ''
    for c in range(b.cols):
        if (c, frow) in fr6:
            continue
        cc = b.cells[(c, frow)]
        extras += text(cc['cx'], cc['cy'], nm(cc['note']), '#6d6455', 13, '600')
    # two +tritone arcs: A♭ -> D and C -> F♯ (3 steps right each)
    def arc_above(c1, c2, h):
        p, q = b.cells[c1], b.cells[c2]
        y0 = p['cy'] - b.s * 1.05
        return (f'<path d="M {p["cx"]:.1f} {y0:.1f} Q {(p["cx"] + q["cx"]) / 2:.1f} '
                f'{y0 - h:.1f} {q["cx"]:.1f} {y0:.1f}" fill="none" stroke="#333" '
                f'stroke-width="2.5" marker-end="url(#arrow)"/>')
    extras += arc_above((2, frow), (5, frow), 34)
    extras += arc_above((4, frow), (7, frow), 58)
    mid = b.cells[(4, frow)]
    extras += text(mid['cx'] + b.s * 0.9, mid['cy'] - b.s * 2.6, '+ tritone (3 steps)', INK, 13, '700')
    lo = b.cells[(4, frow)]
    extras += text(lo['cx'] + b.s * 0.5, lo['cy'] + b.s * 1.45, 'French sixth on C: A♭ C D F♯', ACCENT, 13.5, '700')
    write('french-sixth.svg', svg(b, groups, extras, legend=True))


def d_pentatonic():
    """The major pentatonic is 5 consecutive fifths — the scale-line with its two
    ends (the tritone pair F–B) trimmed off."""
    b = wicki(cols=8, rows=7, base=53, s=30)
    start = (0, 6)
    cells = [start]
    for _ in range(6):
        nxt = b.cell_for_note(b.cells[cells[-1]]['note'] + 7, cells[-1])
        if nxt and nxt not in cells:
            cells.append(nxt)                  # F C G D A E B
    pent, ends = cells[1:6], [cells[0], cells[-1]]
    F, B = b.cells[ends[0]], b.cells[ends[1]]
    # tritone connector bows out to the right so it doesn't ride the scale line
    mx, my = (F['cx'] + B['cx']) / 2 + b.s * 4.4, (F['cy'] + B['cy']) / 2
    extras = (f'<path d="M {F["cx"] + b.s * 0.8:.1f} {F["cy"]:.1f} Q {mx:.1f} {my:.1f} '
              f'{B["cx"] + b.s * 0.9:.1f} {B["cy"] + b.s * 0.3:.1f}" fill="none" '
              f'stroke="#333" stroke-width="2.5" stroke-dasharray="4 4"/>')
    extras += text(mx - b.s * 1.1, my, 'the scale’s only tritone', '#555', 12.5, '700', anchor='start')
    mid = b.cells[pent[2]]
    extras += text(mid['cx'] - b.s * 1.5, mid['cy'] - b.s * 1.1, 'major pentatonic', ACCENT, 13.5, '800', anchor='end')
    groups = [
        {'cells': pent, 'fill': ACCENT, 'labels': 'note', 'outline': ACCENT},
        {'cells': ends, 'fill': '#6b7280', 'labels': 'note'},
    ]
    write('pentatonic-line.svg', svg(b, groups, extras, legend=True))


def d_third_side():
    """Chord quality = which side of the brightness axis the third sits on: the
    major third leans sharpward of the root–fifth spine, the minor third flatward."""
    b = wicki(cols=10, rows=6, base=45, s=32)
    # C major rooted on C4 (far left), C minor rooted on C5 (right)
    CM = b.cell_for_note(60, (0, 2))
    EM, GM = b.cell_for_note(64, CM), b.cell_for_note(67, CM)
    Cm = b.cell_for_note(72, (7, 2))
    Em, Gm = b.cell_for_note(75, Cm), b.cell_for_note(79, Cm)
    extras = ''
    def harrow(c1, c2, col):
        p, q = b.cells[c1], b.cells[c2]
        sgn = 1 if q['cx'] > p['cx'] else -1
        return line(p['cx'] + sgn * b.s * 0.95, p['cy'], q['cx'] - sgn * b.s * 0.95, q['cy'], col, 3, arrow=True)
    extras += harrow(CM, EM, BLUE)             # root -> major third: 2 steps right (sharp side)
    extras += harrow(Gm, Em, GOLD)             # fifth -> minor third: 2 steps left (flat side)
    cm, cn = b.cells[EM], b.cells[Em]
    extras += text(cm['cx'], cm['cy'] + b.s * 1.4, 'third leans right (sharp side)', BLUE, 12.5, '700')
    extras += text(cn['cx'], cn['cy'] - b.s * 1.5, 'third leans left (flat side)', GOLD, 12.5, '700')
    lM, lm = b.cells[CM], b.cells[Cm]
    extras += text(lM['cx'], lM['cy'] + b.s * 1.55, 'C major', INK, 14, '800')
    extras += text(lm['cx'], lm['cy'] + b.s * 1.55, 'C minor', INK, 14, '800')
    groups = [
        {'cells': [Cm, Gm], 'fill': '#6b7280', 'labels': 'note'},
        {'cells': [CM, GM], 'fill': '#6b7280', 'labels': 'note'},
        {'cells': [EM], 'fill': BLUE, 'labels': 'note'},
        {'cells': [Em], 'fill': GOLD, 'labels': 'note'},
    ]
    write('third-side.svg', svg(b, groups, extras, legend=True))


def _blob(b, cells, col, sw=3):
    """Outline hugging the OUTER boundary of a set of hexes (hull of their corner
    points) — unlike _outline it never strikes through cell labels."""
    pts = []
    for k in cells:
        c = b.cells[k]
        pts.extend(b.hexpts(c['cx'], c['cy'], 1.04))
    h = hull([(round(x, 1), round(y, 1)) for x, y in pts])
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in h)
    return (f'<polygon points="{d}" fill="none" stroke="{col}" stroke-width="{sw}" '
            f'stroke-linejoin="round" opacity="0.85"/>')


def d_dominant_chain():
    """A chain of applied dominants is one dom7 shape rubber-stamped down the fifths
    axis into the tonic: A7 -> D7 -> G7 -> C."""
    b = wicki(cols=8, rows=6, base=48, s=32)
    roots = [b.cell_for_note(n, (3, 2)) for n in [69, 62, 55]]   # A4 D4 G3
    Croot = b.cell_for_note(48, roots[-1])
    dom = b.offsets([0, 4, 7, 10])
    maj = b.offsets([0, 4, 7])
    stamps = [b.place(rc, dom) for rc in roots] + [b.place(Croot, maj)]
    labels = ['A7 = V/V/V', 'D7 = V/V', 'G7 = V', 'C = I']
    cols = [GOLD, GREEN, BLUE, ACCENT]         # same colour language as d_progression
    # consecutive stamps share exactly one cell — the common tone handed along
    shared = {}
    for i in range(len(stamps) - 1):
        common = set(stamps[i]) & set(stamps[i + 1])
        assert len(common) == 1, (i, sorted(common))
        shared[common.pop()] = (cols[i], cols[i + 1])
    groups, extras = [], ''
    for col, cells in zip(cols, stamps):
        groups.append({'cells': [k for k in cells if k not in shared],
                       'fill': col, 'labels': 'note'})
    for i, (cell, (c_prev, c_next)) in enumerate(shared.items()):
        extras += (f'<defs><linearGradient id="gdc{i}" x1="0" y1="0" x2="1" y2="0">'
                   f'<stop offset="0.5" stop-color="{c_next}"/>'
                   f'<stop offset="0.5" stop-color="{c_prev}"/></linearGradient></defs>')
        groups.append({'cells': [cell], 'fill': f'url(#gdc{i})', 'labels': 'note'})
    for col, cells in zip(cols, stamps):
        extras += _blob(b, cells, col)
    # chord tags to the right of each stamp, where the grid is empty
    for col, cells, lab in zip(cols[:3], stamps[:3], labels[:3]):
        c = b.cells[max(cells, key=lambda k: b.cells[k]['cx'])]
        extras += text(c['cx'] + b.s * 1.3, c['cy'], lab, col, 12.5, '800', anchor='start')
    cc = b.cells[Croot]
    extras += text(cc['cx'], cc['cy'] + b.s * 1.5, labels[3], ACCENT, 13, '800')
    write('dominant-chain.svg', svg(b, groups, extras, legend=True))


def d_chromatic_path():
    """The chromatic scale is the LONG way round: each semitone is a big zigzag,
    because the grid sorts notes by harmonic kinship, not by pitch."""
    b = wicki(cols=9, rows=6, base=47, s=32)
    cells = [b.cell_for_note(60, (4, 4))]
    for n in range(61, 73):
        cells.append(b.cell_for_note(n, cells[-1]))
    groups = [
        {'cells': cells[1:-1], 'fill': GOLD, 'labels': 'note'},
        {'cells': [cells[0], cells[-1]], 'fill': ACCENT, 'labels': 'noteoct'},
    ]
    extras = ''
    for i in range(len(cells) - 1):
        p, q = b.cells[cells[i]], b.cells[cells[i + 1]]
        dx, dy = q['cx'] - p['cx'], q['cy'] - p['cy']
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        extras += line(p['cx'] + ux * b.s * 0.9, p['cy'] + uy * b.s * 0.9,
                       q['cx'] - ux * b.s * 0.9, q['cy'] - uy * b.s * 0.9, '#33333388', 2, arrow=True)
    write('chromatic-path.svg', svg(b, groups, extras, legend=True))


# ---------------------------------------------------------------------------
# Post-3 figures: evenness, Euclidean rhythms, Bresenham, the spiral of fifths
# ---------------------------------------------------------------------------

def _clock(cx, cy, R, NR, chosen, labels, fill_on, ring=None, necklace=True):
    """One 12-slot clock face. chosen = set of slots; labels[i] = text per slot."""
    s = ''
    if necklace:
        pts = []
        for i in sorted(chosen):
            a = math.radians(-90 + 30 * i)
            pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
        d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
        s += f'<polygon points="{d}" fill="{fill_on}18" stroke="{fill_on}" stroke-width="2"/>'
    for i in range(12):
        a = math.radians(-90 + 30 * i)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        on = i in chosen
        fill = fill_on if on else GRID_FILL
        tcol = '#fff' if on else MUTED
        rr = NR + 2 if (ring is not None and i == ring) else NR
        stroke = INK if (ring is not None and i == ring) else GRID_STROKE
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
        s += text(x, y, labels[i], tcol, 13, '700')
    return s


def d_evenness_clock():
    """Pick 7 of 12 as evenly as possible (on the chromatic clock) and you are forced
    into the major scale; the 5 left over are the black-key pentatonic."""
    W, H = 560, 560
    CX, CY, R, NR = W / 2, H / 2, 165, 21
    scale = {0, 2, 4, 5, 7, 9, 11}
    labels = [nm(i) for i in range(12)]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
             f'font-family="Georgia, serif" role="img">']
    parts.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{GRID_STROKE}" stroke-width="2"/>')
    parts.append(_clock(CX, CY, R, NR, scale, labels, ACCENT, ring=0))
    # complement drawn as filled dark nodes (the black keys) — overdraw those slots
    for i in [1, 3, 6, 8, 10]:
        a = math.radians(-90 + 30 * i)
        x, y = CX + R * math.cos(a), CY + R * math.sin(a)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{NR}" fill="#3a3a42" stroke="{GRID_STROKE}" stroke-width="1.6"/>')
        parts.append(text(x, y, labels[i], '#fff', 12, '700'))
    # step-size letters between consecutive scale notes
    ordered = sorted(scale) + [12]
    for a0, a1 in zip(ordered[:-1], ordered[1:]):
        gap = a1 - a0
        amid = math.radians(-90 + 30 * (a0 + a1) / 2)
        x, y = CX + (R + 40) * math.cos(amid), CY + (R + 40) * math.sin(amid)
        parts.append(text(x, y, 'L' if gap == 2 else 's', ACCENT if gap == 2 else GOLD, 15, '800'))
    parts.append(text(CX, CY - 14, 'most even 7 of 12', ACCENT, 18, '800'))
    parts.append(text(CX, CY + 12, '= the major scale', INK, 15, '700'))
    parts.append(text(CX, CY + 36, 'leftovers = the black keys', '#3a3a42', 13, '700'))
    parts.append('</svg>')
    write('evenness-clock.svg', '\n'.join(parts))


def d_euclid_pair():
    """The same necklace twice: as a 12-pulse bell rhythm (time) and as the major
    scale (pitch). E(7,12) — Euclid's algorithm output — is both."""
    W, H = 900, 480
    R, NR = 150, 20
    cy = H / 2 + 14
    scale = {0, 2, 4, 5, 7, 9, 11}
    beat_labels = [str(i + 1) for i in range(12)]
    note_labels = [nm(i) for i in range(12)]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
             f'font-family="Georgia, serif" role="img">']
    lx, rx = W * 0.26, W * 0.74
    for cx, chosen, labels, col, title in [
        (lx, scale, beat_labels, ACCENT2, 'a 12-pulse bell rhythm · E(7,12)'),
        (rx, scale, note_labels, ACCENT, 'the major scale · 7 of 12'),
    ]:
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{GRID_STROKE}" stroke-width="2"/>')
        parts.append(_clock(cx, cy, R, NR, chosen, labels, col))
        parts.append(text(cx, 30, title, col, 16, '800'))
    parts.append(text(W / 2, cy, '=', INK, 44, '800'))
    parts.append(text(W / 2, cy + 36, 'same necklace', MUTED, 13, '600'))
    parts.append('</svg>')
    write('euclid-pair.svg', '\n'.join(parts))


def d_bresenham():
    """The major scale as a pixelated straight line: climb 12 semitones in 7 steps
    and the evenest staircase you can draw has risers 2,2,1,2,2,2,1 — LLsLLLs."""
    cw, ch = 46, 26                       # cell width/height of the grid paper
    x0, y0 = 70, 30                       # top-left of plot area
    steps = [0, 2, 4, 5, 7, 9, 11, 12]
    names = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
    Wp, Hp = 7 * cw, 12 * ch
    W, H = x0 + Wp + 120, y0 + Hp + 60
    X = lambda k: x0 + k * cw
    Y = lambda semi: y0 + Hp - semi * ch
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
             f'font-family="Georgia, serif" role="img">']
    for k in range(8):                    # grid paper
        parts.append(line(X(k), Y(0), X(k), Y(12), GRID_STROKE, 1))
    for s_ in range(13):
        parts.append(line(X(0), Y(s_), X(7), Y(s_), GRID_STROKE, 1))
    # the ideal line: slope 12 semitones / 7 steps
    parts.append(line(X(0), Y(0), X(7), Y(12), MUTED, 2.5, dash='6 5'))
    # the staircase
    path = [f'M {X(0):.1f} {Y(0):.1f}']
    for k in range(1, 8):
        path.append(f'L {X(k):.1f} {Y(steps[k - 1]):.1f} L {X(k):.1f} {Y(steps[k]):.1f}')
    parts.append(f'<path d="{" ".join(path)}" fill="none" stroke="{ACCENT}" stroke-width="4" '
                 f'stroke-linejoin="round"/>')
    for k in range(8):                    # note dots + names at each landing
        x, y = X(k), Y(steps[k])
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ACCENT}" stroke="#fff" stroke-width="2"/>')
        parts.append(text(x - 14, y - 10, names[k], INK, 14, '700'))
    for k in range(1, 8):                 # riser sizes: L or s
        gap = steps[k] - steps[k - 1]
        parts.append(text(X(k) + 13, (Y(steps[k - 1]) + Y(steps[k])) / 2,
                          'L' if gap == 2 else 's', ACCENT if gap == 2 else GOLD, 14, '800'))
    parts.append(text(x0 + Wp / 2, y0 + Hp + 34, '7 scale steps →', MUTED, 13, '600'))
    parts.append(text(x0 - 42, y0 + Hp / 2, '12 semitones ↑', MUTED, 13, '600'))
    parts.append(text(X(4) + 30, Y(3.6), 'the ideal line: slope 12/7', MUTED, 12.5, '600', anchor='start'))
    parts.append('</svg>')
    write('bresenham-line.svg', '\n'.join(parts))


def d_spiral():
    """Twelve PURE fifths overshoot seven octaves: the circle of fifths is really a
    spiral that misses closure by the Pythagorean comma (~23.5 cents)."""
    W = H = 600
    CX, CY, R = W / 2, H / 2 + 8, 175
    FIFTH_DEG = 701.955 / 1200 * 360      # a pure 3:2 fifth, as arc around the octave
    names = ['C', 'G', 'D', 'A', 'E', 'B', 'F♯', 'C♯', 'G♯', 'D♯', 'A♯', 'E♯', 'B♯']
    pts = []
    for k in range(13):
        a = math.radians(-90 + k * FIFTH_DEG)
        pts.append((CX + R * math.cos(a), CY + R * math.sin(a), a))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
             f'font-family="Georgia, serif" role="img">',
             '<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
             f'<path d="M0,0 L9,4.5 L0,9 z" fill="{ACCENT}"/></marker></defs>',
             f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{GRID_STROKE}" stroke-width="1.5"/>']
    for i in range(12):                   # hops
        (x1, y1, _), (x2, y2, _) = pts[i], pts[i + 1]
        parts.append(line(x1, y1, x2, y2, BLUE + '77', 2))
    for k, (x, y, a) in enumerate(pts):   # nodes; B# drawn hollow, slightly out
        last = (k == 12)
        rr = 15 if not last else 15
        off = 0 if not last else 26       # push B# outward so the near-miss reads
        xx, yy = CX + (R + off) * math.cos(a), CY + (R + off) * math.sin(a)
        fill = ACCENT if k in (0, 12) else '#6b7280'
        parts.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="{rr}" fill="{fill}" '
                     f'stroke="{"#fff" if not last else INK}" stroke-width="1.6"/>')
        parts.append(text(xx, yy, names[k], '#fff', 12, '700'))
    # the gap: arc from C to B#'s angle
    aC, aB = math.radians(-90), math.radians(-90 + 12 * FIFTH_DEG)
    gx1, gy1 = CX + (R + 52) * math.cos(aC), CY + (R + 52) * math.sin(aC)
    gx2, gy2 = CX + (R + 52) * math.cos(aB), CY + (R + 52) * math.sin(aB)
    parts.append(f'<path d="M {gx1:.1f} {gy1:.1f} A {R + 52:.0f} {R + 52:.0f} 0 0 1 {gx2:.1f} {gy2:.1f}" '
                 f'fill="none" stroke="{ACCENT}" stroke-width="3" marker-end="url(#arr)"/>')
    parts.append(text(CX, CY - R - 76, 'the Pythagorean comma ≈ 23.5¢', ACCENT, 14, '800'))
    parts.append(text(CX, CY + R + 44, '12 pure fifths overshoot 7 octaves — B♯ lands just past C', INK, 14.5, '700'))
    parts.append('</svg>')
    write('spiral-fifths.svg', '\n'.join(parts))


if __name__ == '__main__':
    d_piano()
    d_progression()
    d_tritone_sub()
    d_extended()
    d_key_distance()
    d_key_region()
    d_chord_is_a_shape()
    d_axes()
    d_scale_modes()
    d_negative_harmony()
    d_negative_harmony_inv()
    d_negative_harmony_7ths()
    d_circle_of_fifths()
    d_tonnetz_intro()
    d_symmetric()
    d_tonnetz_plr()
    d_wholetone_rows()
    d_french_sixth()
    d_pentatonic()
    d_third_side()
    d_dominant_chain()
    d_chromatic_path()
    d_evenness_clock()
    d_euclid_pair()
    d_bresenham()
    d_spiral()
    print('done ->', OUT)
