# Evidence - GenLayer Intelligent Oracle

## Overview
This repository contains a decentralized intelligent oracle contract primitive designed for GenLayer. It handles multi-validator consensus to fetch, verify, and store external price feed data securely.

## Implementation Details
- **Contract Logic:** Fetches external API data and utilizes GenLayer's AI consensus engine to validate state parameters.
- **Verification & Tolerance:** Evaluates consensus across multiple nodes with strict equivalence checking to prevent malicious data injection.
- **Execution States:** APPROVED, DENIED, and UNVERIFIED states are handled programmatically before updating on-chain states.

## Verification Steps
1. Deploy the contract on the GenLayer testnet simulator.
2. Trigger the price fetch method with valid source URLs.
3. Observe validator nodes reaching a deterministic verdict through equivalence checks.
# genlayer-intelligent-oracle
Decentralized intelligent oracle contract primitive built for GenLayer.
