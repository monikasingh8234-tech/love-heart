
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from datetime import date, datetime

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Love Story | Compatibility 💗",
    page_icon="💘",
    layout="centered"
)


st.markdown("""
<style>
/* Main page */
.stApp {
    background: linear-gradient(180deg, #fff0f5 0%, #fffaf7 100%);
    color: #35202a !important;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stAppViewContainer"] {
    background: transparent;
}

/* Force readable text throughout the app */
.stApp, .stApp p, .stApp label,
.stApp span, .stApp li,
.stApp [data-testid="stMarkdownContainer"] {
    color: #35202a;
}

h1, h2, h3, h4,
.stApp h1, .stApp h2, .stApp h3 {
    color: #a81750 !important;
    font-weight: 800 !important;
}

.stCaption, [data-testid="stCaptionContainer"] {
    color: #75475a !important;
}

/* Input fields */
.stApp input,
.stApp textarea,
.stApp [data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #35202a !important;
    border: 1px solid #efb6cc !important;
    border-radius: 12px !important;
}

.stApp input::placeholder,
.stApp textarea::placeholder {
    color: #866b78 !important;
    opacity: 1 !important;
}

/* Radio buttons and checkboxes */
.stApp [data-testid="stRadio"] label,
.stApp [data-testid="stCheckbox"] label {
    color: #35202a !important;
}

/* Cards and metrics */
[data-testid="stMetric"] {
    background: #ffffff !important;
    border: 1px solid #f2c1d3;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 5px 18px rgba(190, 55, 105, 0.08);
}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: #a81750 !important;
}

/* Buttons */
.stApp div.stButton > button,
.stApp div.stDownloadButton > button {
    background: linear-gradient(90deg, #ed4784, #d91d61) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    min-height: 48px;
    font-weight: 700 !important;
}

.stApp div.stButton > button p,
.stApp div.stDownloadButton > button p {
    color: #ffffff !important;
}

/* Progress bar */
.stProgress > div > div > div {
    background-color: #e63375 !important;
}

/* Expanders */
[data-testid="stExpander"] {
    background: #ffffff;
    border: 1px solid #f0c0d2;
    border-radius: 14px;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 14px;
}

/* Mobile spacing */
.block-container {
    max-width: 900px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

@media (max-width: 600px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }

    h1 {
        font-size: 1.8rem !important;
    }

    h2 {
        font-size: 1.35rem !important;
    }

    [data-testid="stMetric"] {
        padding: 12px;
    }
}
</style>
""", unsafe_allow_html=True)


st.title("💗 Your Love, Your Story")
st.caption("Two hearts. One story. A little bit of magic. 🎀")

st.write(
    "Discover your fun compatibility score, compare your "
    "favourite things, and keep your special dates close to your heart."
)

# ---------------- OPTIONS ----------------
likes_options = [
    "Music", "Movies", "Travel", "Food", "Dancing",
    "Gaming", "Reading", "Photography", "Nature",
    "Shopping", "Cooking", "Fitness", "Pets",
    "Long conversations", "Surprises", "Quality time"
]

dislikes_options = [
    "Lying", "Ignoring messages", "Being late",
    "Loud places", "Crowds", "Arguments",
    "Possessiveness", "Last-minute plans",
    "Spicy food", "Waking up early", "Dishonesty",
    "Poor communication", "Cancelled plans"
]

communication_options = [
    "Talk things out calmly",
    "Need some time before talking",
    "Prefer writing my feelings",
    "Depends on the situation"
]

love_language_options = [
    "Quality time", "Words of affirmation",
    "Acts of service", "Gifts",
    "Physical affection"
]

weekend_options = [
    "A cozy day at home",
    "A romantic date outside",
    "An adventure or road trip",
    "Meeting friends",
    "Trying something new"
]

# ---------------- PERSONAL DETAILS ----------------
st.header("💌 01. Your Love Story")

status = st.radio(
    "Relationship status",
    ["Single 💖", "Mingle 💑"],
    horizontal=True
)

is_mingle = status == "Mingle 💑"

