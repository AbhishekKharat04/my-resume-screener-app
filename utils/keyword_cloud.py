"""
utils/keyword_cloud.py
───────────────────────
Generates a visual keyword cloud from matched/missing skills.
Green = matched, Red = missing.
Returns a PNG image buffer for Streamlit display and PDF embedding.
"""

import io
from typing import List


def generate_keyword_cloud(
    matched_skills: List[str],
    missing_skills: List[str],
    matched_tools: List[str],
    missing_tools: List[str],
) -> io.BytesIO:
    """
    Generate a keyword cloud image showing matched (green) and missing (red) keywords.

    Returns:
        BytesIO buffer containing the PNG image.
    """
    from wordcloud import WordCloud
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Build word frequency dict — matched words get higher weight
    word_freq = {}
    for skill in matched_skills:
        word_freq[f"✓ {skill}"] = 3
    for tool in matched_tools:
        word_freq[f"✓ {tool}"] = 3
    for skill in missing_skills:
        word_freq[f"✗ {skill}"] = 2
    for tool in missing_tools:
        word_freq[f"✗ {tool}"] = 2

    if not word_freq:
        word_freq = {"No keywords found": 1}

    # Color function: green for matched (✓), red for missing (✗)
    def color_func(word, **kwargs):
        if word.startswith("✓"):
            return "#3fb950"  # green
        elif word.startswith("✗"):
            return "#f85149"  # red
        return "#8b949e"      # gray

    wc = WordCloud(
        width=800,
        height=400,
        background_color="#0d1117",
        color_func=color_func,
        max_words=50,
        prefer_horizontal=0.7,
        relative_scaling=0.5,
        margin=10,
    )

    wc.generate_from_frequencies(word_freq)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    fig.patch.set_facecolor("#0d1117")

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#3fb950", label="Matched Keywords"),
        Patch(facecolor="#f85149", label="Missing Keywords"),
    ]
    ax.legend(
        handles=legend_elements,
        loc="lower right",
        fontsize=9,
        facecolor="#161b22",
        edgecolor="#30363d",
        labelcolor="#e6edf3",
    )

    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=150, facecolor="#0d1117")
    plt.close(fig)
    buf.seek(0)
    return buf
