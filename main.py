from decouple import config
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from src.extractors.tika import extract_content, OutputType
from src.llamaparser.chunkers.tokens import split_text_into_chunks_by_tokens
from src.llamaparser.prompts.chunking import toc_summary_synthesizer, synthesis_system_prompt
from src.llamaparser.prompts.cleanup import remove_extra_blank_lines, remove_extra_blank_prompt

openai_api_key = config("OPENAI_API_KEY", default="")

txt_content = extract_content("test.pdf")
with open("content.txt", "w") as f:
    f.write(txt_content.strip())

xhtml_content = extract_content("test.pdf", output_format=OutputType.XHTML)
with open("content.html", "w") as f:
    f.write(xhtml_content)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", remove_extra_blank_prompt),
    ("human", "{text}"),
])
chain = chat_prompt | ChatOpenAI(openai_api_key=openai_api_key)

doc_chunks = split_text_into_chunks_by_tokens(txt_content, tokens_per_chunk=4000, token_overlap=400)

toc = ""
for chunk in doc_chunks:
    toc_synthesis_prompt = ChatPromptTemplate.from_messages([
        ("system", synthesis_system_prompt),
        ("human", toc_summary_synthesizer)
    ])
    chain = toc_synthesis_prompt | ChatOpenAI(openai_api_key=openai_api_key)
    response = chain.invoke({"toc": toc, "chunk": chunk})
    toc = response.content
    print(f"\nResponse:\n{response}")

print(f"Final TOC: {toc}")
