synthesis_system_prompt = "You extract information from documents. Do not provide commentary or edit the text or meaning of any of the text provided. Provide only what is requesed."

toc_summary_synthesizer = "We've been building a markdown table of contents for a document by reading it chunk by chunk. We have this so far:\n```{toc}```\nLooking at the next chunk of the document, identify any new sections you see in this chunk and append the section references to the existing table of contents as flawless markdown (remember the chunk may start in the middle of a section):\n```{chunk}```"