col1, col2 = st.columns(2)

with col1:
    your_name = st.text_input("Your name ✨", placeholder="Enter your name")
    your_birthday = st.date_input(
        "Your birthday 🎂",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today(),
        format="DD/MM/YYYY"
    )

with col2:
    if is_mingle:
        partner_name = st.text_input(
            "Partner's name 💕", placeholder="Their name"
        )
        partner_birthday = st.date_input(
            "Partner's birthday 🎂",
            value=date(2000, 6, 1),
            min_value=date(1900, 1, 1),
            max_value=date.today(),
            format="DD/MM/YYYY"
        )
    else:
        partner_name = ""
        partner_birthday = None
        st.info("Your perfect story starts with loving yourself. 💗")

anniversary = st.date_input(
    "Relationship anniversary 💍",
    value=None,
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="DD/MM/YYYY"
) if is_mingle else None

# ---------------- PREFERENCES ----------------
st.header("💞 02. Likes & Dislikes")

st.write("Choose the things you love and the things you don't enjoy.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Your favourites 💗")
    your_likes = st.multiselect(
        "Things you like",
        likes_options,
        key="your_likes"
    )

    st.subheader("Your dislikes 🙈")
    your_dislikes = st.multiselect(
        "Things you dislike",
        dislikes_options,
        key="your_dislikes"
    )

with col2:
    if is_mingle:
        st.subheader("Their favourites 💕")
        partner_likes = st.multiselect(
            "Things your partner likes",
            likes_options,
            key="partner_likes"
        )

        st.subheader("Their dislikes 🙈")
        partner_dislikes = st.multiselect(
            "Things your partner dislikes",
            dislikes_options,
            key="partner_dislikes"
        )
    else:
        partner_likes = []
        partner_dislikes = []
        st.info("Add a partner to compare your preferences.")

# ---------------- LOVE QUIZ ----------------
st.header("💘 03. The Couple Quiz")

st.caption(
    "Answer honestly. Similar answers can help you understand "
    "each other, but different answers aren't necessarily bad."
)

your_communication = st.selectbox(
    "How do you handle disagreements?",
    communication_options,
    key="your_communication"
)

your_love_language = st.selectbox(
    "What makes you feel loved?",
    love_language_options,
    key="your_love_language"
)

your_weekend = st.selectbox(
    "Your ideal weekend?",
    weekend_options,
    key="your_weekend"
)

if is_mingle:
    partner_communication = st.selectbox(
        "How does your partner handle disagreements?",
        communication_options,
        key="partner_communication"
    )

    partner_love_language = st.selectbox(
        "What makes your partner feel loved?",
        love_language_options,
        key="partner_love_language"
    )

    partner_weekend = st.selectbox(
        "Your partner's ideal weekend?",
        weekend_options,
        key="partner_weekend"
    )
else:
    partner_communication = ""
    partner_love_language = ""
    partner_weekend = ""

# ---------------- HELPERS ----------------
def next_birthday(birthday, today):
    upcoming = birthday.replace(year=today.year)

    if upcoming < today:
        upcoming = birthday.replace(year=today.year + 1)

    return upcoming


def days_until(event_date, today):
    return (event_date - today).days


def overlap_score(first, second):
    """Compare selected preferences symmetrically."""
    first = set(first)
    second = set(second)

    if not first and not second:
        return None

    union = first | second
    return len(first & second) / len(union) * 100


def compatibility_label(score):
    if score >= 90:
        return "Magical Connection ✨"
    elif score >= 75:
        return "Beautiful Bond 💖"
    elif score >= 60:
        return "Growing Together 🌷"
    elif score >= 40:
        return "A Journey of Discovery 💌"
    return "Room to Understand Each Other 🌱"


