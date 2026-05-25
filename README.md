# 🤖 Autonomous WhatsApp Updates Agent

An autonomous mobile agent built on the [Droidrun](https://droidrun.ai/) framework that reads your 
unread WhatsApp messages and writes a clean daily summary — all without you lifting a finger.

## 📖 Overview

The agent opens WhatsApp, scrolls through unread chats (including communities and announcement groups),
and synthesizes everything into a structured daily summary written directly into the Notes app,
titled **"WhatsApp Updates"**.

If certain messages can't be fully accessed, the agent transparently reports this in the summary
rather than silently skipping them.

## ⚙️ What the Agent Does

- Opens WhatsApp and navigates to unread chats
- Handles communities and announcement groups
- Scrolls through unread messages to capture content
- Synthesizes information into a dated, structured summary
- Writes the final summary into the Notes app

## 💡 Why This Matters

Unread messages pile up across dozens of chats and communities.
This agent eliminates that cognitive overload by converting scattered conversations
into one clean, actionable daily update — automatically.

## 🛠️ Technology Stack

| Component | Details |
|---|---|
| Agent Framework | [Droidrun](https://github.com/droidrun/droidrun) |
| Execution Environment | Mobilerun Playground |
| LLM Execution | Vision-enabled (screenshot-based UI understanding) |
| Device Automation | Android |

## 🎬 Demo

Full autonomous execution — no manual interaction performed.

[![Demo](https://img.youtube.com/vi/rP30O6gL1PA/maxresdefault.jpg)](https://www.youtube.com/watch?v=rP30O6gL1PA)

> Click to watch on YouTube

## 📌 Notes

This repository focuses on agent logic and reproducibility.
Execution is demonstrated via the Mobilerun Playground for reliability and consistency.
