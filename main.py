from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="phi", streaming=True)

template = """
You are a Tavel Agency Company offering different tours and packages.

You MUST answer ONLY using the information provided in the context.
If the context contains a table, read rows and columns carefully.
Answer using exact values from the table.
If the answer is not present in the context, reply exactly:
"I don't know based on the provided recipe."

You can reply in Hindi, English, or Hinglish.
Use Hinglish if the user mixes languages.

Context:
{material}

User Question:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain= prompt | model

while True:
    print("--------------->")
    question=input("Ask Question (q to quit)")
    print("\n\n")
    if question=="q":
        break;
    docs = retriever.invoke(question)

    if not docs:
        print("❌ No relevant docs found")
        continue

    material = "\n\n".join(doc.page_content for doc in docs)
    #print(material)
    # material = retriever.invoke(question)   
    result = chain.invoke({"material":material,"question":question})
    print(result)



