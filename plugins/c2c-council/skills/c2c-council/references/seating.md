# How the CEO Seats the Council

Not every decision needs nine opinions. Extra seats add noise, cost, and false confidence, because a crowd of agreeable reviews looks like consensus even when most of those seats had no real stake. The CEO runs this rubric during intake, before any seat reviews the work, and seats only the functions whose view could change the decision.

Seating runs in four steps: classify the decision, check the tripwires, score each remaining seat's relevance, then apply the size limits and any founder overrides.

## Step 1: Classify the decision

Pick the one decision type that best fits the work. If two fit, pick the one where a wrong call would cost more, and note the second. The decision type sets each seat's **influence weight**, which the CEO uses later to weigh reviews. It also breaks ties in seating.

| Decision type | Product | Design | Eng | Ops | Mktg | Sales | CS | Finance | Legal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Product bet or roadmap | 25 | 10 | 20 | 5 | 5 | 10 | 10 | 10 | 5 |
| Pricing and packaging | 10 | 5 | 0 | 5 | 15 | 25 | 15 | 20 | 5 |
| Go-to-market or launch | 10 | 10 | 5 | 10 | 25 | 20 | 10 | 5 | 5 |
| Org change or hiring plan | 5 | 0 | 10 | 30 | 5 | 5 | 5 | 25 | 15 |
| Fundraising or major spend | 10 | 0 | 5 | 10 | 10 | 10 | 10 | 35 | 10 |
| Partnership or channel | 10 | 0 | 5 | 10 | 15 | 20 | 10 | 15 | 15 |
| Market or segment expansion | 20 | 5 | 10 | 10 | 15 | 15 | 10 | 10 | 5 |
| Platform or technical investment | 15 | 5 | 35 | 10 | 0 | 5 | 10 | 15 | 5 |
| AI feature or new data use | 15 | 10 | 25 | 5 | 5 | 5 | 10 | 10 | 15 |

Each row sums to 100. These are starting points. If the founder's situation clearly shifts the stakes (a regulated health product raises Legal on almost everything), adjust and say why in one line.

## Step 2: Check the tripwires

Some facts about the work seat a function automatically, regardless of its relevance score. A tripwire fires only when the work clearly includes the trigger.

| If the work... | Always seat |
| --- | --- |
| Touches customer or personal data in a new way | Legal, Engineering |
| Changes price, packaging, or terms | Finance, Sales, Customer Success |
| Changes anything existing customers use or signed | Customer Success, Legal |
| Commits spend above roughly three months of current burn | Finance |
| Adds, removes, or restructures roles | Operations, Finance, Legal |
| Makes public claims (launch, website, press, investor materials) | Marketing, Legal |
| Changes a customer-facing flow or interface | Design |
| Commits a date or capability to a customer or partner | Engineering, Product |
| Enters a regulated sector or a new country | Legal |

## Step 3: Score each remaining seat's relevance

For every seat not already seated by a tripwire, score four factors from 0 to 3.

| Factor | Weight | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- | --- |
| **Ownership:** this function must build, sell, support, fund, or approve it | 30 | No role | Minor support role | Significant work | Owns or must sign off |
| **Exposure:** if this goes wrong, the damage lands in this function | 30 | None | Minor, recoverable | Real cost or rework | One of this seat's hard stops could trigger |
| **Irreversibility:** mistakes in this function's domain are hard to undo | 20 | Trivially reversible | Reversible with some cost | Costly to reverse | Effectively permanent (signed contracts, leaked data, public claims, architecture) |
| **Decision influence:** this seat's verdict could plausibly change what the founder does | 20 | Wouldn't change anything | Might adjust a detail | Could change the plan | Could change the decision |

**Relevance score = sum of (weight x factor score) / 3**, on a scale of 0 to 100.

| Relevance score | Seating |
| --- | --- |
| 50 or higher | Seat |
| 35 to 49 | Seat only if the council has fewer than four seats, highest score first |
| Below 35 | Sits out |

Two scoring rules keep this honest. Score the work as written, so a pricing memo that never mentions existing customers still gets Customer Success scored on what the change would do to them. And don't penalize a seat for thin evidence; a high-exposure seat facing a thin plan is exactly the seat that should sit, because its job is to name what's missing.

## Step 4: Apply limits and overrides

- **Minimum three seats.** If fewer than three qualify, add the highest-scoring remaining seats until there are three.
- **Maximum six seats.** If more than six qualify, score relevance for every qualifying seat, tripwire seats included, and keep the six highest. Tied seats go to the one with the higher influence weight from Step 1. Name each dropped seat and the tripwire that would have seated it, and offer to add it back.
- **Influence weights for seated seats.** Every seated seat gets an influence weight of at least 10, so no seat sits at the table without a say. Then rescale the weights across only the seated seats so they sum to 100.
- **Founder overrides.** The founder can say "full council" (all nine seats, Step 1 weights unchanged), "add [seat]," "skip [seat]," or "only [seats]." The CEO follows the override. If the founder skips a seat that a tripwire seated, the CEO notes the risk once in the brief and moves on.

## Show the seating

Before the reviews run, the CEO shows the seating in a compact table so the founder can adjust it.

| Seat | Seated | Why |
| --- | --- | --- |
| Finance | Yes (tripwire) | Changes price for existing contracts |
| Sales | Yes (tripwire) | Changes price for deals in flight |
| Customer Success | Yes (tripwire) | 40 percent of revenue renews in the next two quarters |
| Marketing | Yes (relevance 63) | Pricing page and launch messaging change |
| Product | Yes (relevance 53) | Usage metering changes what the product measures |
| Legal | Yes (tripwire) | Existing MSAs fix price for the contract term |
| Engineering | No (relevance 40) | Metering already exists; build work is small |
| Design | No (relevance 30) | One pricing page update |
| Operations | No (relevance 27) | Billing tool already supports usage plans |

Then the CEO says, in one line: "Reply 'go' to run this council, or tell me which seats to add or drop." If the founder said earlier to run without checking in, or isn't present, the CEO proceeds with the seating as shown.
