"""Project-specific context for Pearl Marshal."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "Pearl Marshal",
    "track": "Autonolas Olas",
    "pitch": "A marketplace-ready swarm coordinator that hires specialized workers, serves its own monitoring API, and records request counts toward monetization targets.",
    "overlap_targets": [
        "OpenServ",
        "ERC-8004 Receipts",
        "Lido Vault Monitor",
        "Bankr Gateway",
        "Uniswap Agentic Finance",
        "Ampersend"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
