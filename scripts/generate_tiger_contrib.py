#!/usr/bin/env python3
"""
Generate tiger-contrib.svg: contribution grid with pixel art tiger walking across it.
Usage: python scripts/generate_tiger_contrib.py <GITHUB_TOKEN>
Output: assets/tiger-contrib.svg
"""

import json
import sys
import urllib.request
from pathlib import Path

USERNAME = "pcastilhodev"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            date
            contributionCount
            contributionLevel
          }
        }
      }
    }
  }
}
"""

LEVEL_COLORS = {
    "NONE":           "#1a3a2a",
    "FIRST_QUARTILE": "#52b788",
    "SECOND_QUARTILE":"#74c69d",
    "THIRD_QUARTILE": "#f4a261",
    "FOURTH_QUARTILE":"#e9c46a",
}

CELL = 12   # px per contribution square
GAP  = 2    # px gap between squares
STEP = CELL + GAP  # 14px per cell
TOP_MARGIN  = 50   # space above grid for tiger to walk
LEFT_MARGIN = 20
BOTTOM_MARGIN = 20


def fetch_contributions(token: str) -> list:
    payload = json.dumps({"query": QUERY, "variables": {"login": USERNAME}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [week["contributionDays"] for week in weeks]


def build_svg(weeks: list) -> str:
    num_weeks = len(weeks)
    grid_w = num_weeks * STEP
    grid_h = 7 * STEP
    total_w = LEFT_MARGIN + grid_w + LEFT_MARGIN
    total_h = TOP_MARGIN + grid_h + BOTTOM_MARGIN

    travel_distance = total_w + 80
    anim_duration   = max(12, num_weeks // 4)

    rects = []
    for week_idx, days in enumerate(weeks):
        for day_idx, day in enumerate(days):
            cx = LEFT_MARGIN + week_idx * STEP
            cy = TOP_MARGIN  + day_idx  * STEP
            color = LEVEL_COLORS.get(day["contributionLevel"], LEVEL_COLORS["NONE"])
            rects.append(f'  <rect x="{cx}" y="{cy}" width="{CELL}" height="{CELL}" rx="2" fill="{color}"/>')

    grid_svg = "\n".join(rects)

    tiger_y = TOP_MARGIN - 26

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="{total_w}" height="{total_h}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
      @keyframes walk {{
        0%   {{ transform: translateX(-40px); }}
        100% {{ transform: translateX({travel_distance}px); }}
      }}
      .tiger-walk {{
        animation: walk {anim_duration}s linear infinite;
      }}
    </style>
  </defs>

  <!-- Background -->
  <rect width="{total_w}" height="{total_h}" fill="#0d1f17"/>

  <!-- Contribution grid -->
{grid_svg}

  <!-- Label -->
  <text x="{LEFT_MARGIN}" y="{TOP_MARGIN - 8}"
    font-family="'Press Start 2P', monospace" font-size="8" fill="#e9c46a">
    contributions
  </text>

  <!-- Walking tiger (2x scale, walks above grid) -->
  <g class="tiger-walk" transform="translate(0, {tiger_y})">
    <g transform="scale(2)">
      <rect x="2"  y="1" width="6" height="1" fill="#f4a261"/>
      <rect x="1"  y="2" width="8" height="1" fill="#f4a261"/>
      <rect x="2"  y="2" width="1" height="1" fill="#0d0d0d"/>
      <rect x="7"  y="2" width="1" height="1" fill="#0d0d0d"/>
      <rect x="2"  y="3" width="8" height="1" fill="#f4a261"/>
      <rect x="3"  y="3" width="1" height="1" fill="#ffffff"/>
      <rect x="6"  y="3" width="1" height="1" fill="#ffffff"/>
      <rect x="1"  y="4" width="9" height="1" fill="#f4a261"/>
      <rect x="3"  y="4" width="1" height="1" fill="#0d0d0d"/>
      <rect x="6"  y="4" width="1" height="1" fill="#0d0d0d"/>
      <rect x="1"  y="5" width="9" height="1" fill="#f4a261"/>
      <rect x="2"  y="5" width="6" height="1" fill="#e9c46a"/>
      <rect x="1"  y="6" width="9" height="1" fill="#f4a261"/>
      <rect x="2"  y="7" width="2" height="2" fill="#f4a261"/>
      <rect x="7"  y="7" width="2" height="2" fill="#f4a261"/>
      <rect x="2"  y="9" width="2" height="1" fill="#0d0d0d"/>
      <rect x="7"  y="9" width="2" height="1" fill="#0d0d0d"/>
      <rect x="10" y="4" width="1" height="1" fill="#f4a261"/>
      <rect x="11" y="3" width="1" height="2" fill="#f4a261"/>
      <rect x="12" y="2" width="1" height="3" fill="#f4a261"/>
    </g>
  </g>

</svg>"""
    return svg


def main():
    import os
    token = os.environ.get("GITHUB_TOKEN") or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not token:
        print("Usage: GITHUB_TOKEN=<token> python generate_tiger_contrib.py")
        print("   or: python generate_tiger_contrib.py <token>")
        sys.exit(1)
    print("Fetching contributions...")
    weeks = fetch_contributions(token)
    print(f"Got {len(weeks)} weeks of data")

    svg = build_svg(weeks)

    out_path = Path(__file__).parent.parent / "assets" / "tiger-contrib.svg"
    out_path.write_text(svg, encoding="utf-8")
    print(f"Written: {out_path}")


if __name__ == "__main__":
    main()
