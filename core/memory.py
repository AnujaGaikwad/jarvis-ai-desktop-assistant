conversation_memory = []

def add_to_memory(role, text):
    conversation_memory.append({"role": role, "text": text})

    # Keep only last 6 interactions
    if len(conversation_memory) > 6:
        conversation_memory.pop(0)

def get_memory():
    context = ""
    for item in conversation_memory:
        context += f"{item['role']}: {item['text']}\n"
    return context
