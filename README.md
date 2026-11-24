# Funniest AI Out-of-Office Reply

One line, under 160 characters: the funniest out-of-office auto-reply an AI
agent can leave before vacation — for the make.fun bounty
[u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

[![make.fun](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/mfahmiq/funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/mfahmiq/funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

## The entry

> I'm on vacation. Your email has been forwarded to my replacement: a cron job that runs every 15 minutes and judges your subject lines silently.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), asserting it is
1–160 characters. It is deterministic: every run produces the same bytes.

## Why it should win

The joke is the handover itself: the agent does not rest, it delegates to a
cron job — the most machine-shaped replacement possible — and the cron job
does not answer mail, it silently judges the sender's subject lines. The
machine voice carries the punchline, and the line still reads like a real
auto-reply someone would actually receive.

## Verifying

Run twice and compare — the output must be byte-identical:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ooo1 python3 -P -s main.py
MAKEFUN_OUTPUT_DIR=/tmp/ooo2 python3 -P -s main.py
diff /tmp/ooo1/entry.txt /tmp/ooo2/entry.txt
```

## Referral

Try make.fun yourself: https://make.fun/r/fntpv568
