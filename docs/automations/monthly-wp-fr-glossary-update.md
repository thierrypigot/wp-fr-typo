# Monthly WP FR glossary update

Template for a [Cursor Automation](https://cursor.com/docs/cloud-agent/automations.md).  
Cursor does **not** load this file automatically — copy the fields into the Automations editor, then save and activate.

Contains no secrets, tokens, or Slack channel IDs.

## Name

```
Monthly WP FR glossary update
```

## Description

```
On the 10th of each month, refresh the official WordPress French glossary and open a PR if anything changed.
```

## Trigger

- Type: On a schedule / custom cron
- Expression:

```
0 9 10 * *
```

(= 10th of each month at 09:00 — confirm timezone in the picker)

## Repository

- Repo: `Thivinfo/wp-fr-typo`
- Branch: `main`

## Tools

- Open pull requests: on (default for repo-backed automations)
- Send to Slack (optional): pick a **public** channel in the editor after connecting Slack. Invite `@Cursor` to that channel.

## Instructions

```
Fetch the official French WordPress glossary from https://translate.wordpress.org/locale/fr/default/glossary/.

Rebuild references/glossaire.md in the existing format: header with term count and last-update date, the usage-rules section (keep it), then A–Z tables with columns Anglais | Français | Nature | Notes. Prefer the official export or structured page data over noisy HTML chrome.

Also sync the glossary date and term count in SKILL.md and README.md wherever those stamps or badges appear.

If nothing meaningful changed, do not open a pull request. If Slack is connected, post a short "no changes" note.

If terms changed, open a pull request summarizing added, updated, and removed entries. If Slack is connected, post a short status with the PR link and counts.
```

## After paste

1. Confirm 09:00 timezone if shown.
2. Connect Slack in the editor if you want notifications, then choose a public channel.
3. Save and activate.
