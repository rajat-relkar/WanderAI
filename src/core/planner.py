from langchain_core.messages import AIMessage, HumanMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = [] # to store conversation history
        self.city = ""
        self.days = ""
        self.interests = [] 
        self.itineary = "" # to store output

        logger.info("Initialized Travel Planner Instance...")

    def set_city(self, city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city)) # city is human input
            logger.info("City set sucessfully...")
        except Exception as e:
            logger.error(f"Error while setting city : {e}")
            raise CustomException("Failed to set city", e)
        
    def set_days(self, days:str):
        try:
            self.days = days
            self.messages.append(HumanMessage(content=days)) # days is human input
            logger.info("Days set sucessfully...")
        except Exception as e:
            logger.error(f"Error while setting days : {e}")
            raise CustomException("Failed to set days", e)
        
    def set_interests(self, interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests set sucessfully...")
        except Exception as e:
            logger.error(f"Error while setting Interests : {e}")
            raise CustomException("Failed to set Interests", e)      

    def create_itineary(self):
        try:
            logger.info(f"Generating a {self.days} day Itineary for {self.city} and for interests: {self.interests}")
            itineary = generate_itineary(self.city, self.days, self.interests)  
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))  
            logger.info("Itineary generated sucessfully...")
            return itineary
        except Exception as e:
            logger.error(f"Error while generating itineary: {e}")
            raise CustomException("Failed to generate itineary", e)  
        
    
