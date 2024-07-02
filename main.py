from google.cloud import aiplatform

def generate_response(request):
    prompt = request.get_json().get('prompt', '')
    
    # Initialize Vertex AI
    aiplatform.init(project='your-project-id')
    
    # Get a prediction from the model
    model = aiplatform.Model('model-name')
    response = model.predict(prompt)
    
    return {'response': response}