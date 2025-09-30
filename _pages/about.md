---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am Zhitian Hou(侯智天), a third-year Master's student in Computer Technology at **[SYSU](https://www.sysu.edu.cn/sysuen/)**, advised by **[Prof. Kun Zeng](https://cse.sysu.edu.cn/teacher/ZengKun)**. I am currently an intern at **[Infix.ai](https://infix-ai.com/)**, under the supervision of **[Prof. Hongxia Yang](https://www4.comp.polyu.edu.hk/~hongxyang/)**. Prior to this, I received my Bachelor's degree in 2023 from SCNU, where I studied in the **[TAM Lab](https://tony-hao.github.io/TAMLab/)** under the supervision of **[Prof. Tianyong Hao](https://www.scholat.com/haoty.en)**. 
My current research interests lie primarily in **Natural Language Processing (NLP)**, **Large Language Models (LLMs)**, and **Medical MLLMs**, with previous research experience in **Legal AI**.


# 🔥 News
- *2025.09*: &nbsp;🎉🎉 Our paper "InfiMed-Foundation: Pioneering Advanced Multimodal Medical Models with Compute-Efficient Pre-Training and Multi-Stage Fine-Tuning" has been published on [arXiv](https://arxiv.org/abs/2509.22261).
- *2025.09*: &nbsp;🎉🎉 Our paper "InfiMed: Low-Resource Medical MLLMs with Advancing Understanding and Reasoning" has been published on [arXiv](https://arxiv.org/abs/2505.23867).
- *2025.09*: &nbsp;🎉🎉 Our paper "Large Language Models Meet Legal Artificial Intelligence: A Survey" has been published on [arXiv](https://arxiv.org/abs/2509.09969).
- *2025.07*: &nbsp;🎉🎉 Our paper "QCSH: Quantization Controlled Semantic Hashing for Effective Similar Text Search" has been accepted to **IEEE SMC Conference 2025**. 
- *2025.04*: &nbsp;🎉🎉 Our paper "KnowJudge: A Knowledge-Driven Framework for Legal Judgment Prediction" has been accepted to **CogSci 2025**. 
- *2022.10*: &nbsp;🎉🎉 Our paper "Homogeneous ensemble models for predicting infection levels and mortality of COVID-19 patients: Evidence from China" has been accepted to **Digital Health**. 

# 📝 Publications 


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2025</div><img src='images/InfiMed-Foundation.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

InfiMed-Foundation: Pioneering Advanced Multimodal Medical Models with Compute-Efficient Pre-Training and Multi-Stage Fine-Tuning

Guanghao Zhu, **Zhitian Hou**, Zeyu Liu, Zhijie Sang, Congkai Xie, Hongxia Yang

[![**HF**](https://img.shields.io/badge/HuggingFace-InfiMed--Foundation--4B-blue?logo=huggingface&logoColor=yellow&labelColor=FFEB66)](https://huggingface.co/InfiX-ai/InfiMed-Foundation-4B)
[![](https://img.shields.io/badge/InfiMed--Foundation-Paper-red?labelColor=blue)](https://arxiv.org/pdf/2509.22261) <strong><span class='show_paper_citations' data='ma9gcQsAAAAJ:UeHWp8X0CEIC'></span></strong>

- Multimodal large language models (MLLMs) have shown remarkable potential in various domains, yet their application in the medical field is hindered by several challenges. General-purpose MLLMs often lack the specialized knowledge required for medical tasks, leading to uncertain or hallucinatory responses. Knowledge distillation from advanced models struggles to capture domain-specific expertise in radiology and pharmacology. Additionally, the computational cost of continual pretraining with large-scale medical data poses significant efficiency challenges ...

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2025</div><img src='images/Infi-Med.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

InfiMed: Low-Resource Medical MLLMs with Advancing Understanding and Reasoning

Zeyu Liu$^\*$, **Zhitian Hou$^\*$**, Guanghao Zhu, Zhijie Sang, Congkai Xie, Hongxia Yang

[![**HF**](https://img.shields.io/badge/HuggingFace-InfiMed--RL--3B-blue?logo=huggingface&logoColor=yellow&labelColor=FFEB66)](https://huggingface.co/InfiX-ai/InfiMed-RL-3B)
[![](https://img.shields.io/badge/InfiMed--RL-Paper-red?labelColor=blue)](https://arxiv.org/pdf/2505.23867) <strong><span class='show_paper_citations' data='ma9gcQsAAAAJ:UeHWp8X0CEIC'></span></strong>

- In this work, we introduce the InfiMed-Series models, including InfiMed-SFT-3B and InfiMed-RL-3B, a set of multimodal large language models (MLLMs) specialized for medical tasks.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2025</div><img src='images/LLM4LegalAI.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Large Language Models Meet Legal Artificial Intelligence: A Survey

**Zhitian Hou**, Zihan Ye, Nanli Zeng, Tianyong Hao, Kun Zeng

<!-- [**Code**](https://github.com/ZhitianHou/LLMs4LegalAI)  -->
[![](https://img.shields.io/github/stars/ZhitianHou/LLMs4LegalAI?style=social)](https://github.com/ZhitianHou/LLMs4LegalAI)
[![](https://img.shields.io/badge/LLM4LegalAI--Survey-Paper-red?labelColor=blue)](https://arxiv.org/pdf/2509.09969) <strong><span class='show_paper_citations' data='ma9gcQsAAAAJ:zYLM7Y9cAGgC'></span></strong>


- This paper provides a comprehensive review of 16 legal LLMs series and 47 LLM-based frameworks for legal tasks, and also gather 15 benchmarks and 29 datasets to evaluate different legal capabilities. Additionally, we analyse the challenges and discuss future directions for LLMbased approaches in the legal domain. We hope this paper provides a systematic introduction for beginners and encourages future research in this field.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE SMC Conference 2025</div><img src='images/QCSH.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

QCSH: Quantization Controlled Semantic Hashing for Effective Similar Text Search

Zihan Ye, **Zhitian Hou**, Ge Lin, Kun Zeng

- We propose an unsupervised novel semantic text hashing framework, Quantization Controlled Semantic Hashing (QCSH), which enhances feature representation while refines the binarization process.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CogSci 2025</div><img src='images/KnowJudge.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

KnowJudge: A Knowledge-Driven Framework for Legal Judgment Prediction

**Zhitian Hou**, Jinlin Li, Ge Lin, Kun Zeng

<!-- [**Code**](https://github.com/ZhitianHou/KnowJudge)  -->
[![](https://img.shields.io/github/stars/ZhitianHou/KnowJudge?style=social)](https://github.com/ZhitianHou/KnowJudge) 
[![](https://img.shields.io/badge/KnowJudge-Paper-red?labelColor=blue)](https://escholarship.org/uc/item/28w694zd) <strong><span class='show_paper_citations' data='ma9gcQsAAAAJ:IjCSPb-OGe4C'></span></strong>
- We proposed KnowJudge, a knowledge-driven cognitive simulation framework and introduces the Law Keyword Recognition (LKR) dataset. 
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Digital Health</div><img src='images/Homogeneous.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Homogeneous ensemble models for predicting infection levels and mortality of COVID-19 patients: Evidence from China

Jiafeng Wang$^\*$, Xianlong Zhou$^\*$, **Zhitian Hou$^\*$**, Xiaoya Xu, Yueyue Zhao, Shanshan Chen, Jun Zhang, Lina Shao, Rong Yan, Mingshan Wang, Minghua Ge, Tianyong Hao, Yuexing Tu, and Haijun Huang

[![](https://img.shields.io/badge/COVID--19--Analysis-Paper-red?labelColor=blue)](https://journals.sagepub.com/doi/epub/10.1177/20552076221133692) <strong><span class='show_paper_citations' data='ma9gcQsAAAAJ:qjMakFHDy7sC'></span></strong>
- We proposed two homogeneous ensemble models based on clinical features of COVID-19 patients for predicting infection levels and mortality.
</div>
</div>

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

# 🎖 Honors and Awards
- *2024.09* First-Grade Scholarship, SYSU 
- *2023.06* Outstanding Graduate, SCNU  
- *2023.06* 37 Interactive Entertainment Scholarship, 37 Interactive Entertainment
- *2023.04* First-Grade Scholarship, SCNU  
- *2022.10* "Intelligent Base" Future Star Scholarship，Ministry of Education & Huawei 
- *2021.04* First-Grade Scholarship, SCNU 
- *2021.04* Finalist (F Award), Mathematical Contest in Modeling (MCM), COMAP

# 📖 Educations
- *2023.09 - present*, Master, Computer Technology, School of Computer Science and Engineering, Sun Yat-sen University.
- *2019.09 - 2023.06*, Undergraduate, Artificial Intelligence, School of Computer Science, South China Normal University. 

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
- *2025.06 - present*, Research Intern, [Infix.ai](https://infix-ai.com/), Shenzhen.
- *2022.09 - 2023.06*, Research Intern, [TAM Lab](https://tony-hao.github.io/TAMLab/), Guangzhou.