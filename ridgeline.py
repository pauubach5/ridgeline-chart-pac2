import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carreguem les dades de Spotify
df = pd.read_csv("spotify.csv")

# Preparem els colors i un gràfic per a cada gènere
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

palette = sns.color_palette("crest", n_colors=len(df['track_genre'].unique()))

g = sns.FacetGrid(df, row="track_genre", hue="track_genre", aspect=15, height=0.8, palette=palette)

# Dibuixem les distribucions de tempo i hi afegim una línia de contorn
g.map(sns.kdeplot, "tempo",
      bw_adjust=0.5, clip_on=False,
      fill=True, alpha=0.7, linewidth=1.5)

g.map(sns.kdeplot, "tempo", clip_on=False, color="w", lw=2, bw_adjust=0.5)

# Afegim el nom de cada gènere al seu gràfic
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, 0.2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes, size=12)

g.map(label, "tempo")

g.figure.subplots_adjust(hspace=-0.5)

g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)

plt.xlabel("Tempo (BPM)", fontsize=12, fontweight="bold")
plt.suptitle("Distribució del Tempo de Pistes per Gènere Musical (Ridgeline Plot)", y=0.98, fontsize=14, fontweight="bold")
plt.figtext(0.5, 0.02, "Font: Spotify Tracks Dataset (Anàlisi de densitat de tempo)", ha="center", fontsize=9, style="italic")

plt.tight_layout()

# Guardem el gràfic com a imatge
output_image_path = "spotify_ridgeline_plot.png"
plt.savefig(output_image_path, bbox_inches='tight')
print("Ridgeline plot generated successfully and saved as:", output_image_path)