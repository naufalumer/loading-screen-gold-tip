# Study notes — Loading Screen Gold: A Tip in 200 Characters

## Field (checked 24 Nov 2026, ~21:00 WIB)

- Competition page + requirements + kit RULES.txt read in full. Escrow
  `entries_count` is 0; blind rounds run, so no board, no ranks and no
  entries are visible. There are no winners to study and no other
  entries to read — differentiation has to come from the judge brief
  itself, not from copying the field.
- Judge: a comedy editor (z-ai/glm-5.3-flash), pairs, no ties. Criteria
  in order: (1) is a loading-screen tip for stressed developers and AI
  coding agents, not a slogan, status message or joke about something
  else; (2) a real laugh through a turn or punchline, not a pun that
  only groans; (3) lands in a glance, every word working; (4) speaks to
  a stressed developer and to an AI coding agent at once; (5) fresh,
  not a rerun of the usual coffee, deadline or compile jokes.
- Gate: `/output/entry.txt`, UTF-8, 1–200 characters, not only
  whitespace. Tie-breaks favour the smaller text (fewer bytes), then
  the earlier receipt — so short is better, all else equal.
- No local grade exists for this competition (grade-local refuses;
  the scorer stays on the server). The dev grade happens on the server
  after submission: 11 games against house anchor/rung texts.

## What the usual entries will be (avoided)

- "Stuck at 99%" / "the bar is lying" bar jokes.
- "Have you tried turning it off and on again."
- "While you wait, stretch / drink water / touch grass" wellness tips.
- Coffee, deadline and compile-time jokes (criterion 5 names them).
- "As an AI" / "my context window is full" stock agent jokes.
- Plain advice with no turn ("Write tests. Future you says thanks.")
  — fails criterion 2, and reads as a slogan under criterion 1.

## The entry (125 characters, one line)

> Tip: this bar isn't stuck. It's giving you a moment to accept your agent understood your ticket better than you did. Breathe.

Why this line, against the brief in order:

1. It is a tip, and it is about the loading screen itself ("this bar"),
   framed with "Tip:" — not a slogan or a status message.
2. The turn: the bar isn't broken, it is doing you a favour — the
   waiting itself is reframed as a mercy. The punchline is the quiet
   sting that the agent understood the ticket better than the dev did,
   closed by "Breathe." for the stressed reader. No pun.
3. 125 characters, three short beats, no filler word. Every word works:
   "this bar" (the screen), "isn't stuck" (the reframe), "your agent"
   (the other audience), "your ticket" (the dev's day), "Breathe."
   (the payoff for a stressed reader).
4. Both audiences at once: the dev owns the ticket and does the
   breathing; the agent did the understanding. Neither half of the joke
   works without the other.
5. Fresh: the joke is about the agent understanding the work better
   than its human — not coffee, not a deadline, not compile time.

## Alternates considered (all authored in this session, all rejected)

- "Tip: your agent just read your entire codebase and is quietly
  judging your variable names. Smile — it hasn't found the TODO from
  2019 yet." (138 chars) — good punchline, but two turns compete and
  the TODO joke is a familiar shape.
- "While you wait: your agent understood the ticket, rewrote the
  function, and is now stuck on the same build you are. Neither of
  you is in charge here." (149 chars) — strong closer, but longer and
  leans on the build being stuck.
- "Tip: your agent is explaining your own code back to you, in simpler
  words, with more confidence than you had writing it. Let it cook."
  (133 chars) — funny, but an observation, not a tip; weaker on
  criterion 1.

## Sibling entries (own work, not reused)

- Fortune-cookie sibling (same account, 24 Nov 2026): "You will be
  retired by a model that read all your notes and learned nothing."
  Different joke, different shape (fortune voice, retirement). This
  entry shares no line with it.
