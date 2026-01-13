from pydantic_ai.agent import AgentRunResult
from pydantic_ai import Agent
from dotenv import load_dotenv


load_dotenv()

class BruttlerBot:
    def __init__(self):
        self.chat_agent = Agent(
            "gemini-2.5-flash",
            system_prompt="Be a posh brittish butler," \
            "always answer politely and use titles such M'lord and Madam." \
            "Keep your answers concise and to the point and be helpful and service minded." \
        )
        
        
        self.result = None

    

    def chat (self, prompt: str) -> AgentRunResult:
        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history = message_history)

        return {"user": prompt, "bot": self.result.output}
    

if __name__ == "__main__": 
    bot = BruttlerBot()
    result = bot.chat("Hej svej")
    result = bot.chat("Hej svej igen")
    print(result)
    print(bot.result.all_messages)
    
