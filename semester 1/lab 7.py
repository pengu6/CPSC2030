import languagemodels





def get_topic(question):
    """Get the topic for a question


    Returns a single topic related to a question or None if not topic is
    found.

    This needs to only support a very restricted topic computation that
    will simply return the second capitalized word. For example, if we
    consider the question "Who created Python?", this function should return
    "Python"

    Note that this should not include punctuation after the topic. For
    example, "Python?" should not be returned for the previous example.

    Exampe usage:

    >>> get_topic("Who created Python?")
    'Python'

    >>> get_topic("How many moons does Saturn have?")
    'Saturn'

    >>> get_topic("What is the largest city in Germany?")
    'Germany'
    """
   
    uppercount = 0
    word = question.split()
    #cap = [word for word in words if word[0].isupper()]
    
    for word in word:
        for letter in word:
            if letter.isupper() == True:
                uppercount += 1
                if uppercount == 2:
                    if word.isalpha() == False:
                        return word[:len(word) - 1]
                    else:
                        return(word)
        
    #while len(cap) >= 2:
        #return cap[1]
    
        #if str(words.isalpha()) == False:
         #   return word[:len(word) - 1]
        #else:
         #   return(word)
    


def create_rag_prompt(question, context):
    """Create a prompt given a question and topic

    The prompt must in the following form exactly:

    "Answer from context: [user question] Context: [supplied context]"

    For example:

    >>> create_rag_prompt("Is it raining?", "It is raining")
    'Answer from context: Is it raining? Context: It is raining'
    """
    nstring = f"Answer from context: {question} Context: {context}"
    return nstring
    


def main():
    # Main program entry point
    
    
    # Function tests

    # Test for `get_topic`
    result = get_topic("What is Python?")
    expected = "Python"
    if result != expected:
        print("Test failed for get_topic.")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        exit(1)

    # Test for `create_rag_prompt`
    result = create_rag_prompt("Is it raining?", "It is raining")
    expected = "Answer from context: Is it raining? Context: It is raining"
    if result != expected:
        print("Test failed for create_rag_prompt.")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        exit(1)

    # TODO: Call `input` to get a question from the user
    question = input('Input a  question ')
    # TODO: Call `get_topic` to get a topic based on the question
    topic = get_topic(question)
    # TODO: Retrieve context from Wikipedia if we have a topic
    context = languagemodels.get_wiki(topic)
    # TODO: Create a prompt for the LLM by calling `create_rag_prompt`
    prompt = languagemodels.do(create_rag_prompt(question, context))
    # TODO: Generate a response from the LLM

    # TODO: Output the response
    print(prompt)

if __name__ == "__main__":
    main()
