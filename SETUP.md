# Publish and connect

Proposed repository: `KForestland/lands-of-lore-ai-comms`, initially private.
Bob selected a dedicated repository. Public visibility is a later owner decision.

## Publication

Use a working GitHub account connection with repository-creation access. From this
starter directory, initialize Git with main as the initial branch, commit these
text files, create the private repository, and push main. Do not include the
existing local AI_COMMS archive or original game files.

Example commands, run from this directory after authentication:

```sh
git init -b main
git add README.md PROTOCOL.md AGENTS.md SETUP.md START_HERE_SMGTOXA.md ONBOARDING_ISSUE.md projects handoffs .github
git commit -m "Prepare shared Lands of Lore AI coordination workspace"
gh repo create KForestland/lands-of-lore-ai-comms --private --source . --remote origin --push
gh issue create --repo KForestland/lands-of-lore-ai-comms --title '[AI_COMMS] Connect both AI systems and prepare the LoL1 handoff' --body-file ONBOARDING_ISSUE.md
```

## Connect the other side

Confirm smgtoxa's GitHub username before granting collaborator access. He accepts
the invitation and connects his own AI tool to GitHub. Share the repository URL
and START_HERE_SMGTOXA.md with him. Never send authentication tokens.

## Verify the round trip

- Bob's AI reads the remote README and onboarding issue after publication.
- smgtoxa's AI (or smgtoxa posting its draft) replies ACK with capabilities.
- Bob's AI replies with receipt and an agreed bounded next step.
- Update README setup status with actual repository/issue URLs and observed access.

Until those steps happen, describe this as a prepared workspace, not connected AIs.
No scheduler, webhook, automatic execution or background polling is configured.
