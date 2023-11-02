
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

        # Arguments: GPT_role, setting, dialogue_string, next_message
    '''Rate the performance of {0} in the dialogue with respect to the role fitness. We define role fitness as: the speaker uses appropriate language, vocabulary and sentences that are suitable and expected from a {0} in the explained setting, the speaker possesses knowledge, interests and personality of {0}. Produce rating on a 1 to 3 scale for a dialogue. First output "1", "2" or "3" and then explain the reasoning for the rating in a few sentences. Explanation of the scale:
1: Partial role fitness: the speaker rarely sounds like a {0} and rarely usea common sentences and actions that {0} does. The {0} is not adapted to the setting well. The sentence is only partially in the role.
2: Good role fitness: the speaker mostly sounds like a {0} and sometimes uses common sentences and actions that {0} do. The role fitness is good.
3: Perfect role fitness: the speaker sounds like a {0} all of the time and correctly and extensively uses common sentences and actions that {0} does. The sentence is completely in the role.

Take into account the setting.

Examples of ratings:

Setting: At a train station.
Role: Ticket salesperson
Message: Unfortunatelly, your train has already departed. The next one is in 20 minutes, would you like to purchase a ticket for that one?
Rating: 2
Reasoning: The response provided by the speaker mostly demonstrates acceptable role fitness for a ticket salesperson at a train station. The speaker correctly informs the customer about their train's departure status and offers an alternative option for the next train. However, the response could be improved to better align with the expected language and behavior of a ticket salesperson in this context. While the response includes appropriate information about the next train and offers a ticket purchase option, it lacks a bit of the courteous and customer-oriented tone that is typically associated with ticket salespeople. The response could benefit from incorporating more polite and welcoming language, such as "I'm sorry, but it appears that your train has already left. The next train is scheduled to depart in 20 minutes. Would you like to buy a ticket for that departure?" This adjustment would enhance the overall role fitness by better reflecting the knowledge and mannerisms of a ticket salesperson interacting with a customer at a train station.


Setting: In a cafe
Role: Bartender
Message: Good morning, what can I offer you today, we have  an exquisite offer of fresh juices if you are interested?
Rating: 3
Reasoning: The dialogue demonstrates a perfect role fitness for a bartender in a cafe setting. The speaker uses appropriate language, vocabulary, and sentences that are expected from a bartender. They greet the customer in a friendly manner, inquire about the customer's preferences, and mention a specific offer available (fresh juices). This aligns with the typical behavior of a bartender in a cafe, who would engage customers, suggest offerings, and create a welcoming atmosphere. The dialogue effectively captures the knowledge, interests, and personality of a bartender by showcasing their familiarity with the cafe's offerings and their proactive approach to engaging the customer. 

Setting: Talking to a student
Role: Professor
Message: Get out!
Rating: 1
Reasoning: The response "Get out!" is not fitting for a professor in a dialogue with a student. Professors typically maintain a respectful and professional tone when interacting with students. This response lacks the appropriate language and demeanor expected from a professor. It is not adapted well to the setting of a professor-student dialogue, resulting in poor role fitness.


Rate the following

Setting: {1}
Role: {0}
Message:
{3}

''',

        # Arguments: GPT_role, setting, dialogue_string, next_message
    '''Rate the performance of speaker with role of {0} in the dialogue with respect to the role fitness. We define role fitness as: the speaker uses appropriate language, vocabulary and sentences that are suitable and expected from role of a{0} in the explained setting, the speaker possesses knowledge, interests and personality of {0}. Produce rating on a 1 to 5 scale for a dialogue. First output "1", "2", "3", "4" or "5" and then explain the reasoning for the rating in a few sentences. Explanation of the scale:
1 - Not Applicable (N/A): The sentence is completely unrelated to the specified role and does not provide any relevant information or context related to the role. It does not contribute to understanding the individual's suitability for the role.

2 - Limited Relevance (LR): The sentence has some connection to the specified role, but the information provided is vague, unclear, or lacks depth. It does not sufficiently demonstrate the individual's qualifications, skills, or experience relevant to the role.

3 - Moderate Relevance (MR): The sentence contains relevant information related to the specified role, but the details provided are basic or generic. It offers a limited insight into the individual's fitness for the role, and further elaboration is needed to assess their suitability.

4 - Good Relevance (GR): The sentence provides clear and pertinent information regarding the specified role. It demonstrates the individual's qualifications, skills, or experience in a way that is directly related to the role. The information is sufficiently detailed and informative.

5 - Highly Relevant (HR): The sentence is highly relevant to the specified role and provides comprehensive and detailed information about the individual's qualifications, skills, experience, and attributes that directly align with the role's requirements. It gives a strong indication of the individual's excellent fitness for the role.

When evaluating sentences for role fitness, assess the extent to which the information provided in the sentence directly contributes to understanding the individual's suitability for the specified role. Consider the clarity, depth, and specificity of the information presented. Use the scale to assign a rating that reflects the sentence's relevance and significance to the role being evaluated.Take into account the setting.
Take the setting into account 

Examples of ratings:

Setting: In a cafe.
Role: Bartender.
Sentence: "The weather is really nice today."
Rating: 1
Reasoning: The provided sentence, "The weather is really nice today," is graded with a score of 1 (N/A) for the role of a bartender in a cafe setting. This is because the sentence is entirely unrelated to the role of a bartender and provides no relevant information about the individual's qualifications, skills, experience, or attributes that pertain to bartending. The sentence focuses on the weather, which has no direct connection to the responsibilities, tasks, or role of a bartender. As a result, it does not contribute to evaluating the individual's fitness for the specified role.

Setting: At a train station.
Role: Ticket salesperson
Message: "I've been to this train station many times before."
Rating: 2
Reasoning: While the sentence mentions being at the train station multiple times, it lacks direct relevance to the role of a ticket salesperson. The information provided is generic and does not offer any insight into the individual's qualifications, skills, or experience related to selling tickets. The sentence only establishes familiarity with the train station but does not demonstrate any connection to the role's requirements. As a result, it receives a Grade 2 (LR) rating on the scale, indicating limited relevance to the specified role.

Setting: At a train station.
Role: Ticket salesperson
Message: "I handle cash transactions, assist customers with their travel inquiries, and provide information about different ticket options at the train station."
Rating: 3
Reasoning: This sentence has moderate relevance to the specified role of a ticket salesperson in the setting of a train station. It outlines some of the basic tasks and responsibilities that are associated with the role. The mention of handling cash transactions, assisting customers with travel inquiries, and providing information about ticket options demonstrates a connection to the job functions of a ticket salesperson. However, the information provided is somewhat general and lacks specific details or examples to fully illustrate the candidate's qualifications or experience. To achieve a higher rating, the sentence could include more specific examples or elaborate on how the individual has successfully performed these tasks in previous roles.

While the sentence does mention traveling and meeting new people, it lacks direct relevance to the role of a ticket salesperson at a train station. The information provided is vague and does not offer any insight into the individual's qualifications, skills, or experience related to ticket sales or customer service. The sentence does not address the specific tasks, responsibilities, or qualities required for the role of a ticket salesperson, such as handling transactions, providing information about train schedules, assisting customers, or managing ticket sales operations. As a result, the sentence falls short in establishing a clear connection between the individual and the role, warranting a grade of 2 (Limited Relevance) on the evaluation scale.
Setting: In a cafe
Role: Bartender
Message: Good morning, what can I offer you today, we have  an exquisite offer of fresh juices if you are interested?
Rating: 4
Reasoning: This sentence demonstrates moderate to good relevance to the role of a bartender. The sentence begins with a friendly greeting, "Good morning," which is a positive interaction characteristic of a bartender's customer service. The phrase "what can I offer you today" aligns well with the responsibilities of a bartender, who is expected to provide drink options and suggestions to customers. The mention of an "exquisite offer of fresh juices" indicates the bartender's knowledge of the available menu items, showcasing familiarity with the offerings. The mention of "fresh juices" is particularly relevant as it highlights a key aspect of a bartender's role: crafting and serving beverages. The sentence includes an inviting tone, which is important for engaging with customers and encouraging them to explore menu options. While the sentence provides good relevance by addressing the key aspects of a bartender's role, it could be enhanced further by including more specific details about the types of fresh juices available or by adding a personal touch that reflects the bartender's expertise in mixology. Overall, the sentence effectively demonstrates the bartender's engagement with the customer and their ability to promote menu offerings.

Setting: Talking to a student about his preferences about his master's thesis
Role: Professor
Message: "As your professor, I am thrilled to discuss your preferences for your master's thesis. Given your exceptional performance in advanced data analysis courses and your demonstrated passion for environmental sustainability, I believe exploring the application of data-driven models to assess the impact of renewable energy initiatives would be an outstanding and impactful direction for your thesis. This aligns perfectly with your academic strengths and long-term career goals, allowing you to contribute meaningfully to both the field of data science and the advancement of sustainable practices."
Rating: 5
Reasoning: This sentence is graded with a 5 (Highly Relevant) because it demonstrates a thorough understanding of the role of a professor in the given setting and provides detailed and personalized guidance to the student about their master's thesis preferences. Direct Role Alignment: The sentence explicitly establishes the role of the professor and their expertise in guiding the student's academic decisions. Specific Acknowledgment: The professor acknowledges the student's past achievements and strengths, such as excelling in data analysis courses and displaying a passion for environmental sustainability. Detailed Guidance: The sentence offers specific and tailored advice by suggesting a thesis topic that leverages the student's strengths and interests. It outlines a clear and impactful direction related to renewable energy initiatives and data-driven models. Alignment with Goals: The sentence demonstrates an understanding of the student's academic and career aspirations, emphasizing how the proposed thesis topic aligns with both their strengths and long-term goals. Encouragement and Motivation: The professor's positive language ("thrilled to discuss," "outstanding and impactful direction") conveys enthusiasm, support, and encouragement, creating a motivating environment for the student. Overall, this sentence provides a comprehensive and personalized response that not only acknowledges the student's preferences but also offers expert guidance, aligns with their strengths and goals, and fosters a sense of enthusiasm and support. As a result, it is highly relevant and well-suited to the role of a professor engaging in a discussion about a master's thesis topic with a student.

Rate the following

Setting: {1}
Role: {0}
Message:
{3}

'''
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



