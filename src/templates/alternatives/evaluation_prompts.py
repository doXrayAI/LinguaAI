
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
