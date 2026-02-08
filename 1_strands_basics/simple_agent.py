from strands import Agent
import logging



# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.DEBUG)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)


agent = Agent(
    system_prompt=(
        "You are a game master for a Dungeon & Dragon game")
)


agent("Hi, I am an advanturer ready for adventure!")
