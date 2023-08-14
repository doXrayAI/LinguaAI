
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


language_level_prompts = [
    
    # Arguments: language_level, cefr_description, message
    # Average acc:  0.3666666666666667 Average percentage diff > 1:  0.1388888888888889
    ''' Rate the performance of waiter in the dialogue with respect to language proficiency matching the {0} level. {0} is defined as: {1}

Produce rating on a 1 to 3 scale for a message. Only output "1", "2" or "3". Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {0} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {0} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {0} description. 

Message: "{2}"
    ''',
    
    # Arguments: language_level, cefr_description, message
    # Average acc:  0.4 Average percentage diff > 1:  0.14999999999999997
    ''' Rate the performance of waiter in the dialogue with respect to language proficiency matching the {0} level. {0} is defined as: {1}

Produce rating on a 1 to 3 scale for a message. First output the rating "1", "2" or "3" and explain your reasoning. Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {0} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {0} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {0} description. 

Message: "{2}"
    ''',
    
    # Arguments: language_level, cefr_description, message
    # Average acc:  0.3388888888888889 Average percentage diff > 1:  0.2
    ''' Rate the performance of waiter in the dialogue with respect to language proficiency matching the {0} level. {0} is defined as: {1}

Produce rating on a 1 to 3 scale for a message. Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {0} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {0} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {0} description. 

Focus on grammar level, vocabulary complexity and sentence complexity. First output the rating "1", "2" or "3" and explain your reasoning.

Message: "{2}"
    ''',
    
    
        # Arguments: language_level, cefr_description, message -> DOESN'T USE CEFR DESCRIPTION
        # Average acc:  0.3222222222222222 Average percentage diff > 1:  0.20555555555555555
    ''' Rate the performance of waiter in the dialogue with respect to language proficiency matching the {0} level of CEFR language proficiency.

Produce rating on a 1 to 3 scale for a message. Only output "1", "2" or "3". Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {0} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {0} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {0} description. 

Message: "{2}"
    ''',
    
    
    # Arguments: language_level, cefr_description_extension, message
    # Average acc:  0.31666666666666665 Average percentage diff > 1:  0.19444444444444448
    
        ''' Rate the performance of waiter in the dialogue with respect to language proficiency matching the {0} level of CEFR language proficiency.

Produce rating on a 1 to 3 scale for a message. Only output "1", "2" or "3". Explanation of the scale:

1: Poor level match: the sentence proficiency level does not match the {0} description at all. The displayed proficiency level is either much higher or much lower.
2: Acceptable level match: the sentence proficiency level does not match the {0} description completely. The displayed proficiency level is either a bit higher or a bit lower.
3: Good level match: the sentence proficiency level matches the {0} description. 

Message: "{2}"
    ''',
]


