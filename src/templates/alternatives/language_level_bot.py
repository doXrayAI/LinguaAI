language_level_refinement_alternatives = [
        # Basic instruction
        # Arguments: language_level
        "Rephrase the text in {3} to be on {0} level of CEFR language proficiency. All text must be grammatically correct.  ",

        # Basic instruction with language level description
        # Arguments: language_level, cefr_description
        "Rephrase the text in{3} to be on {0} level of CEFR language proficiency. The {0} level is defined as: {1}. All text must be grammatically correct. Do not change the meaning. Rephrase the text to COMPLETELY fit the {0} level of language proficiency definition: ",

        # Instruction + language level description + CoT
        # Arguments: language_level, cefr_description
        "Rephrase the text in {3} to be on {0} level of CEFR language proficiency. The {0} level is defined as: {1}. All text must be grammatically correct. Do not change the meaning. \n\nExamples of reasoning:\n\nSentence-> Lab supervisor: There is no way this can be achieved in just under 20 minutes, they must have gone mad.\nLevel-> A1\nThought-> Is there too complex vocabulary? Can the grammar be simplified? Can the most basic user understand this?\nRephrasing-> Lab supervisor: They could not do this in 20 minutes. They are crazy.\n\nSentence-> Comentator: Football matches can create great atmosphere in stadiums because football is competitive.\nLevel->  C1\nThought-> Can the grammar and vocabulary be improved? Does it fit C1 knowledge?\nRephrasing-> Comentator: The intensity and competitiveness of football matches can create an electrifying atmosphere in stadiums.\n\nRephrase the text to be on a {0} level. Only output the rephrasing.",
        
        "Rephrase the text in {3} to be on {0} level of CEFR language proficiency. The {0} level is defined as: {1}. {2}\n All text must be grammatically correct. Do not change the meaning. Rephrase the text to be on {0} level of language proficiency: ",
        
        "Rephrase the following text in {3} to be simpler without changing the meaning and tone. Use simpler words and grammar. Use shorter sentences. Text:"

]

language_level_examples = {
    'A1': [
            "I like to eat pizza. It is tasty.",
            "My cat is small and playful. It sleeps a lot.",
            "She goes to school every day. She learns many things."
    ],
     
    'A2': [    
            "I like to go to the park and play with my dog.",
            "She enjoys reading books and watching movies in her free time.",
            "We often meet for coffee and have a nice chat about our day." 
    ],
    
    'B1': [    
            "I enjoy taking walks in the park and admiring the beautiful flowers.",
            "She always helps me with my homework, and I'm really thankful for her assistance.",
            "The movie last night was so exciting, with lots of action scenes and unexpected twists."
    ],
    
    'B2' : [ 
            "I enjoy taking long walks in the park, especially during the vibrant colors of autumn.",
            "She carefully prepared a delicious homemade meal to share with her close friends.",
            "After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea."
    ],
    
    'C1': [ 
            "The intricate plot of the novel kept me engrossed from beginning to end, with its unexpected twists and complex characters.",
            "Having lived abroad for several years, I've gained a profound appreciation for diverse cultures and a deep understanding of global issues.",
            "The scientist's groundbreaking research not only expanded our understanding of the universe but also paved the way for revolutionary technological advancements."
    ],
    
    'C2': [ 
            "Exemplifying profound linguistic acumen, the orator delivered a discourse that both captivated and enlightened the discerning audience.",
            "The intricate interplay of hues in the impressionist masterpiece evokes a sense of ephemeral beauty that resonates deeply with the beholder.",
            "Through meticulous analysis of intricate datasets, the astute scientist unearthed novel correlations, thereby advancing our understanding of complex ecological systems."
    ]
}
