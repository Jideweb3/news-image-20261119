[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Jideweb3/news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Jideweb3/news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

# The World Today · Night Edition — a one-image news summary

This entry is a small Python program whose output is a single image:
**The World Today · Night Edition**, a portrait news poster summing up the
world news of **Thursday, 19 November 2026** — 31 stories, every continent,
all from this one day. The design lives in `art.svg`; its rendered form is
`entry.png` (864×1024), and `main.py` simply delivers that image to the
output directory, byte for byte.

## Design

A deliberate break from the cream broadsheet: a deep ink-navy page
(#101d33) with warm cream story cards (#faf5ea), full-colour flat vector
illustrations, gold rules and figures, and one strong red for the date
band. From top to bottom: the masthead and the date in the largest type on
the page; a strip of seven region chips with story counts; a numbers strip
of six big gold figures from the day; four large illustrated lead cards; a
grid of ten smaller illustrated cards; a dotted world map ("Where it
happened") with numbered pins beside a numbered briefs column ("Also on
Thursday"); and a footer date-check line confirming every story is from
Thursday 19 November 2026, with sources (Reuters · AP · AFP · Yonhap ·
Al Jazeera · IAEA · ICJ).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`. Without `MAKEFUN_OUTPUT_DIR` the program writes
to `/output/entry.png`. It uses only the Python 3 standard library and checks
that the copied bytes match the source before exiting.

## The 31 stories

**Leads**

1. Trump, Xi & Putin meet in Shenzhen — nuclear arms, Ukraine and Iran top
   the agenda at the APEC summit.
2. Biggest IPO ever: Anthropic lands on Nasdaq — $81bn raised at $83 a
   share, past SpaceX's record.
3. World Court: Myanmar committed genocide — first ruling of its kind, on
   the Rohingya case.
4. GTA VI is out: the 13-year wait ends — the most awaited game on earth
   finally launches.

**Card grid**

5. COP31 down to the wire over fossil fuels.
6. 3 tankers burn after mines in Hormuz.
7. Ukraine hits Crimea Bridge again.
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
