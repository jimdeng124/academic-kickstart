---
title: "Deep domain generalization-based indoor pedestrian identification using footstep-induced vibrations"
authors:
  - X. Xu
  - Ruipeng (Jim) Deng
  - G. Zhao
  - B. Zhang
  - C. Liu
author_notes:
  - "Equal contribution"
  - "Equal contribution"
  - ""
  - ""
  - ""
date: "2024-01-01T00:00:00Z"
doi: ""  # Add your DOI here if available

# Schedule page publish date (NOT publication's date).
publishDate: "2024-01-01T00:00:00Z"
# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Instrumentation and Measurement, 73*"
publication_short: ""

abstract: Pedestrian identification based on footstep-induced vibrations is a nonintrusive identification method requiring sparse sensor layout for biometrics in smart buildings. Affected by variations in environments, developing pedestrian identification algorithms across different scenarios is challenging. To enhance the reusability and transferability of identification, a deep domain generalization-based method combining time-frequency domain signal processing and deep learning is proposed. First, the collected signals are converted into time-frequency images through continuous wavelet transform (CWT) to focus on the changes in energy distribution. Second, a deep residual shrinkage network (DRSN) specially designed for noise component suppression is used as a backbone network to automatically extract features. Third, classification information inherently in a single domain and discriminative knowledge generated through multiple domains are learned as the internally invariant and mutually invariant features to provide domain invariance for the classifier in the domain-invariant feature exploration (DIFEX) model. The results of the experiments involving multiple influencing factors demonstrated the great generalization of the proposed method, which achieves consistent pedestrian identification performance with over 90% accuracy across various environments.

# Summary. An optional shortened abstract.
summary: The study introduces a deep‐learning framework that converts footstep‐induced vibration signals into continuous‑wavelet time‑frequency images and feeds them to a noise‑robust deep residual shrinkage network combined with a domain‑invariant feature exploration (DIFEX) module, enabling pedestrian identification that generalizes across different building environments. Experiments show the approach maintains over 90 % identification accuracy under multiple environmental variations, confirming its reusability and transferability.

#tags:
#- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://ieeexplore.ieee.org/document/10385181

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

