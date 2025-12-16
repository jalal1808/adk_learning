import uuid
import asyncio

from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types


async def main():
    session_service = InMemorySessionService()

    state_context = {
        "user_name": "JJ",
        "user_post_preferences": """
            - LinkedIn: Professional, engaging, and relevant to the topic.
              should have a primary hook, not more than 60 characters.
              should have a line break after the hook.
              should have a post-hook that supports or inverses the hook.
              should be conversational and easy to read.
              should include bullet points.
              should include actionable items.
              should include a question.
              should ask audience to comment and repost.
              should use emojis.
              should use hashtags.
            - Instagram: Engaging, fast paced.
              should have a strong hook.
              should end with a call to action.
        """,
    }

    SESSION_ID = str(uuid.uuid4())
    USER_ID = "jalal"
    APP_NAME = "Social Media Post Generator"

    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=state_context,
    )

    print("Session ID:", session.id)

    runner = Runner(
        agent=root_agent,
        session_service=session_service,
        app_name=APP_NAME,
    )

    user_query = types.Content(
        role="user",
        parts=[
            types.Part(
                text="What does the user want at the beginning of the post?",
            )
        ],
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_query,
    ):

        if event.is_final_response():
            if event.content and event.content.parts:
                print("Final response:", event.content.parts[0].text)

    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    print("\nSession state:")
    for key, value in session.state.items():
        print(f"{key}: {value}")


asyncio.run(main())
