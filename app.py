import streamlit as st
import random
from datetime import date

# List of motivational quotes
quotes = [
    "🌟 Believe in yourself and you will be unstoppable!",
    "💡 The only way to do great work is to love what you do. – Steve Jobs",
    "🔥 Success is not in never falling, but in rising every time you fall.",
    "💪 You are stronger than you think. Keep pushing forward!",
    "✨ The best time to plant a tree was 20 years ago. The second-best time is now.",
    "🚀 Don't stop when you're tired. Stop when you're done.",
    "🛤️ Difficult roads often lead to beautiful destinations.",
    "🌈 Every storm runs out of rain. Keep going!",
    "💖 You are not your past. You are the choices you make today.",
    "🎯 Stay focused, stay humble, and chase your dreams!",
    "📖 Struggles make you stronger. Every failure is a lesson.",
    "🔝 Keep going! Your future self is watching and cheering for you.",
    "🌍 If you want to change the world, start by changing yourself.",
    "⏳ Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "🦋 Growth and comfort never coexist. Choose growth!",
    "🚧 The harder the battle, the sweeter the victory.",
    "🌱 Small daily improvements are the key to staggering long-term results.",
    "🎵 One day, all the pain will make sense. Trust the process.",
    "🔥 Be so good they can't ignore you!",
    "📢 Your voice matters. Your dreams matter. Keep fighting for them!",
    "🔄 Success is a journey, not a destination. Enjoy the ride!",
    "💎 Hard times create strong people. Keep shining!",
    "🌞 No matter how dark it gets, the sun will rise again.",
    "✨ You were born to stand out. Don't try to fit in!",
    "🔑 Action is the key to all success. Stop overthinking and start doing!"
]

# Function
def quote_for_the_day():
    today = date.today()
    quote_index = today.day % len(quotes)  # Rotate quotes daily
    return quotes[quote_index]

def main():
    st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

    # Initialize session state for progress history
    if "progress_history" not in st.session_state:
        st.session_state.progress_history = []

    # Title
    st.title("🌱 Growth Mindset Challenge")
    st.subheader("Develop a mindset that fosters learning and growth!")

    # Display a new motivational quote daily
    st.write("### 🌟 Today's Motivation")
    st.success(quote_for_the_day())

    # User input for tracking progress
    st.write("### 📖 Track Your Daily Growth")
    daily_growth = st.text_area("What did you learn today?", "")

    if st.button("Save My Progress"):
        if daily_growth.strip():
            st.session_state.progress_history.append(daily_growth)
            st.success("✅ Your progress has been saved!")
        else:
            st.warning("⚠ Please write something before saving.")

    # Display progress history
    st.write("### ⏳ Your Progress History")
    if st.session_state.progress_history:
        for i, entry in enumerate(st.session_state.progress_history, 1):
            st.info(f"**{i}.** {entry}")
    else:
        st.write("No progress recorded yet.")

    # Footer
    st.markdown("---")
    st.markdown("💡 keep learning, keep growing! 🚀")

if __name__ == "__main__":
    main()
