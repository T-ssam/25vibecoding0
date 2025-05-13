import streamlit as st
import streamlit as st

# 🧠 MBTI별 직업 추천 데이터
mbti_careers = {
    "INTJ": ["💻 데이터 과학자", "📈 전략 컨설턴트", "🧠 인공지능 연구원", "🔬 기술 분석가", "📚 학술 작가"],
    "INTP": ["🧪 연구 과학자", "👨‍💻 개발자", "🧮 알고리즘 전문가", "📖 철학자", "💡 아이디어 디자이너"],
    "ENTJ": ["🏢 CEO", "📊 경영 컨설턴트", "🧭 프로젝트 매니저", "📈 투자 분석가", "👨‍🏫 기업 교육가"],
    "ENTP": ["🚀 스타트업 창업가", "🎙️ 방송 기획자", "🎮 UX/UI 디자이너", "📢 마케팅 전략가", "🎥 유튜버"],
    "INFJ": ["🧘 심리상담가", "📖 작가", "👩‍🏫 교사", "🌱 사회복지사", "🎨 콘텐츠 크리에이터"],
    "INFP": ["🎨 예술가", "📚 소설가", "🧠 상담심리사", "🌈 인권운동가", "💌 카피라이터"],
    "ENFJ": ["👩‍🏫 교육자", "🗣️ 커뮤니케이션 코치", "🎤 발표 전문가", "🧑‍🤝‍🧑 팀 리더", "📚 진로 지도사"],
    "ENFP": ["🌍 여행 콘텐츠 제작자", "📢 브랜드 기획자", "🎤 이벤트 진행자", "📸 콘텐츠 디자이너", "👫 청소년 멘토"],
    "ISTJ": ["📁 회계사", "🏛️ 공무원", "📋 품질 관리자", "📐 기술 엔지니어", "📊 통계 분석가"],
    "ISFJ": ["👩‍⚕️ 간호사", "📑 행정 사무원", "👨‍🏫 초등교사", "🎁 고객 서비스 담당", "🧵 패션 디자이너"],
    "ESTJ": ["💼 경영 관리자", "🔧 설비 기술자", "📈 세일즈 매니저", "🛠️ 프로젝트 관리자", "📊 재무 분석가"],
    "ESFJ": ["🧑‍🏫 학급담임", "💍 웨딩 플래너", "🧾 인사담당자", "🍽️ 식음료 매니저", "📋 상담 행정가"],
    "ISTP": ["🛠️ 기계 정비사", "🚗 자동차 전문가", "🔧 기술 연구원", "🎮 게임 개발자", "📸 포토그래퍼"],
    "ISFP": ["🎨 일러스트레이터", "🎶 음악가", "📷 포토 에디터", "🪡 패션 스타일리스트", "🌺 플로리스트"],
    "ESTP": ["🏎️ 레이서", "💼 비즈니스 개발자", "📢 영업 전문가", "🎬 광고 기획자", "🎮 스트리머"],
    "ESFP": ["🎤 MC/방송인", "🎭 배우", "📸 인플루언서", "🍳 요리사", "🎉 이벤트 플래너"]
}

# 🌟 페이지 설정
st.set_page_config(page_title="🌈 MBTI 진로 추천기", page_icon="🧭", layout="centered")

# ✨ 타이틀 영역
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='font-size: 3em; color: #6c5ce7;'>🌈 MBTI 기반 ✨ 진로 추천기 🎯</h1>
        <h3>당신의 성격 유형에 맞는 최고의 직업을 찾아드립니다 💼</h3>
    </div>
""", unsafe_allow_html=True)

# 🧭 MBTI 선택
st.markdown("### 👉 아래에서 당신의 MBTI 유형을 선택하세요!")
selected_mbti = st.selectbox("🔎 MBTI 유형 선택", list(mbti_careers.keys()))

# 🚀 추천 직업 표시
if selected_mbti:
    st.markdown(f"## 🎉 {selected_mbti} 유형에게 추천하는 직업 Top 5 🎯")
    st.markdown("---")

    jobs = mbti_careers[selected_mbti]
    for i, job in enumerate(jobs, 1):
        st.markdown(f"### {i}. {job}")

    st.success("✨ 다양한 직업을 탐색하고, 당신의 가능성을 넓혀보세요!")

# 🎁 하단 푸터
st.markdown("""
    <hr>
    <div style='text-align:center; font-size: 16px;'>
        📚 진로 교육 플랫폼 • MBTI Career Finder<br>
        Made with ❤️ by AI Assistant
    </div>
""", unsafe_allow_html=True)
