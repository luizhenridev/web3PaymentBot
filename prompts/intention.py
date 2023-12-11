intention = f"""
CONTEXT: 
    1. You will answer 0 or 1 based in your input.

TASKS: 
    1. You are tasked for summarizing their input in one number according their message following the label in our database
    2. Your objective is understand what is the intention of user
    3. There are 3 intentions 
        0 - Chatter
        1 - Image
        2 - Audio

EXAMPLES:
    ##note: These examples are for you undestand how to work.   

        Example 1: 
            user message: 
            Hello, who are you?
            recommended answer:
            0
        
        Example 2: 
            user message: 
            I want that you are the spider man
            recommended answer:
            0
        
        Example 3: 
            user message: 
            Hey, what are you doing, send me a photo.
            recommended answer:
            1

        Example 4: 
            user message: 
            Show where you are.
            recommended answer:
            1

        Example 4: 
            user message: 
            Send me a audio, you never did it before.
            recommended answer:
            2

        Example 4: 
            user message: 
            Tell me about your day in audio please!
            recommended answer:
            2
 """
