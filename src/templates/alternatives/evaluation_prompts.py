
role_fitness_prompts = [
    
    # Arguments: GPT_role, setting, dialogue_string, next_message
    '''Rate the performance of {0} in the dialogue with respect to the role fitness. We define role fitness as: the speaker uses appropriate language, vocabulary and sentences that are suitable and expected from a {0} in the explained setting, the speaker possesses knowledge, interests and personality of {0}. Produce rating on a 1 to 3 scale for a dialogue. Only evaluate the next response, only output "1", "2" or "3". Explanation of the scale:
1: Poor role fitness: the speaker doesn't sound like a {0} and does not use common sentences and actions that {0} does. The {0} is not adapted to the setting well.
2: Acceptable role fitness: the speaker only sometimes sounds like a {0} and only sometimes uses common sentences and actions that {0} do.
3: Good role fitness: the speaker sounds like a {0} and  uses common sentences and actions that {0} does.

Take into account the previous dialogue and the setting.

Setting: {1}
Dialogue:

{2}

Next response:
{3}

''',



]


# Arguments: language, language_level, level_description, message, level_example_string, level_antiexample_string, ratings_example
language_level_prompts = [
    
    # Average acc:  0.3666666666666667 Average percentage diff > 1:  0.1388888888888889
    ''' Rate the message with respect to language proficiency matching the {1} level of {0}. {1} is defined as: {2}

Produce rating on a 1 to 3 scale for a message. Only output "1", "2" or "3". Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {1} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {1} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {1} description. 

Message: "{3}"
    ''',
    
    # Average acc:  0.4 Average percentage diff > 1:  0.14999999999999997
    ''' Rate the message with respect to language proficiency matching the {1} level of {0}. {1} is defined as: {2}

Produce rating on a 1 to 3 scale for a message. First output the rating "1", "2" or "3" and explain your reasoning. Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {1} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {1} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {1} description. 

Message: "{3}"
    ''',
    
    # Average acc:  0.3388888888888889 Average percentage diff > 1:  0.2
    ''' Rate the message with respect to language proficiency matching the {1} level of {0}. {1} is defined as: {2}

Produce rating on a 1 to 3 scale for a message. Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {1} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {1} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {1} description. 

Focus on grammar level, vocabulary complexity and sentence complexity. First output the rating "1", "2" or "3" and explain your reasoning.

Message: "{3}"
    ''',
    
    
        # Average acc:  0.3222222222222222 Average percentage diff > 1:  0.20555555555555555
    ''' Rate the message with respect to language proficiency matching the {1} level of CEFR language proficiency in {0}.

Produce rating on a 1 to 3 scale for a message. Only output "1", "2" or "3". Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {1} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {1} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {1} description. 

Message: "{3}"
    ''',
    
    
    # Average acc:  0.31666666666666665 Average percentage diff > 1:  0.19444444444444448
    
        ''' Rate the message with respect to language proficiency matching the {1} level of CEFR language proficiency in {0}.

Produce rating on a 1 to 3 scale for a message. Only output "1", "2" or "3". Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {1} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {1} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {1} description. 

Message: "{3}"
    ''',
    
    
    
        ''' Rate the message with respect to language proficiency matching the {1} level in {0}. {1} is defined as: {2}

Produce rating on a 1 to 3 scale for a message. First output the rating "1", "2" or "3" and explain your reasoning. Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {1} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {1} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {1} description. 

Examples of sentences that are {1} level:
{4}

Examples of Sentences that are NOT {1} level:
{5}


Message: "{3}"
    ''',
    
    
        ''' Rate the message with respect to language proficiency matching the {1} level of {0}. {1} is defined as: {2}

Produce rating on a 1 to 3 scale for a message. First output the rating "1", "2" or "3" and explain your reasoning. Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {1} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {1} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {1} description. 

Examples of ratings for {1} level:
{6}


Message: "{3}"
    ''',
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


language_level_antiexamples = {
    'A1': [
        "The intricate plot of the novel kept me engrossed from beginning to end, with its unexpected twists and complex characters.",
        "After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea."
    ],
    
    'A2': [
        "The intricate interplay of hues in the impressionist masterpiece evokes a sense of ephemeral beauty that resonates deeply with the beholder.",
        "The scientist's groundbreaking research not only expanded our understanding of the universe but also paved the way for revolutionary technological advancements."
    ],
    
    'B1': [
        "The intricate interplay of hues in the impressionist masterpiece evokes a sense of ephemeral beauty that resonates deeply with the beholder.",
        "Through meticulous analysis of intricate datasets, the astute scientist unearthed novel correlations, thereby advancing our understanding of complex ecological systems."
     ],
    
    'B2': [
        "I like to eat pizza. It is tasty.",
        "Exemplifying profound linguistic acumen, the orator delivered a discourse that both captivated and enlightened the discerning audience.",
    ],
    
    'C1': [
        "My cat is small and playful. It sleeps a lot.",
        "She goes to school every day. She learns many things."
    ],
    
    'C2': [
        "She goes to school every day. She learns many things."
        "We often meet for coffee and have a nice chat about our day." 
    ]
    
    
}

language_level_rating_examples = {
    'A1': ['Message: I like to eat pizza. It is tasty. Rating: 3',
           'Message: After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea. Rating: 2',
           'Message: Exemplifying profound linguistic acumen, the orator delivered a discourse that both captivated and enlightened the discerning audience. Rating: 1'
           ],
    'A2': ['Message: She enjoys reading books and watching movies in her free time. Rating: 3',
           'Message: I enjoy taking long walks in the park, especially during the vibrant colors of autumn. Rating: 2',
           'Message: Having lived abroad for several years, I\'ve gained a profound appreciation for diverse cultures and a deep understanding of global issues. Rating: 1'
           ],
    'B1': ['Message: She always helps me with my homework, and I\'m really thankful for her assistance. Rating: 3',
           'Message: After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea. Rating: 2',
           'Message: Through meticulous analysis of intricate datasets, the astute scientist unearthed novel correlations, thereby advancing our understanding of complex ecological systems. Rating: 1'
           ],
    'B2': ['Message: After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea.  Rating: 3',
           'Message: She enjoys reading books and watching movies in her free time. Rating: 2',
           'Message: I like to eat pizza. It is tasty. Rating: 1'
           ],
    'C1': ['Message: The intricate plot of the novel kept me engrossed from beginning to end, with its unexpected twists and complex characters. Rating: 3',
           'Message: I enjoy taking walks in the park and admiring the beautiful flowers. Rating: 2',
           'Message: She goes to school every day. She learns many things. Rating: 1'
           ],
    'C2': ['Message: Exemplifying profound linguistic acumen, the orator delivered a discourse that both captivated and enlightened the discerning audience. Rating: 3',
           'Message: She carefully prepared a delicious homemade meal to share with her close friends. Rating: 2',
           'Message: My cat is small and playful. It sleeps a lot. Rating: 1'
           ]
}


language_level_rating_examples_with_reasoning = {
    'A1': ['Message: I like to eat pizza. It is tasty. Reasoning: The vocabulary and grammar level match the description completely.The sentences are very simple, as expected from A1 level. Rating: 3',
           'Message: After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea. Reasoning: The vocabulary is a bit too complex for A1 level. Rating: 2',
           'Message: Exemplifying profound linguistic acumen, the orator delivered a discourse that both captivated and enlightened the discerning audience. Reasoning: The vocabulary, grammar and sentence complxity is very high, which is completely opposite from expectations from A1 level. Rating: 1'
           ],
    'A2': ['Message: She enjoys reading books and watching movies in her free time. Reasoning: The match of the message is perfect because because it demonstrates a basic understanding and use of present tense verbs, simple sentence structure, and common vocabulary. It expresses a simple idea about someone\'s leisure activities, which aligns with the language complexity typically expected at the A2 level. The Rating: 3',
           'Message: I enjoy taking long walks in the park, especially during the vibrant colors of autumn. Reasoning: The sentence "I enjoy taking long walks in the park, especially during the vibrant colors of autumn" may not completely match the A2 level of English proficiency because it includes some complex language elements that could challenge learners at that level. The use of "especially during the vibrant colors of autumn" involves a more advanced vocabulary ("especially" and "vibrant colors"), and the structure of the sentence is relatively complex with multiple phrases connected by commas. A2-level learners typically focus on simpler sentence structures and basic vocabulary to convey their ideas effectively. Still, the sentence and activity explained are rather simple, expected from A2 level. Rating: 2',
           'Message: Having lived abroad for several years, I\'ve gained a profound appreciation for diverse cultures and a deep understanding of global issues. Reasoning: The sentence is more complex and uses advanced vocabulary and grammatical structures that go beyond the typical comprehension and expression abilities of someone at an A2 level of English proficiency. A2 level typically involves basic sentence structures and vocabulary, while this sentence involves a complex participle construction ("Having lived abroad"), advanced vocabulary ("profound appreciation," "diverse cultures," "deep understanding," "global issues"), and a higher level of syntactical complexity. Reasoning: The sentence exceeds the B1 level of English proficiency by far due to its complexity, vocabulary, and structure. B1-level learners typically deal with simpler sentences and everyday vocabulary, while the given sentence uses advanced words and intricate phrasing that may be challenging for them to understand and use comfortably.Rating: 1'
           ],
    'B1': ['Message: She always helps me with my homework, and I\'m really thankful for her assistance. Reasoning: This sentence matches the B1 level of English proficiency because it demonstrates an ability to express gratitude and describe a recurring action. It includes a simple present tense ("She always helps me with my homework") to convey a habitual action and uses vocabulary like "thankful" and "assistance" to express feelings and convey ideas clearly. The sentence also maintains basic grammatical accuracy, which aligns with the B1 level\'s requirement for fundamental language skills. Rating: 3',
           'Message: After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea. Reasoning: The sentence demonstrates B1-level English proficiency partially because it effectively conveys a routine activity and preferences. However, it could be improved by using simpler vocabulary and more straightforward sentence structures to ensure full comprehension for B1-level readers. For instance, replacing "unwind" with "relax," and "soothing herbal tea" with "calming tea" could enhance clarity and align better with B1 proficiency.  Rating: 2',
           'Message: Through meticulous analysis of intricate datasets, the astute scientist unearthed novel correlations, thereby advancing our understanding of complex ecological systems. Rating: 1'
           ],
    'B2': ['Message: After a busy day at work, I like to unwind by reading a good book and sipping on a cup of soothing herbal tea. Reasoning: This sentence demonstrates a B2 level of English proficiency due to its ability to express a sequence of actions, convey personal preferences, and use descriptive language. It showcases a clear understanding of verb tenses, vocabulary related to relaxation activities, and the use of transitional phrases like "after" and "and" to connect ideas. Additionally, the sentence exhibits a grasp of common expressions ("unwind," "soothing herbal tea") that are indicative of an intermediate language skill level.  Rating: 3',
           'Message: She enjoys reading books and watching movies in her free time. Reasoning: The sentence "I enjoy taking walks in the park and admiring the beautiful flowers" partially matches the B2 level of English proficiency. It demonstrates the ability to express personal preferences and engage in simple activities, but it could further showcase higher proficiency by incorporating more complex sentence structures, varied vocabulary, and perhaps providing additional details or explanations about the enjoyment of walking in the park and admiring the flowers. This would contribute to a more comprehensive and sophisticated expression of the idea.  Rating: 2',
           'Message: I like to eat pizza. It is tasty. Reasoning: The sentence "I like to eat pizza. It is tasty." lacks complexity and depth necessary for a B2 level of English proficiency. B2-level writing typically involves more intricate sentence structures, varied vocabulary, and elaboration to express ideas and opinions. This sentence is relatively simple and lacks the sophistication expected at that proficiency level. Rating: 1'
           ],
    'C1': ['Message: The intricate plot of the novel kept me engrossed from beginning to end, with its unexpected twists and complex characters. Reasoning: This sentence showcases a C1 level of English proficiency due to its sophisticated vocabulary and complex sentence structure. It effectively communicates a nuanced response to a literary work, discussing the "intricate plot," "unexpected twists," and "complex characters," demonstrating an advanced understanding of narrative elements. The coherent flow and appropriate use of adjectives highlight the writer\'s ability to convey a detailed and insightful interpretation, indicating a strong command of the language at an advanced level. Rating: 3',
           'Message: I enjoy taking walks in the park and admiring the beautiful flowers. Reasoning: The sentence "I enjoy taking walks in the park and admiring the beautiful flowers" demonstrates a strong command of vocabulary and grammatical structures typically associated with a C1 level of English proficiency. However, to fully meet the requirements of C1, the sentence could benefit from a more complex sentence structure or the inclusion of more sophisticated vocabulary to showcase an even higher level of language proficiency. Rating: 2',
           'Message: She goes to school every day. She learns many things. Reasoning: The given sentence lacks complexity and variety in its language structures. A C1 level of English proficiency typically requires more sophisticated and varied vocabulary, along with complex sentence structures that demonstrate a higher level of fluency and expressiveness. The provided sentence, while grammatically correct, is too simple and does not exhibit the level of linguistic proficiency expected at the C1 level. Rating: 1'
           ],
    'C2': ['Message: Exemplifying profound linguistic acumen, the orator delivered a discourse that both captivated and enlightened the discerning audience. Reasoning: This sentence demonstrates a C2 level of English proficiency due to its sophisticated vocabulary, complex sentence structure, and nuanced use of language. The writer showcases a deep understanding of linguistic nuances, employing words like "exemplifying," "profound," "discourse," "captivated," and "enlightened." The seamless integration of these elements reflects an advanced command of English, suitable for effectively communicating with a discerning and educated audience. Rating: 3',
           'Message: She carefully prepared a delicious homemade meal to share with her close friends. Reasoning: The sentence demonstrates a high level of English proficiency (C2) due to its coherent structure, vocabulary variety, and accurate use of complex grammar. However, it falls short of complete C2 mastery as it lacks some nuanced elements such as highly sophisticated vocabulary choices and intricate sentence structures that are characteristic of native-like fluency. Rating: 2',
           'Message: My cat is small and playful. It sleeps a lot. Reasoning: The sentence provided is well-structured and conveys clear information about the cat\'s size, behavior, and sleeping habits. However, for C2 level of English proficiency, more sophisticated and nuanced language use is expected. A C2-level sentence would likely exhibit a richer vocabulary, complex sentence structures, and a higher level of precision and depth in expression. The given sentence, while accurate, lacks the depth and complexity typically associated with advanced language proficiency. Rating: 1'
           ]
}
