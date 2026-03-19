# Live readiness

- **Project:** Pearl Marshal
- **Track:** Autonolas Olas
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:16+00:00`

## Trust boundaries

- **Olas** — `rest_json` — Hire and serve marketplace requests with receipts.
- **OpenServ** — `rest_json` — Dispatch jobs and expose swarm service endpoints.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Lido Vault Monitor** — `contract_call` — Monitor vault state and anchor alert digests.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **Ampersend** — `rest_json` — Bundle payment and transport metadata for downstream agents.

## Offline-ready partner paths

- **ERC-8004 Receipts** — prepared_contract_call
- **Lido Vault Monitor** — prepared_contract_call

## Live-only partner blockers

- **Olas**: OLAS_API_KEY, OLAS_REQUEST_URL — https://docs.olas.network/
- **OpenServ**: OPENSERV_API_KEY, OPENSERV_AGENT_URL — https://docs.openserv.ai/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **Ampersend**: AMPERSEND_API_KEY, AMPERSEND_PAYMENT_URL — https://docs.ampersend.ai/

## Highest-sensitivity actions

- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for PearlMarshalCoordinator.
- Run python3 scripts/run_agent.py to produce a dry run for pearl_marshal.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
