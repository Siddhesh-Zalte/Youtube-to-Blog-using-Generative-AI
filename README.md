# 📹✍️ YouTube Blog Writer using CrewAI + Generative AI

A CrewAI-based application that **automatically writes blog posts** based on the content of a **YouTube channel**. Just provide the channel link — our intelligent agents do the rest!

---

## 🚀 Features

- 🔗 **YouTube Channel Input**  
  Provide a YouTube channel URL to get started.

- 🧠 **Agent-Based Architecture (CrewAI)**  
  - **Research Agent** – Extracts and analyzes content, trends, and tone from the YouTube channel.
  - **Writing Agent** – Crafts a coherent, engaging, and structured blog post using the analyzed data.

- ✨ **Generative AI-Powered Writing**  
  Creates human-like, SEO-optimized blog content using models like **Google Gemini** or **OpenAI GPT**.

- 🔍 **Video Analysis & Topic Detection**  
  Identifies recurring themes, audience focus, and highlights from the channel.

- 📝 **Ready-to-Publish Blog Output**  
  Clean and professional blog format ready for direct use in publications or websites.

---

## 🛠️ Tech Stack

- [CrewAI](https://docs.crewai.com/)
- [Google Gemini](https://ai.google.dev/gemini-api/docs) or [OpenAI GPT](https://platform.openai.com/)
- [YouTube Data API](https://developers.google.com/youtube/v3) *(optional but recommended)*
- [Serper.dev](https://serper.dev/) *(for search and metadata)*
- Python 3.9+

---

## 📂 How It Works

1. **Input**: User provides a YouTube channel URL.
2. **Content Analysis**:  
   - Research agent fetches and summarizes content.
   - Identifies video topics, tone, posting trends, and audience appeal.
3. **Blog Generation**:  
   - Writing agent uses the processed data to write a blog.
4. **Output**: A complete, structured blog post (~500-1000 words).

---

## 🧪 Example

**Input**:  
`https://www.youtube.com/c/YourFavoriteCreator`

**Output (blog snippet)**:
> "Exploring Creativity with CreatorName: From DIY Masterpieces to Audience Inspiration"  
> CreatorName’s YouTube channel is a vibrant showcase of hands-on creativity, DIY tutorials, and authentic engagement with a growing global audience...

---

## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Siddhesh-Zalte/Youtube-to-Blog-using-Generative-AI/
   cd Youtube-to-Blog-using-Generative-AI
