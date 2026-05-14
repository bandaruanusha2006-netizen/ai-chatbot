def ai_response(message):

    message = message.lower()

    # Greetings
    if "hello" in message or "hi" in message:
        return "Hello 👋 Welcome to AI Assistant"

    # Thank you
    elif "thank you" in message or "thanks" in message:
        return "You're welcome 😊 Happy Learning 🚀"

    # Python
    elif "python" in message:
        return "Python is powerful for AI, Web Development, Automation, and Machine Learning 🚀"

    # AI
    elif "ai" in message:
        return "Artificial Intelligence is changing the future 🤖"

    # Roadmap
    elif "roadmap" in message or "road map" in message:

        return """
🚀 Complete Python Learning Roadmap

1️⃣ Python Basics
- Variables
- Data Types
- Input/Output
- Operators
- Conditions
- Loops
- Functions

2️⃣ Intermediate Python
- OOPs
- File Handling
- Modules
- Exception Handling

3️⃣ Advanced Python
- Decorators
- Generators
- APIs
- Multithreading

4️⃣ Libraries
- NumPy
- Pandas
- Matplotlib
- Seaborn

5️⃣ Web Development
- Flask
- Django
- REST APIs

6️⃣ Database
- SQLite
- MySQL
- MongoDB

7️⃣ Machine Learning
- Scikit-Learn
- TensorFlow
- PyTorch

8️⃣ Build Projects
- AI Chatbot
- Face Recognition
- Web Apps
- AI Assistants

9️⃣ Deployment
- GitHub
- Render
- Vercel

🔟 Learn DSA + Problem Solving
- Arrays
- Strings
- Linked Lists
- Recursion
"""

    # Machine Learning
    elif "machine learning" in message:
        return "Machine Learning helps computers learn from data 📊"

    # Bye
    elif "bye" in message:
        return "Goodbye 👋 Have a great day"

    # Default
    else:
        return "Sorry 😅 I am still learning. Please ask another question."