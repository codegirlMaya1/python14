# main_script.py

import text_utils as tu

# Test the functions from text_utils module
sample_text = "hello world"

reversed_text = tu.reverse_string(sample_text)
capitalized_text = tu.capitalize_string(sample_text)
uppercase_text = tu.to_uppercase(sample_text)
lowercase_text = tu.to_lowercase(sample_text)

print(f"Original: {sample_text}")
print(f"Reversed: {reversed_text}")
print(f"Capitalized: {capitalized_text}")
print(f"Uppercase: {uppercase_text}")
print(f"Lowercase: {lowercase_text}")
