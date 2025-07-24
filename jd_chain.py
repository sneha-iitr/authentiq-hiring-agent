from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Load prompt template
with open("prompt_template.txt", "r") as f:
    prompt_text = f.read()

prompt = PromptTemplate.from_template(prompt_text)

# Create LLM chain
llm = ChatOpenAI(openai_api_key=api_key, model="gpt-4", temperature=0.7)
chain = LLMChain(llm=llm, prompt=prompt)

# Get input from user
job_input = {}
print("\n📝 Enter Job Details:\n")
job_input["title"] = input("Job Title: ")
job_input["skills"] = input("Key Skills (comma separated): ")
job_input["experience"] = input("Years of Experience Required: ")
job_input["location"] = input("Location: ")
job_input["company"] = input("Company Description: ")
job_input["salary"] = input("Salary Range: ")

# Loop until approved
approved = False
while not approved:
    print("\n📄 Generating Job Description...\n")
    jd = chain.run(job_input)
    print(jd)

    feedback = input("\n✅ Approve JD? Type 'yes' to approve, or enter feedback to improve: ")

    if feedback.strip().lower() == "yes":
        approved = True
        print("\n🎉 JD Approved and Ready for Posting!\n")
    else:
        print("\n🔁 Updating JD with your feedback...\n")
        job_input["company"] += f"\n\nNote from hiring manager: {feedback}"
