from dotenv import load_dotenv
load_dotenv()

from scripts.question_answering_on_pdf.intentservice import IntentService
from scripts.question_answering_on_pdf.responseservice import ResponseService
from scripts.question_answering_on_pdf.dataservice import DataService

# Example pdf
pdf = 'data/pdf-example.pdf'

data_service = DataService()

# Drop all data from redis if needed
data_service.drop_redis_data()

# Load data from pdf to redis
data = data_service.pdf_to_embeddings(pdf)

data_service.load_data_to_redis(data)

intent_service = IntentService()
response_service = ResponseService()

# Question 
question = "Can you explain to me the summary of the paper?"
# Get the intent
intents = intent_service.get_intent(question)
# Get the facts
facts = data_service.search_redis(intents)
# Get the answer
answer = response_service.generate_response(facts, question)
print(answer)