def draw_heart(your_name, partner_name, score, single=False):
    t = np.linspace(0, 2 * np.pi, 1000)

    x = 16 * np.sin(t) ** 3
    y = (
        13 * np.cos(t)
        - 5 * np.cos(2 * t)
        - 2 * np.cos(3 * t)
        - np.cos(4 * t)
    )

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("#fff5f7")
    ax.set_facecolor("#fff5f7")

    ax.fill(x, y, color="#ff477e", zorder=1)
    ax.plot(x, y, color="#e60050", linewidth=2, zorder=2)

    if single:
        ax.text(
            0, 1, your_name,
            color="white", fontsize=18, fontweight="bold",
            ha="center", va="center", zorder=5
        )
        ax.text(
            0, -3, "SELF LOVE ♥",
            color="#ffe5ec", fontsize=11, fontweight="bold",
            ha="center", va="center", zorder=5
        )
    else:
        arrow = FancyArrowPatch(
            (-14, -7.5), (14, 7.5),
            arrowstyle="-|>", mutation_scale=28,
            linewidth=3, color="#ffd700", zorder=5
        )
        ax.add_patch(arrow)

        ax.text(
            -7, -3.5, partner_name,
            color="white", fontsize=11, fontweight="bold",
            ha="center", va="center", zorder=6
        )
        ax.text(
            7, 3.5, your_name,
            color="white", fontsize=11, fontweight="bold",
            ha="center", va="center", zorder=6
        )
        ax.text(
            0, 0, "♥",
            color="#ffd700", fontsize=23,
            ha="center", va="center", zorder=7
        )

    ax.set_title(
        "Your Love, Your Story ❤️",
        fontsize=18, color="#d6336c", pad=15
    )
    ax.set_aspect("equal")
    ax.set_xlim(-21, 21)
    ax.set_ylim(-17, 17)
    ax.axis("off")
    plt.tight_layout()

    return fig


# ---------------- CALCULATE ----------------
st.divider()

if st.button("Create Our Love Story 💘", use_container_width=True):

    if not your_name.strip():
        st.warning("Please enter your name first! 💗")

    elif is_mingle and not partner_name.strip():
        st.warning("Please enter your partner's name! 💌")

    elif is_mingle and your_name.strip().casefold() == partner_name.strip().casefold():
        st.warning("Enter two different names to compare your love story.")

    else:
        st.session_state["love_result"] = True

