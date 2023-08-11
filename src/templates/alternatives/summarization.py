summarization_prompt_templates = [    
    "Summarize the following dialogue. Use the information from the previous summary.\n\nPrevious summary:{0}\n\nDialogue:\n\n{1}",
    
    "Create a summary from BOTH the dialogue and the previous summary. Previous summary is a text in $$ signs. Dialogue is a text in ## signs.\n\nPrevious summary:${0}$\n\nDialogue:\n\n#{1}#",
    
    "Create a concise summary from BOTH the dialogue and the previous summary. The summary should be 100 words or shorter. Previous summary is a text in $$ signs. Dialogue is a text in ## signs.\n\nPrevious summary:${0}$\n\nDialogue:\n\n#{1}#",
    
    "You are given a summary and a dialogue. Rephrase the summary to also contain the new information from the dialogue and it must be 100 words or shorter. Previous summary is a text in $$ signs. Dialogue is a text in ## signs.\n\nPrevious summary:${0}$\n\nDialogue:\n\n#{1}#"
]