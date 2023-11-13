import time
import random

def typing_speed_test():
    sample_text = "The swirled lollipop had issues with the pop rock candy. She saw the brake lights, but not in time.It caught him off guard that space smelled of seared steak."

    
    print("Type the following text:")
    print(sample_text)
    input("Press Enter when you are ready.")

    
    start_time = time.time()

    
    user_input = input("Start typing: ")

    
    end_time = time.time()

    
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    wpm = (words_typed / time_taken) * 60

    
    correct_characters = sum([1 for c1, c2 in zip(user_input, sample_text) if c1 == c2])
    accuracy = (correct_characters / len(sample_text)) * 100

    
    print("\nTyping Speed Test Results are:")
    print(f"Typing speed: {wpm:.2f} WPM")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the typing speed test
typing_speed_test()
