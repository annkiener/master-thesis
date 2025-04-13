import pandas as pd
import ace_tools

import ace_tools as tools

# Create a DataFrame containing the methodology details of the reviewed studies
data = {
    "Authors (Year)": [
        "Skoy et al. (2016)", "Zare-Bidaki et al. (2022)", "Chaffin et al. (2013)",
        "Silverstein et al. (2021)", "Van Ommen et al. (2019)", "Yoo et al. (2020)",
        "Lee et al. (2020)", "Kuhail et al. (2022)", "Marques et al. (2022)",
        "Silva et al. (2017)", "Krogmeier et al. (2024)", "Hsia et al. (2022)"
    ],
    "Technology Used": [
        "VR", "VR", "VR", "VR", "Survey (for visual symptoms)", "VR (360 video)", "VR (360 video)",
        "VR", "VR", "AR", "AR/MR", "VR + Speaker"
    ],
    "Target Group": [
        "Pharmacy Students", "Medical Students", "General Public", "General Public", "Patients with psychosis",
        "Nursing Students", "Nursing Students", "Medical Students", "General Public", "Medical Students",
        "Healthcare Students", "Pharmacy Students"
    ],
    "Study Design": [
        "Pre/Post Experimental", "Comparison with Patient Visit", "Exploratory", "Experimental (Survey/VR)", "Survey Study",
        "Usability Study", "Usability Study", "Controlled Trial", "Controlled Trial", "Pilot Study", "Qualitative Evaluation", "Mixed-methods"
    ],
    "Symptoms Simulated": [
        "Auditory Hallucinations", "Auditory + Delusions", "Auditory + Visual Hallucinations",
        "Visual Hallucinations", "Visual Hallucinations", "Multiple Symptoms", "Multiple Symptoms",
        "Auditory Hallucinations", "Auditory + Visual + Delusions", "Auditory + Visual", "Auditory + Visual + Delusions", "Auditory + Discussion"
    ],
    "Main Results": [
        "Increased empathy", "Greater empathy and stigma reduction than patient visits", "Increased understanding, potential distress",
        "Reduced stigma after simulation", "Detailed phenomenology for simulation design", "Realistic, immersive training experience",
        "Improved awareness, safe tool", "Increased empathy, strong emotional engagement", "Mixed physiological responses, high empathy",
        "High realism, some discomfort", "Empathy increase, realism praised", "Empathy increased more with combined speaker"
    ],
    "Year Published": [
        2016, 2022, 2013, 2021, 2019, 2020, 2020, 2022, 2022, 2017, 2024, 2022
    ]
}

df = pd.DataFrame(data)

# Display the table to the user
tools.display_dataframe_to_user(name="Immersive Schizophrenia Simulation Studies", dataframe=df)