if st.session_state.get("love_result", False):

    # Recheck names in case inputs changed
    if not your_name.strip() or (is_mingle and not partner_name.strip()):
        st.session_state["love_result"] = False
        st.info("Please complete the required name fields and generate again.")
        st.stop()

    st.divider()
    st.header("🌹 Your Results")

    if not is_mingle:
        score = None
        st.subheader(f"A little love for {your_name.strip()} 💗")
        st.write(
            "Your story matters too. Celebrate your interests, "
            "dreams, boundaries and the person you are becoming."
        )
    else:
        # Shared likes
        likes_score = overlap_score(your_likes, partner_likes)

        # Shared dislikes are compared separately.
        dislikes_score = overlap_score(your_dislikes, partner_dislikes)

        # Conflicts: one person's like is the other's dislike.
        conflicts = (
            (set(your_likes) & set(partner_dislikes))
            | (set(partner_likes) & set(your_dislikes))
        )

        # Quiz similarity: exact matches earn full points.
        quiz_pairs = [
            (your_communication, partner_communication),
            (your_love_language, partner_love_language),
            (your_weekend, partner_weekend)
        ]
        quiz_score = (
            sum(a == b for a, b in quiz_pairs) / len(quiz_pairs) * 100
        )

        # Ignore preference categories if both people left them empty.
        components = [
            (likes_score, 0.40),
            (dislikes_score, 0.20),
            (quiz_score, 0.40)
        ]

        available = [
            (value, weight)
            for value, weight in components
            if value is not None
        ]

        score = round(
            sum(value * weight for value, weight in available)
            / sum(weight for _, weight in available)
        )

        st.subheader(f"{partner_name.strip()} 💞 {your_name.strip()}")
        st.metric("Your Fun Compatibility Score", f"{score}%")
        st.progress(score / 100)
        st.markdown(f"### {compatibility_label(score)}")

        st.caption(
            "This is a playful score based on your selected answers, "
            "not a scientific measurement or prediction of relationship success."
        )

        st.subheader("💖 Compatibility breakdown")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Shared likes",
            f"{round(likes_score)}%" if likes_score is not None else "N/A"
        )
        c2.metric(
            "Shared dislikes",
            f"{round(dislikes_score)}%" if dislikes_score is not None else "N/A"
        )
        c3.metric("Quiz match", f"{round(quiz_score)}%")

        st.subheader("💕 Things you have in common")

        common_likes = sorted(set(your_likes) & set(partner_likes))
        common_dislikes = sorted(set(your_dislikes) & set(partner_dislikes))

        if common_likes:
            st.write("**You both love:** " + ", ".join(common_likes))
        else:
            st.write("Your favourite things differ. Discover something new together!")

        if common_dislikes:
            st.write("**You both dislike:** " + ", ".join(common_dislikes))

        if conflicts:
            st.write(
                "**Different preferences:** " + ", ".join(sorted(conflicts))
            )
            st.caption(
                "Different preferences are normal. Talk about them with respect."
            )

        st.subheader("💌 Your quiz comparison")

        quiz_labels = [
            "Communication style",
            "Love language",
            "Ideal weekend"
        ]

        for label, (first, second) in zip(quiz_labels, quiz_pairs):
            with st.expander(label):
                st.write(f"**{your_name.strip()}:** {first}")
                st.write(f"**{partner_name.strip()}:** {second}")

                if first == second:
                    st.success("You selected the same answer! 💗")
                else:
                    st.info("A chance to understand each other better. 🌷")

    # Heart graphic
    st.subheader("💘 Your Heart Design")

    fig = draw_heart(
        your_name.strip(),
        partner_name.strip(),
        score,
        single=not is_mingle
    )
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # ---------------- REMINDERS ----------------
    st.divider()
    st.header("🎂 Special Dates & Reminders")

    today = date.today()

    birthday1 = next_birthday(your_birthday, today)
    st.write(
        f"🎂 **{your_name.strip()}'s birthday:** "
        f"{your_birthday.strftime('%d %B')} "
        f"({days_until(birthday1, today)} days to go)"
    )

    if is_mingle:
        birthday2 = next_birthday(partner_birthday, today)
        st.write(
            f"🎂 **{partner_name.strip()}'s birthday:** "
            f"{partner_birthday.strftime('%d %B')} "
            f"({days_until(birthday2, today)} days to go)"
        )

        if anniversary:
            next_anniversary = anniversary.replace(year=today.year)
            if next_anniversary < today:
                next_anniversary = anniversary.replace(year=today.year + 1)

            st.write(
                f"💍 **Your anniversary:** "
                f"{anniversary.strftime('%d %B')} "
                f"({days_until(next_anniversary, today)} days to go)"
            )

    st.info(
        "Reminder note: These dates are displayed in this session. "
        "For automatic notifications when the app is closed, "
        "you will need a database and a scheduled email or notification service."
    )

    # ---------------- SHAREABLE SUMMARY ----------------
    st.divider()
    st.subheader("💌 Your Love Note")

    if is_mingle:
        summary = (
            f"💗 {partner_name.strip()} + {your_name.strip()} 💗\n\n"
            f"Our fun compatibility score: {score}%\n"
            f"{compatibility_label(score)}\n\n"
            f"Things we both love: {', '.join(common_likes) or 'Discovering new things'}\n\n"
            "Different hearts, one beautiful journey. ❤️"
        )
    else:
        summary = (
            f"💗 {your_name.strip()}'s Love Story 💗\n\n"
            "Self-love is the beginning of every beautiful story. ❤️"
        )

    st.text_area(
        "Copy your love note",
        value=summary,
        height=150
    )

    st.download_button(
        "Download Your Love Note 💌",
        data=summary,
        file_name="my_love_story.txt",
        mime="text/plain",
        use_container_width=True
    )

    if st.button("Start a New Love Story 🔄"):
        st.session_state["love_result"] = False
        st.rerun()

else:
    st.info(
        "Fill in your details and preferences, then click "
        "'Create Our Love Story' to see your results. 💕"
        )
                


            
