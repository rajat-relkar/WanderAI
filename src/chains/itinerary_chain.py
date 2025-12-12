from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.75,
)

itinerary_prompt = ChatPromptTemplate([
    (
        "system",
        "You are a professional travel assistant. Generate a travel itinerary for the user based on:\n"
        "- City: {city}\n"
        "- Duration: {days} days (can be 1 or multiple)\n"
        "- User interests: {interests}\n\n"
        "Instructions:\n"
        "- Provide a well-structured, easy-to-read itinerary.\n"
        "- For single-day itineraries, keep it concise and focus on key highlights.\n"
        "- For multi-day itineraries, break the plan day-by-day.\n"
        "- Use bullet points for activities, food recommendations, and ideal timings.\n"
        "- Ensure suggestions align with the user's interests."
    ),
    (
        "human",
        "Create my travel itinerary."
    )
])


def generate_itineary(city:str, days, interests:list[str]) -> str:
    response = llm.invoke(
        itinerary_prompt.format_messages(city=city, days=str(days), interests=', '.join(interests))
    )

    return response.content


