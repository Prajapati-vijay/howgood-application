import hashlib
import hmac
import json
import requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

notes=f"Backend engineer with ~3.5 years of experience in Python, Django, and FastAPI, building scalable microservices and production APIs. Strong in async systems (Celery), performance optimization (40% improvement), and Docker/AWS-based deployments. Interested in system design, workflow orchestration, and LLM integrations."
payload = {
    "name": "Vijay Prajapati",
    "email": "vijayprajapati260263@gmail.com",
    "resume": "https://drive.google.com/uc?export=download&id=1urtcdYfaZugaYop3M3thslJh20qTZwgp",
    "location": "Noida, India",
    "linkedin": "https://www.linkedin.com/in/vijay-prajapati-60a3b5247/",
    "codeLink": "https://github.com/Prajapati-vijay/howgood-application",
    "yearsPython": 3,
    "yearsDjango": 3,
    "repos": "https://github.com/Prajapati-vijay",
    "notes": notes
}

body = json.dumps(payload)

signature = hmac.new(
    secret.encode(),
    body.encode(),
    hashlib.sha256
).hexdigest()

response = requests.post(
    endpoint,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-HMAC-Signature": signature
    }
)

print(response.status_code)
print(response.text)