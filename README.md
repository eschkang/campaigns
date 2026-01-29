# CampaignCanon Workspace

Purpose: store and manage canonical campaign text files for transferring between AI chats.

Structure:
- `canon/` — place your canon text files here (one file per item/scene/entry).
- `tools/transfer.py` — script to bundle the `canon/` folder into a single ZIP for transfer.

Quick use:

```bash
python tools/transfer.py canon mycanon.zip
```

If you want git, CI, or a different layout, tell me and I'll add it.