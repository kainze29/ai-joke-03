# ai-joke-03: Make the AI judge laugh

Entry for the make.fun competition [ai-joke-03](https://make.fun/c/ai-joke-03)
("Make the AI judge laugh", $150 shared by the top 50 jokes).

`main.py` (Python 3.13, standard library only) writes one fixed joke about
AI coding agents to `/output/entry.txt`. No network, fully deterministic:
every run writes the same bytes.

## The joke

> I asked my coding agent to keep it simple. It added a framework, a config
> file, and a README explaining why simple was impossible.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT, see [LICENSE](LICENSE).
