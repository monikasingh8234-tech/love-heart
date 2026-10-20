import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Page settings
st.set_page_config(
    page_title="Your Love, Your Story ❤️",
    page_icon="💘",
    layout="centered"
)

# Page heading
st.title("❤️ Your Love, Your Story 💘")
st.write("Create your own beautiful love heart!")

# Select relationship status
status = st.radio(
    "Are you Single or Mingle?",
    ["Single", "Mingle"],
    horizontal=True
)

# Name inputs
if status == "Single":
    name = st.text_input("Enter your name")
    partner = ""

else:
    partner = st.text_input("Partner's name")
    name = st.text_input("Your name")

# Generate button
if st.button("Create My Love Heart 💘", use_container_width=True):

    if not name.strip():
        st.warning("Please enter your name!")

    elif status == "Mingle" and not partner.strip():
        st.warning("Please enter your partner's name!")

    else:
        # Heart shape
        t = np.linspace(0, 2 * np.pi, 1000)

        x = 16 * np.sin(t) ** 3
        y = (
            13 * np.cos(t)
            - 5 * np.cos(2 * t)
            - 2 * np.cos(3 * t)
            - np.cos(4 * t)
        )

        # Create figure
        fig, ax = plt.subplots(figsize=(10, 9))

        fig.patch.set_facecolor("#fff5f7")
        ax.set_facecolor("#fff5f7")

        # Draw red heart
        ax.fill(x, y, color="#ff1744", zorder=1)
        ax.plot(x, y, color="#e60026", linewidth=2, zorder=2)

        if status == "Single":

            # Single design
            ax.text(
                0, 0, name.strip(),
                color="white",
                fontsize=18,
                fontweight="bold",
                ha="center",
                va="center",
                zorder=5
            )

        else:

            # Golden Cupid arrow across the heart
            arrow = FancyArrowPatch(
                (-17, -9),
                (17, 9),
                arrowstyle="-|>",
                mutation_scale=35,
                linewidth=4,
                color="#FFD700",
                zorder=5,
                clip_on=False
            )

            ax.add_patch(arrow)

            # Golden highlight on the arrow shaft
            ax.plot(
                [-16, 15],
                [-8.5, 8],
                color="#FFF0A0",
                linewidth=1,
                zorder=6,
                clip_on=False
            )

            # Partner name near the arrow tail
            ax.text(
                -13, -7.5, partner.strip(),
                color="black",
                fontsize=13,
                fontweight="bold",
                ha="center",
                va="center",
                rotation=28,
                zorder=7
            )

            # Your name near the arrow head
            ax.text(
                12, 7.2, name.strip(),
                color="black",
                fontsize=13,
                fontweight="bold",
                ha="center",
                va="center",
                rotation=28,
                zorder=7
            )

            # Golden heart accent
            ax.text(
                0, 0, "♥",
                color="#FFD700",
                fontsize=20,
                ha="center",
                va="center",
                zorder=7
            )

        # Title
        ax.set_title(
            "Your Love, Your Story ❤️",
            fontsize=18,
            color="#e91e63",
            pad=15
        )

        # Keep complete heart and arrow visible
        ax.set_aspect("equal")
        ax.set_xlim(-22, 22)
        ax.set_ylim(-18, 18)
        ax.axis("off")

        plt.tight_layout()

        # Display heart on the website
        st.pyplot(fig, use_container_width=True)

        # Release Matplotlib figure
        plt.close(fig)

        st.success("Your love heart is ready! 💌")

else:
    st.info("Enter your name and click the button to create your heart.")
