[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Jideweb3/news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Jideweb3/news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

# The World Today — Classic Broadsheet

This entry is a small Python program whose output is a single image:
**The World Today**, a classic newspaper front page summing up the world
news of **Thursday, 19 November 2026** — 39 stories, 19 of them in
pictures, every continent, all from this one day. The design source is
`page.html`; its rendered form is `entry.png` (1024×1024), and `main.py`
simply delivers that image to the output directory, byte for byte. A
slim edition of the same page, encoded as a JPEG of 300,908 bytes, sits
in `slim/` (and as `entry-slim.jpg.png`) with its own copy of `main.py`.

## Design

A dense classic broadsheet in the old front-page manner: cream paper
(#f6efdd), black ink, and a big red masthead band (#c8102e) carrying the
name in white condensed type. Under it, the date — **THURSDAY 19
NOVEMBER 2026** — in large serif, then a numbers strip of six figures
from the day. One huge lead (the Shenzhen summit) with a big picture;
two secondary leads (the Anthropic IPO, GTA VI) beside it; a strip of
four more pictured stories; then the day in full: three dense columns
where pictured stories sit scattered among numbered text stories, every
story carrying its number in a red chip. A world map ("Where it
happened") and a date-check line close the page. Georgia serif for
headlines, Arial for kickers, decks and briefs — all text is real HTML
text, never baked into the pictures. Pictures are a mix of real
photographs and editorial illustrations, credited in `SOURCES.md`.

`entry.png` is rendered from `page.html` with headless Chrome at
1024×1024 and is 648,984 bytes — under the 1 MiB limit.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`. Without `MAKEFUN_OUTPUT_DIR` the program
writes to `/output/entry.png`. It uses only the Python 3 standard
library and checks that the copied bytes match the source before
exiting.

## The 39 stories

**Leads and pictured strip**

1. Trump, Xi & Putin meet in Shenzhen — nuclear arms, Ukraine and Iran
   top the agenda at the APEC summit. *(photo)*
2. Biggest IPO ever: Anthropic lands on Nasdaq — $81.3bn raised at $83
   a share, past SpaceX's record; shares jump 34% on day one. *(photo)*
3. GTA VI is out: the 13-year wait ends — the most awaited game on
   earth finally launches. *(photo)*
4. World Court: Myanmar committed genocide — first ruling of its kind,
   on the Rohingya case. *(photo)*
5. 3 tankers burn after mines in Hormuz. *(photo)*
6. Ukraine hits Crimea Bridge again. *(photo)*
7. COP31 down to the wire over fossil fuels. *(illustration)*

**The day in full — pictured**

8. Israel opens ground operation in central Gaza — troops operate in
   the Nuseirat area amid claims of ceasefire violations.
   *(illustration)*
9. Houthi missile damages Riyadh tower — damage reported at a
   prominent tower in the capital's financial district.
   *(illustration)*
10. Seoul court clears ex-PM over martial law. *(illustration)*
11. North Korea expands uranium plant — IAEA — Yongbyon extension
    finished in late October, the agency says. *(illustration)*
12. Bangladesh switches on first nuclear plant. *(illustration)*
13. 72,000 flee Cyclone Akvan in India — coastal communities evacuated
    as the storm threatens the east coast. *(photo)*
14. El Niño rains flood South Florida. *(photo)*
15. Russian strike on Odesa kills 4, injures 13. *(illustration)*
16. Zelenskyy: no peace deal without Ukraine — Kyiv insists it must
    sit at any table that decides its future. *(photo)*
19. Van Gogh painting sells for $190.4 million — the sale follows a
    fight over its Nazi-era ownership history. *(photo)*
29. Red crabs march on Christmas Island — millions of crabs begin the
    annual migration to the sea. *(photo)*

**The day in full — text stories**

17. US & Venezuela restore military ties — Hegseth announced the deal
    on a visit to Caracas.
18. Senegal migrant boat sinks — dozens missing; about 100 people were
    aboard the boat.
20. Ethiopia–Eritrea clashes raise war fears.
21. Bangladesh unrest: Yunus home set ablaze — the ancestral home was
    attacked amid Awami League protests.
22. EU delays methane rules after US pressure.
23. European Commission hit by cyberattack.
24. Fiji declares disaster in El Niño drought — the drought threatens
    water supplies across the islands.
25. Seoul's Lee calls for talks with North Korea.
26. South Korea sits Suneung exam day.
27. Australia jobless rate rises to 4.9%.
28. Miami court convicts pastor in Haiti case — the case stems from
    the 2021 assassination of President Moïse.
30. NZ court: pay-equity changes broke rights.
31. DR Congo Ebola response battles insecurity.
32. Musk regrets scale of midterm spending — his remarks renew debate
    over big money in elections.
33. Sudan: RSF commander defects to the army — the defection adds to
    uncertainty in the civil war.
34. Russian charged over spying on Palantir staff — US authorities say
    defence-tech workers were targeted.
35. El Salvador sends 2,500 troops to Haiti — the deployment supports
    security operations there.
36. Prince Harry: I would serve again against Russia — a personal
    remark, not a policy announcement.
37. Indonesia passes asset-forfeiture law — the move targets proceeds
    of criminal activity.
38. AI chip fight at the heart of US–China talks — Trump raised
    Nvidia's Jensen Huang with Xi.
39. Arab League condemns Gaza hospital attacks — it denounced strikes
    affecting medical facilities.

Stories 32–39 are additional reporting from the Open Chronicle Global
News Brief for 19 November 2026; see `SOURCES.md`.
