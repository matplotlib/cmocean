import cmocean
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 3))
ax = fig.add_subplot(1, 2, 1)
cmocean.plots.test(cmocean.cm.gray, ax=ax)
ax = fig.add_subplot(1, 2, 2)
cmocean.plots.test(cmocean.cm.gray_r, ax=ax)
fig.tight_layout()