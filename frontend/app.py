import streamlit as st
import requests

st.set_page_config(page_title="FAANG ATS", layout="centered")

st.title("🚀 FAANG LEVEL AI RESUME ATS SYSTEM")

uploaded_file = st.file_uploader("Upload Resume (PDF)")
jd = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_file and jd:

        # Upload
        upload_res = requests.post(
            "http://127.0.0.1:8000/upload",
            files={"file": uploaded_file}
        )

        if upload_res.status_code == 200:

            data = upload_res.json()
            resume_text = data["resume_text"]

            # Score
            score_res = requests.post(
                "http://127.0.0.1:8000/match",
                json={
                    "resume_id": data["resume_id"],
                    "jd_text": jd
                }
            )

            if score_res.status_code == 200:

                result = score_res.json()

                st.success(f"Match Score: {result['match_score']}%")

                st.write("### Resume Skills")
                st.write(result["resume_skills"])

                st.write("### JD Skills")
                st.write(result["jd_skills"])

            else:
                st.error(score_res.text)

        else:
            st.error("Upload failed")

    else:
        st.warning("Upload resume + JD")