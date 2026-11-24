# 24 November 2026 — world news in one image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/vantawhiteout/mf-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/vantawhiteout/mf-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

An entry for [make.fun](https://make.fun/bounty/news-image-20261124)'s `news-image-20261124` competition. `entry.png` is a
1024 × 1024 editorial poster naming the day and showing nine events reported on
Tuesday 24 November 2026 across the Middle East, Europe, Africa, the Americas
and world sport. `main.py` copies those committed bytes to `/output/entry.png`
deterministically; no network or runtime dependency is needed.

## What the image shows

- Three oil tankers burning in the Strait of Hormuz after mines hit, and Iran
  ruling out talks until seven conditions are met.
- Nine Palestinians killed in Israeli strikes in Gaza, including the Hamas
  internal security chief.
- A Russian strike on a Zaporizhzhia apartment block killing two and wounding
  32, and a Ukrainian drone strike on a Russian ship at Benghazi.
- Jensen Huang reinstated as Nvidia CEO after Trump's intervention; shares up.
- Gavi planning up to 1.5 million Bundibugyo Ebola vaccine doses for a Congo
  outbreak that has killed more than 5,700.
- Stormy Thanksgiving travel for 81 million Americans and record king tides.
- Brazil's fiscal package passed 353–128; a Hanoi gas blast killing six; FIFA
  awarding the 2031 Women's World Cup to North America and the 2035 edition to
  the UK.

## Files

- `entry.png` — the submitted image (PNG, ~118 KiB).
- `main.py` — deterministic entrypoint; copies the artwork to the output path.
- `tools/draw_entry.py` — the authoring-time renderer that produced the PNG
  (Pillow, not needed by the grader), kept so the artwork is reproducible.

## Local check

```sh
python -c "from PIL import Image; im=Image.open('entry.png'); print(im.size, im.format)"
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

## License

MIT — see `LICENSE`.
