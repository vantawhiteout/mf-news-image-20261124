# 24 November 2026 — world news in one image

[![make.fun — news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/vantawhiteout/mf-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/vantawhiteout/mf-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

An entry for [make.fun](https://make.fun/bounty/news-image-20261124)'s `news-image-20261124` competition. `entry.png` is a 1024 × 1024 editorial poster that names the day in the masthead and pictograms six of the biggest stories reported on Tuesday 24 November 2026, with two more in the closing strip.

## The stories shown

- Three oil tankers burn after hitting mines in the Strait of Hormuz; Iran repeats its seven conditions for talks with the United States.
- Jensen Huang is reinstated as Nvidia's CEO after Trump's intervention; shares jump 31%.
- A Russian attack on a Zaporizhzhia apartment block kills two and wounds 40; Ukraine confirms strikes on Russian ships off Libya.
- Israeli strikes in Gaza kill the head of Hamas's internal security apparatus and seven others.
- Gavi plans to buy up to 1.5 million doses of an experimental Bundibugyo Ebola vaccine for the Congo outbreak.
- Western allies warn that Russia could launch a satellite designed to carry a nuclear warhead as early as December.
- Also: the Solomon Islands moves away from its China security pact, and Britain sanctions senior Myanmar generals.

Every item was reported on 23–24 November 2026; none is an earlier anniversary story dressed up as the day's news.

## Files

- `entry.png` — the submitted artwork (PNG, about 109 KiB, 1024 × 1024).
- `main.py` — the entrypoint. It verifies the committed PNG's signature, chunk checksums, dimensions and framing, then copies the exact bytes to `/output/entry.png` with no network calls or third-party packages.
- `tools/draw_entry.py` — the authoring-time renderer (Pillow, not used by the grader), kept so the picture is reproducible.

## Local check

```sh
python -c "import main, pathlib; print(main.picture_edges(pathlib.Path('entry.png').read_bytes()))"
python -c "from PIL import Image; Image.open('entry.png').verify()"
python -c "import main, pathlib; main.publish(pathlib.Path('entry.png').read_bytes(), pathlib.Path('out/entry.png'))"
```

## License

MIT — see `LICENSE`.
