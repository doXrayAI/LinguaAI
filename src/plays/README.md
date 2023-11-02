# Chatbot plays

Chatbot plays are used to simulate the conversaion betweeen a language learning chatbot and the user (played by another chatbot). Both chatbots are instantiated with the same setting, language, language level. The roles are reversed between the chatbots. A user defined refinement pipeline is assigned to the first chatbot. An identity pipeline is assigned to the second, user imitating, chatbot.

The aim of a chatbot play is to produce a dialogue in which one of the roles had a specific pipeline applied to it. The produced datasets are used to evaluate the pipeline according to two criteria: role fitness (scale 1-5) and language level (scale 1-3).

The dialogues have been generated with GPT-3.5-turbo anf GPT-4 models and can be found in their respective folders. The file naming format is the following: ```<refinement_bot>_<prompt_alternative>```.

The analysis of the evaluation results can be found in ```src/analysis/evaluation``` folder as CSV files and Jupyter notebooks.