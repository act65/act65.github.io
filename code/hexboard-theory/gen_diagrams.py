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
            if g.get('labels') == 'note':
                parts.append(text(c['cx'], c['cy'], nm(c['note']), '#fff', 15, '700'))
            elif g.get('labels') == 'noteoct':
                parts.append(text(c['cx'], c['cy'], nm_oct(c['note']), '#fff', 13, '700'))
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
    vi–ii–V–I turnaround (A→D→G→C) walks down the up-right (fifths) axis onto the tonic."""
    b = wicki(cols=8, rows=6, base=48, s=32)
    C = b.cell_for_note(60, (1, 3))
    cells = [C]
    for _ in range(3):
        nxt = b.cell_for_note(b.cells[cells[-1]]['note'] + 7, cells[-1])
        if nxt and nxt not in cells:
            cells.append(nxt)          # C(I) G(V) D(ii) A(vi) up the fifths line
    roman = ['I', 'V', 'ii', 'vi']
    groups = [{'cells': [cells[0]], 'fill': ACCENT, 'labels': 'note'},          # tonic = home
              {'cells': cells[1:], 'fill': BLUE, 'labels': 'note'}]
    extras = ''
    for i in range(len(cells) - 1, 0, -1):     # arrows point toward the tonic
        p, q = b.cells[cells[i]], b.cells[cells[i - 1]]
        dx, dy = q['cx'] - p['cx'], q['cy'] - p['cy']
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        extras += line(p['cx'] + ux * b.s * 0.98, p['cy'] + uy * b.s * 0.98,
                       q['cx'] - ux * b.s * 0.98, q['cy'] - uy * b.s * 0.98, '#333', 3, arrow=True)
    for i, cell in enumerate(cells):
        c = b.cells[cell]
        extras += text(c['cx'] - b.s * 1.15, c['cy'], roman[i], INK, 15, '800', anchor='end')
    write('progression-fifths.svg', svg(b, groups, extras, legend=True))


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
    d_tonnetz_intro()
    d_symmetric()
    d_tonnetz_plr()
    print('done ->', OUT)
