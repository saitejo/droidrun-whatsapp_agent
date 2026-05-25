"""
Autonomous WhatsApp Updates Agent
Built for the Droidrun DevSprint submission.
Execution demonstrated via the Mobilerun Playground.
"""

import asyncio
from dotenv import load_dotenv
from droidrun import DroidAgent, AdbTools

load_dotenv()

GOAL = """
Open WhatsApp and navigate to unread chats, including communities
and announcement groups. Scroll through unread messages to capture
their content. Then open the Notes app and write a structured,
dated summary titled 'WhatsApp Updates'. If any messages cannot
be fully accessed, report them transparently in the summary.
"""

async def main():
    tools = await AdbTools.create()
    agent = DroidAgent(
        goal=GOAL,
        tools=tools,
        llm="claude-sonnet-4-20250514",  # swap with gpt-4o or gemini if needed
        vision=True,
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
