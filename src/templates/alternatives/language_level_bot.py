language_level_refinement_alternatives = [
        # Basic instruction
        # Arguments: language_level
        "Rephrase the text to be on {0} level of CEFR language proficiency. All text must be grammatically correct.  ",

        # Basic instruction with language level description
        # Arguments: language_level, cefr_description
        "Rephrase the text to be on {0} level of CEFR language proficiency. The {0} level is defined as: {1}. All text must be grammatically correct. Do not change the meaning. Rephrase the text to COMPLETELY fit the {0} level of language proficiency definition: ",

        # Instruction + language level description + CoT
        # Arguments: language_level, cefr_description
        "Rephrase the text to be on {0} level of CEFR language proficiency. The {0} level is defined as: {1}. All text must be grammatically correct. Do not change the meaning. \n\nExamples of reasoning:\n\nSentence-> Lab supervisor: There is no way this can be achieved in just under 20 minutes, they must have gone mad.\nLevel-> A1\nThought-> Is there too complex vocabulary? Can the grammar be simplified? Can the most basic user understand this?\nRephrasing-> Lab supervisor: They could not do this in 20 minutes. They are crazy.\n\nSentence-> Comentator: Football matches can create great atmosphere in stadiums because football is competitive.\nLevel->  C1\nThought-> Can the grammar and vocabulary be improved? Does it fit C1 knowledge?\nRephrasing-> Comentator: The intensity and competitiveness of football matches can create an electrifying atmosphere in stadiums.\n\nRephrase the text to be on a {0} level. Only output the rephrasing."

    ]

