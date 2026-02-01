import streamlit as st
from vector import retriever
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# ----------------------------
# Session State Defaults
# ----------------------------
if "cancel" not in st.session_state:
    st.session_state.cancel = False

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "running" not in st.session_state:
    st.session_state.running = False


# ----------------------------
# Model
# ----------------------------
model = OllamaLLM(
    model="phi",
    temperature=0.0,
    num_predict=300,
)

# ----------------------------
# Prompt
# ----------------------------
template = """
You are a professional Tavel Agency guide offering different tours and packages.

You MUST answer ONLY using the information provided in the context.
If the context contains a table, read rows and columns carefully.
Answer using exact values from the table.
DO NOT:
- invent new people
- invent scenarios
- create stories
- add logic puzzles
- introduce new questions
- mention tours not in the context
- speculate

If the context contains a table or structured data,
you MUST convert it into a clear day-wise list.
Do not summarize. Do not skip days.
if there is Cost Breakup Table, convert it into Compeonent, Cost & Currency line by line.
if Hotel Options Table is there it will have Hotel Name, City, Star Rating, Room Type, Meal Plan, Guest Rating
understand each data line by line clearly. if user asking trip details about any location user Region filed in document.
Always provide the data based on Single trip do not mix different trips into one.
If the answer is not present in the context, reply exactly:
"I don't know based on the provide data."
Stop immediately after answering the question.
Be to the point Specific to answer no need to provide extra information.

Context:
{material}

User Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


# ----------------------------
# UI
# ----------------------------
st.set_page_config(page_title="Travel RAG Bot", layout="centered")
st.title("🌍 Global Horizons Travel Assistant")

# Input row
col1, col2, col3 = st.columns([5, 1.2, 1.2])

with col1:
    query = st.text_input(
        label="",
        label_visibility="collapsed",
        placeholder = "How can i help you with trip details?",
        key="query",
        disabled=st.session_state.running,
    )


with col2:
    ask_btn = st.button("▶ Ask", disabled=st.session_state.running, use_container_width=True)

with col3:
    reset_btn = st.button("⏹ Reset",
    use_container_width=True
    )


# ----------------------------
# Reset button logic
# ----------------------------
if reset_btn:
    st.session_state.cancel = True
    st.session_state.running = False
    st.session_state.answer = ""
    st.rerun()


# ----------------------------
# Ask button logic
# ----------------------------
if ask_btn and query:

    st.session_state.cancel = False
    st.session_state.running = True
    st.session_state.answer = ""

    placeholder = st.empty()

    with st.spinner("Searching brochure and generating answer..."):

        docs = retriever.invoke(query)

        if not docs:
            st.session_state.answer = "❌ No relevant information found."
        else:
            material = "\n\n".join(d.page_content for d in docs)

            # --- STREAM OUTPUT MANUALLY ---
            for chunk in model.stream(
                prompt.format(material=material, question=query)
            ):

                # STOP if reset pressed
                if st.session_state.cancel:
                    st.session_state.answer += "\n\n⏹ Generation stopped."
                    break

                st.session_state.answer += chunk
                placeholder.markdown(st.session_state.answer)

    st.session_state.running = False


# ----------------------------
# Display Final Answer
# ----------------------------
if st.session_state.answer:
    st.subheader("Answer")
    st.markdown(st.session_state.answer)


# ----------------------------
# Retrieved Context Viewer
# ----------------------------
if st.session_state.answer and not st.session_state.running:

    with st.expander("📄 Retrieved Context"):
        docs = retriever.invoke(query)
        for i, d in enumerate(docs, 1):
            st.markdown(f"**Chunk {i} — Page:** {d.metadata.get('page_number', '?')}")
            st.write(d.page_content[:600])
