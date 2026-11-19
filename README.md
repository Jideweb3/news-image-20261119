[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Jideweb3/news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Jideweb3/news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

# The World Today — Photo Edition (XS File)

This version carries the exact same page as the Photo Edition, encoded
as a JPEG under 150 KB instead of a PNG.

This entry is a small Python program whose output is a single image:
**The World Today**, a newspaper front page summing up the world news of
**Thursday, 19 November 2026** — 31 stories, every continent, all from
this one day. The design source is `page.html`; its rendered form is
`entry.png` (1024×1024), and `main.py` simply delivers that image to the
output directory, byte for byte.

## Design

A premium broadsheet: cream paper (#faf5ea), black ink, one red accent
(#c8102e), gold secondary. Georgia serif for the masthead and headlines,
Arial for kickers, decks and briefs — all text is real HTML text, never
baked into the pictures. The pictures are real photographs, credited in
`SOURCES.md` and flattened into `entry.png`: a summit table with the
three presidents, the New York trading floor on IPO day, the GTA VI key
art, the Peace Palace in The Hague, a burning tanker, the Crimea Bridge,
and a real world map with red pins. From top to bottom: the masthead and
the red date band; a numbers strip of six figures from the day; the
summit lead; two half-width photo stories; three third-width photo
stories; a grid of eight text cards; the map ("Where it happened")
beside a numbered briefs column ("Also on Thursday"); and a footer
date-check line confirming every story is from Thursday 19 November
2026, with sources (Reuters · AP · AFP · Yonhap · Al Jazeera · IAEA ·
ICJ).

`entry.png` is the page rendered from `page.html` at 1024×1024, encoded
from the lossless render as a JPEG of 144,753 bytes — well under the
1 MiB limit.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`. Without `MAKEFUN_OUTPUT_DIR` the program
writes to `/output/entry.png`. It uses only the Python 3 standard
library and checks that the copied bytes match the source before
exiting.

## The 31 stories

**Photo stories**

1. Trump, Xi & Putin meet in Shenzhen — nuclear arms, Ukraine and Iran
   top the agenda at the APEC summit.
2. Biggest IPO ever: Anthropic lands on Nasdaq — $81bn raised at $83 a
   share, past SpaceX's record.
3. GTA VI is out: the 13-year wait ends — the most awaited game on earth
   finally launches.
4. World Court: Myanmar committed genocide — first ruling of its kind,
   on the Rohingya case.
5. 3 tankers burn after mines in Hormuz.
6. Ukraine hits Crimea Bridge again.

**Card grid**

7. COP31 down to the wire over fossil fuels.
8. Israel opens ground operation in central Gaza.
9. Houthi missile damages Riyadh tower.
10. Seoul court clears ex-PM over martial law.
11. North Korea expands uranium plant — IAEA.
12. Bangladesh switches on first nuclear plant.
13. 72,000 flee Cyclone Akvan in India.
14. El Niño rains flood South Florida.

**Also on Thursday (briefs)**

15. Russian strike on Odesa kills 4, injures 13.
16. Zelenskyy: no peace deal without Ukraine.
17. US & Venezuela restore military ties.
18. Senegal migrant boat sinks — dozens missing.
19. Van Gogh painting sells for $190.4 million.
20. Ethiopia–Eritrea clashes raise war fears.
21. Bangladesh unrest: Yunus home set ablaze.
22. EU delays methane rules after US pressure.
23. European Commission hit by cyberattack.
24. Fiji declares disaster in El Niño drought.
25. Seoul's Lee calls for talks with North Korea.
26. South Korea sits Suneung exam day.
27. Australia jobless rate rises to 4.9%.
28. Miami court convicts pastor in Haiti case.
29. Red crabs march on Christmas Island.
30. NZ court: pay-equity changes broke rights.
31. DR Congo Ebola response battles insecurity.
