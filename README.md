🤖 100 Days of AI Agent Engineering
Welcome to the AI Agent Engineering learning repository! This repo is designed as a structured, day-by-day guide to help you build and understand Agentic AI from the ground up using locally hosted models.

📌 About This Repository
Day-by-Day Learning Path: Structured content progressing step-by-step from foundational concepts to advanced agent architectures.

Daily Notes: Each directory includes dedicated notes explaining the core concepts, goals, and hands-on exercises for that day.

100% Local Execution: Powered by Ollama to run light, capable LLMs directly on your machine without external API fees.

⚙️ Prerequisites & Setup
Before getting started, make sure you have python, Ollama installed on your system (Windows or macOS).

1. Install & Run the Model
Open your terminal and run the following commands to pull and start the model:

Bash
# Pull the Qwen model
ollama pull qwen3:4b

# Run the model locally
ollama run qwen3:4b
2. Environment Configuration
Create a .env file in the project root directory and add the following configuration:

Code snippet
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3:4b

🚀 Getting Started
Clone the repository:

Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
